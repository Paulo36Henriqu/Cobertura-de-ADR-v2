"""Cliente 360 - extrai dados do ERP (Protheus, CMIXUT_121254_PR_PD) por CPF/CNPJ
e grava no DB_MKT para o Power BI "Cobertura de ADR v2".

Tabelas geradas (recriadas a cada execução):
- c360_erp_resumo: 1 linha por documento (financeiro em aberto, balcão de peças, oficina)
- c360_erp_os:     ordens de serviço da oficina dos últimos 36 meses

Uso: python cliente360_erp.py
"""
from datetime import datetime

from PyCodigosUteis.database import connect_to_database, connect_to_database_Tots

MESES_OS = 36

# Títulos a receber em aberto. Exclui adiantamentos/créditos (RA, NCC) e abatimentos (tipo terminado em "-").
SQL_FINANCEIRO = """
SELECT doc, COUNT(*) qtd_titulos_abertos, SUM(E1_SALDO) saldo_aberto,
       SUM(CASE WHEN venc < CAST(GETDATE() AS date) THEN E1_SALDO ELSE 0 END) saldo_vencido,
       SUM(CASE WHEN venc < CAST(GETDATE() AS date) THEN 1 ELSE 0 END) qtd_titulos_vencidos,
       MAX(CASE WHEN venc < CAST(GETDATE() AS date) THEN DATEDIFF(day, venc, GETDATE()) END) maior_atraso_dias,
       MIN(CASE WHEN venc >= CAST(GETDATE() AS date) THEN venc END) proximo_vencimento
FROM (
    SELECT LTRIM(RTRIM(a.A1_CGC)) doc, e.E1_SALDO, TRY_CONVERT(date, e.E1_VENCREA, 112) venc
    FROM SE1010 e
    JOIN SA1010 a ON a.A1_COD = e.E1_CLIENTE AND a.A1_LOJA = e.E1_LOJA AND a.D_E_L_E_T_ = ' '
    WHERE e.D_E_L_E_T_ = ' ' AND e.E1_SALDO > 0
      AND e.E1_TIPO NOT IN ('RA ', 'NCC') AND e.E1_TIPO NOT LIKE '%-%'
) x
WHERE doc <> ''
GROUP BY doc
"""

# Balcão de peças: orçamentos faturados (com NF).
SQL_BALCAO = """
SELECT LTRIM(RTRIM(a.A1_CGC)) doc,
       MAX(TRY_CONVERT(date, s.VS1_DATORC, 112)) ultima_compra_balcao,
       SUM(CASE WHEN s.VS1_DATORC >= CONVERT(char(8), DATEADD(month, -12, GETDATE()), 112) THEN s.VS1_VTOTNF ELSE 0 END) balcao_valor_12m,
       COUNT(DISTINCT CASE WHEN s.VS1_DATORC >= CONVERT(char(8), DATEADD(month, -12, GETDATE()), 112) THEN s.VS1_FILIAL + s.VS1_NUMNFI END) balcao_nfs_12m
FROM VS1010 s
JOIN SA1010 a ON a.A1_COD = s.VS1_CLIFAT AND a.A1_LOJA = s.VS1_LOJA AND a.D_E_L_E_T_ = ' '
WHERE s.D_E_L_E_T_ = ' ' AND s.VS1_NUMNFI <> ' ' AND LTRIM(RTRIM(a.A1_CGC)) <> ''
GROUP BY LTRIM(RTRIM(a.A1_CGC))
"""

# OS da oficina pelo proprietário da máquina (VO1_PROVEI/VO1_LOJPRO).
SQL_OS = f"""
SELECT LTRIM(RTRIM(a.A1_CGC)) doc, o.VO1_FILIAL filial, o.VO1_NUMOSV numero_os,
       LTRIM(RTRIM(o.VO1_CHASSI)) chassi,
       TRY_CONVERT(date, o.VO1_DATABE, 112) data_abertura,
       TRY_CONVERT(date, NULLIF(o.VO1_DATSAI, '        '), 112) data_saida,
       o.VO1_HORTRI horimetro,
       CASE o.VO1_STATUS WHEN 'A' THEN 'Aberta' WHEN 'D' THEN 'Liberada' WHEN 'F' THEN 'Fechada' WHEN 'C' THEN 'Cancelada' ELSE o.VO1_STATUS END status
FROM VO1010 o
JOIN SA1010 a ON a.A1_COD = o.VO1_PROVEI AND a.A1_LOJA = o.VO1_LOJPRO AND a.D_E_L_E_T_ = ' '
WHERE o.D_E_L_E_T_ = ' ' AND LTRIM(RTRIM(a.A1_CGC)) <> ''
  AND o.VO1_DATABE >= CONVERT(char(8), DATEADD(month, -{MESES_OS}, GETDATE()), 112)
"""

DDL_RESUMO = """
CREATE TABLE dbo.c360_erp_resumo (
    documento varchar(20) NOT NULL PRIMARY KEY,
    qtd_titulos_abertos int, saldo_aberto float, saldo_vencido float, qtd_titulos_vencidos int,
    maior_atraso_dias int, proximo_vencimento date,
    ultima_compra_balcao date, balcao_valor_12m float, balcao_nfs_12m int,
    os_12m int, os_abertas int, ultima_os date,
    data_atualizacao datetime NOT NULL
)"""

DDL_OS = """
CREATE TABLE dbo.c360_erp_os (
    documento varchar(20) NOT NULL, filial varchar(10), numero_os varchar(20), chassi varchar(40),
    data_abertura date, data_saida date, horimetro float, status varchar(20),
    data_atualizacao datetime NOT NULL
)"""


def _ler(cur, sql):
    cur.execute(sql)
    return cur.fetchall()


def main():
    agora = datetime.now()
    erp = connect_to_database_Tots().cursor()
    financeiro = {r.doc: r for r in _ler(erp, SQL_FINANCEIRO)}
    balcao = {r.doc: r for r in _ler(erp, SQL_BALCAO)}
    os_rows = _ler(erp, SQL_OS)
    print(f"ERP: financeiro {len(financeiro)} | balcão {len(balcao)} | OS {len(os_rows)}")

    limite_12m = agora.date().replace(year=agora.year - 1)
    oficina = {}
    for r in os_rows:
        o = oficina.setdefault(r.doc, {"os_12m": 0, "os_abertas": 0, "ultima_os": None})
        if r.status == "Cancelada":
            continue
        if r.data_abertura and r.data_abertura >= limite_12m:
            o["os_12m"] += 1
        if r.status in ("Aberta", "Liberada"):
            o["os_abertas"] += 1
        if r.data_abertura and (o["ultima_os"] is None or r.data_abertura > o["ultima_os"]):
            o["ultima_os"] = r.data_abertura

    resumo = []
    for doc in sorted(set(financeiro) | set(balcao) | set(oficina)):
        f, b, o = financeiro.get(doc), balcao.get(doc), oficina.get(doc, {})
        resumo.append((
            doc,
            f.qtd_titulos_abertos if f else None, f.saldo_aberto if f else None,
            f.saldo_vencido if f else None, f.qtd_titulos_vencidos if f else None,
            f.maior_atraso_dias if f else None, f.proximo_vencimento if f else None,
            b.ultima_compra_balcao if b else None, b.balcao_valor_12m if b else None,
            b.balcao_nfs_12m if b else None,
            o.get("os_12m"), o.get("os_abertas"), o.get("ultima_os"),
            agora,
        ))
    os_lista = [(r.doc, r.filial, r.numero_os, r.chassi, r.data_abertura, r.data_saida,
                 r.horimetro, r.status, agora) for r in os_rows]

    conn = connect_to_database("DB_MKT")
    cur = conn.cursor()
    cur.fast_executemany = True
    for tabela, ddl in (("c360_erp_resumo", DDL_RESUMO), ("c360_erp_os", DDL_OS)):
        cur.execute(f"IF OBJECT_ID('dbo.{tabela}') IS NOT NULL DROP TABLE dbo.{tabela}")
        cur.execute(ddl)
    cur.executemany("INSERT INTO dbo.c360_erp_resumo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", resumo)
    cur.executemany("INSERT INTO dbo.c360_erp_os VALUES (?,?,?,?,?,?,?,?,?)", os_lista)
    conn.commit()
    print(f"DB_MKT: c360_erp_resumo {len(resumo)} | c360_erp_os {len(os_lista)}")


if __name__ == "__main__":
    main()
