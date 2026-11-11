# Prompt — Mockup do novo relatório "Inteligência Competitiva"

> Cole o bloco abaixo no gerador de mockup. Se a ferramenta aceitar imagens, anexe os prints de `prints/` **apenas como referência de identidade visual**: o relatório novo é outro produto, mas da mesma família.

---

Crie o mockup em alta fidelidade de um **novo relatório Power BI de várias páginas** chamado **"INTELIGÊNCIA COMPETITIVA"**, da **Nissey Máquinas** (concessionária **John Deere** na Amazônia Ocidental: RO, AC, AM, MT, RR), com base nas oportunidades do CRM. O relatório responde a 4 perguntas: **com quem disputamos, por que perdemos ou o cliente cancela, onde isso acontece e qual a diferença de preço**. Ele cobre as duas linhas da empresa: **AG** (agrícola: tratores, colheitadeiras, pulverizadores, plantadeiras) e **CE** (construção: escavadeiras, retroescavadeiras, pás-carregadeiras, motoniveladoras, rolos).

Gere **5 telas**, cada uma em **1366 × 768 px (16:9)**, sem rolagem.

## 1. Identidade visual (igual para todas as telas)

- **Faixa superior verde John Deere (#367C2B)** do topo até a metade dos cards de KPI; abaixo, fundo **cinza-claro (#E9E9E9)**.
- Título à esquerda em branco, caixa alta, negrito: **"INTELIGÊNCIA COMPETITIVA • <nome da página>"** (o "• <página>" em peso normal).
- À direita: **"Nissey Máquinas"** em branco negrito | divisor vertical branco | logo do cervo **John Deere** em branco. Abaixo, **"Referência: 09/10/2026"**.
- **Abas de navegação** abaixo do título, como botões arredondados verde-escuro (#2E6B24) com borda branca fina e texto branco negrito: `Visão Geral` · `Concorrentes` · `Perdas & Cancelamentos` · `Onde Perdemos` · `Preço & Modelos`. A aba ativa fica **amarela John Deere (#FFDE00) com texto preto**.
- **Linha de filtros** (cards brancos de cantos levemente arredondados, rótulo pequeno em cima e dropdown "Todos" com seta), igual em todas as páginas: **Período (FY)** · **Linha (AG / CE)** · **Filial** · **Vendedor** · **Produto** · **Concorrente** · **Resultado (Ganha / Perdida / Cancelada)**.
- **Cards de KPI brancos**: rótulo cinza no topo, número grande preto (~28 px), subtítulo pequeno cinza. Números críticos em **vermelho (#C0392B)** com a palavra de status abaixo (ex.: "Crítico").
- **Painéis de conteúdo** brancos, com **barra de título verde (#367C2B)** e texto branco, caixa alta, negrito e centralizado.
- Tabelas compactas em Segoe UI 9–10 px, com a linha de **Total** em negrito e borda superior.
- **Cores fixas por resultado em todo o relatório**: **Ganha = verde #2E7D32**, **Perdida = vermelho #C0392B**, **Cancelada = cinza-chumbo #7F8C8D**, **Aberta = verde-claro #A4C639**.
- **Formatação condicional**: vermelho #C0392B (ruim), laranja #E67E22 (atenção), verde-claro #A4C639 e verde #2E7D32 (bom).
- Números no padrão brasileiro: `1.017`, `22,9%`, `R$ 43,2 Mi`.
- Estilo corporativo, limpo e denso em informação, sem ilustrações, gradientes ou ícones 3D. Todos os textos em **português do Brasil**.

## 2. Tela 1 — "Visão Geral"

**KPIs (6 cards):**

| Card                         | Valor exemplo              | Subtítulo                                  |
| ---------------------------- | -------------------------- | ------------------------------------------- |
| Negócios encerrados no FY   | **1.659**            | FY26 (nov/25–out/26)                       |
| Ganhas                       | **557** (verde)      | 33,6% de conversão                         |
| Perdidas                     | **571** (vermelho)   | 34,4% · R$ 543 Mi                          |
| Canceladas pelo cliente      | **531** (cinza)      | 32,0% · R$ 711 Mi                          |
| Com concorrente identificado | **31,4%** (vermelho) | 346 de 1.102 perdidas + canceladas          |
| Concorrente nº 1            | **CATERPILLAR**      | 94 negócios (45 perdidos · 49 cancelados) |

**Conteúdo:**

- Esquerda (~40%): **"RESULTADO DOS NEGÓCIOS ENCERRADOS · POR LINHA"**, com barras 100% empilhadas (Ganha / Perdida / Cancelada) para AG e CE. Exemplo: AG 318 / 395 / 184; CE 239 / 176 / 347. Destaque que **em CE as canceladas superam as perdidas**.
- Centro (~35%): **"EVOLUÇÃO MENSAL · GANHAS × PERDIDAS × CANCELADAS"**, com colunas empilhadas por mês de nov/25 a out/26 e uma linha de % de conversão. Mostre um pico de canceladas em **set/26 (166)**.
- Direita (~25%): **"RESULTADO POR FILIAL"**, uma tabela com `Filial` · `Ganhas` · `Perdidas` · `Canceladas` · `Conversão %` (com formatação condicional). Exemplos: Manaus 214 / 111 / 230; Ariquemes 131 / 204 / 115; Rio Branco 61 / 72 / 40; Rolim de Moura 31 / 35 / 38; Pontes e Lacerda 52 / 42 / 59; Vilhena 38 / 53 / 9; Juína 15 / 33 / 11; Cáceres 9 / 6 / 21.

## 3. Tela 2 — "Concorrentes"

**KPIs:** Concorrentes distintos (**~35**) · Negócios disputados com concorrente identificado (**397**) · Vitória no confronto direto (**12,8%**, vermelho, "51 ganhas × 220 perdidas × 126 canceladas") · Líder em CE (**Caterpillar**, 26%) · Líder em AG (**Massey Ferguson**).

**Conteúdo:**

- Esquerda: **"RANKING DE CONCORRENTES · PERDIDAS + CANCELADAS"**, barras horizontais empilhadas por resultado (vermelho = perdida, cinza = cancelada, verde = ganha contra ele), top 12. Exemplos: Caterpillar 45 / 49 / 17; JCB 13 / 23 / 3; Komatsu 17 / 7 / 6; Case 14 / 10 / 8; Volvo 14 / 10 / 3; LiuGong 15 / 6 / 1; Hyundai 11 / 2 / 2; New Holland 17 / 5 / 3; Massey Ferguson 9 / 0 / 0; SDLG 9 / 3 / 0.
- Centro: **"CONCORRENTE × PRODUTO"**, uma matriz heatmap com linhas = concorrentes e colunas = Escavadeira, Retro, Pá-carregadeira, Motoniveladora, Rolo, Trator de esteira, Trator, Colheitadeira, Pulverizador.
- Direita: **"TENDÊNCIA · TOP 5 CONCORRENTES"**, com linhas mensais de negócios perdidos ou cancelados para cada um dos 5 maiores.

## 4. Tela 3 — "Perdas & Cancelamentos"

Esta tela trata **perdidas e canceladas lado a lado**, cada uma com o seu motivo.

**KPIs:** Perdidas (**571**) · Perdidas com motivo (**70,8%**) · Canceladas (**531**) · Canceladas com motivo (**0,4%**, vermelho, "campo criado em out/26") · Motivo nº 1 de perda (**OUTROS**, laranja, "30,8%: motivo genérico demais") · Motivo nº 1 identificável (**PREÇO**, 86).

**Conteúdo (duas metades espelhadas):**

- Metade esquerda, **"MOTIVOS DE PERDA"**:
  - Pareto (barras + linha acumulada): Outros 180, (Sem motivo) 167, Preço 86, Preferência de marca 64, Produto 45, Disponibilidade 19, Financiamento 4, Usado no negócio 4, Crédito recusado 2.
  - Abaixo, uma matriz **Motivo × Linha (AG / CE)**. Destaque que, em CE, Preço e Preferência de marca concentram tudo, enquanto em AG o motivo "Outros" domina.
- Metade direita, **"MOTIVOS DE CANCELAMENTO"**:
  - Barras com a lista oficial de motivos de cancelamento: Desistiu da compra · Adiou a compra · Sem recurso/crédito · Mudança de projeto ou prioridade · Comprou usado · Outros. Quase todas vazias; uma barra cinza grande para **"(Sem motivo) 529"**.
  - **Faixa de alerta amarela** (fundo #FFF4CC, borda #FFDE00, ícone ⚠): *"O motivo de cancelamento passou a existir no CRM em 09/10/2026. As canceladas anteriores não têm motivo. 126 delas têm concorrente informado (Caterpillar 49, JCB 23)."*
  - Abaixo, uma tabela **"CANCELADAS COM CONCORRENTE"**: `Concorrente` · `Qtd` · `Valor` · `Filial principal`.
- Rodapé da tela: **"PREENCHIMENTO POR VENDEDOR"**, uma tabela pequena com `Vendedor` · `Encerradas` · `% com motivo` · `% com concorrente` (com formatação condicional) para cobrar a qualidade do dado.

## 5. Tela 4 — "Onde Perdemos"

**KPIs:** Cidade com mais negócios disputados (**Manaus, 119**) · Filial mais disputada (**Manaus**) · Cidades com concorrente identificado (**~90**) · % de perdas + cancelamentos em CE concentrados em Manaus/AM (**~55%**).

**Conteúdo:**

- Esquerda e centro (~60%): **"MAPA · COR = CONCORRENTE PRINCIPAL · TAMANHO = PERDIDAS + CANCELADAS"**, um mapa satélite (estilo Azure Maps "Hybrid") da área de atuação, com bolhas por município. Cores dos concorrentes: Caterpillar amarelo-escuro, Komatsu azul, Volvo azul-marinho, Case vermelho-escuro, JCB laranja, Massey Ferguson vermelho, New Holland azul-claro, outros cinza. Bolhas principais: Manaus 119, Ariquemes 31, Boa Vista 22, Pontes e Lacerda 19, Juína 15, Porto Velho 15, Ji-Paraná 14, Vila Bela da Santíssima Trindade 12.
- Direita (~40%): **"FILIAL × CONCORRENTE"**, uma matriz heatmap em escala de vermelho. Linhas: ARI, CAC, JUI, MAO, PEL, RBR, ROL, VHA, RR, Total. Colunas: CAT, KOM, LIU, CASE, VOL, JCB, NH, MF, Outros, Total. MAO e ARI devem aparecer como as linhas mais quentes.

## 6. Tela 5 — "Preço & Modelos"

**KPIs:** Diferença de preço mediana (**JD +7% em CE · +18% em AG**, vermelho) · Negócios com preço do concorrente informado (**192**) · Perdas por PREÇO (**86**) · Maior diferença (**444G × LiuGong 838T, +40%**).

**Conteúdo:**

- Esquerda: **"PREÇO JD × PREÇO CONCORRENTE"**, um gráfico de dispersão com x = preço do concorrente, y = preço JD e uma diagonal tracejada de paridade. Pontos coloridos pelo resultado (ganha, perdida ou cancelada). A maioria dos pontos fica acima da diagonal.
- Direita: **"DUELO DE MODELOS · JD × CONCORRENTE"**, uma tabela com `Modelo JD` · `Modelo concorrente` · `Qtd` · `Ganhas` · `Perdidas` · `Canceladas` · `Preço JD` · `Preço conc.` · `Δ %` (positivo = vermelho, ou seja, nós mais caros). Exemplos:
  - 310P × JCB 3CX — 31 — R$ 430 mil — R$ 380 mil — **+12%**
  - 310P × CAT 416F2 — 19 — R$ 450 mil — R$ 465 mil — **−3%** (verde)
  - 444G × Volvo L60H — 12 — R$ 690 mil — R$ 640 mil — **+7%**
  - 210P × CAT 320D2 — 8 — R$ 860 mil — R$ 830 mil — **+4%**
  - 444G × LiuGong 838T — 6 — R$ 690 mil — R$ 415 mil — **+40%**
  - TR5080E × MF 4707 — 5 — R$ 230 mil — R$ 195 mil — **+15%**

---

## Notas técnicas para a implementação real (não vão para o gerador)

**Fonte:** banco `DB_MKT_CRM_JD_CE`.

- Tabela principal: `dbo.oportunidades` (3.087 linhas não deletadas).
- Lookups em `dbo.configuracao_valores`, nas categorias `fase`, `motivo_perda`, `motivo_cancelamento`, `filial` e `fabricante`.
- Catálogo de concorrentes: `dbo.concorrentes_catalogo` (559 modelos, com `fabricante` / `linha` / `produto` / `modelo`).
- Auditoria de alterações: `dbo.historico_oportunidades`.

**Campos usados:**

- `fase_id`. A coluna `status` está sempre nula.
- Motivos: `motivo_perda_id` e `motivo_cancelamento_id`.
- Concorrência: `concorrente`, `produto_concorrente`, `modelo_concorrente`, `preco_concorrente`.
- Valores: `preco_unitario`, `preco_total`, `quantidade`.
- Localização e responsáveis: `id_ibge`, `cidade`, `uf`, `filial_id`, `vendedor_id`.
- Outros: `linha` (AG/CE), `produto`, `modelo`, `data_encerramento`, `data_criacao`.

**Resultado (por fase):**

- `5.FATURADA` = ganha.
- `6.PERDIDA` = perdida.
- `7.CANCELADA PELO CLIENTE` = cancelada.
- `1.`–`4.` = aberta.

**Lista de motivos:**

- **Perda:** Preço, Financiamento, Preferência de marca, Produto, Disponibilidade, Suporte do distribuidor, Crédito recusado, Usado no negócio, Outros.
- **Cancelamento:** Desistiu da compra, Adiou a compra, Sem recurso/crédito, Mudança de projeto ou prioridade, Comprou usado, Outros.

**FY26 (encerramento a partir de 01/11/2025):**

| Linha | Ganhas | Perdidas | Canceladas | Perdidas com motivo | Canceladas com motivo | Perdidas com concorrente | Canceladas com concorrente |
| ----- | ------ | -------- | ---------- | ------------------- | --------------------- | ------------------------ | -------------------------- |
| AG    | 318    | 395      | 184        | 302                 | 2                     | 47                       | 0                          |
| CE    | 239    | 176      | 347        | 102                 | 0                     | 173                      | 126                        |

**Cuidados de qualidade encontrados:**

- **Motivo de cancelamento é novo.** O primeiro registro no histórico é de **09/10/2026**. As canceladas antigas não têm motivo; nas de CE, o melhor sinal disponível é o campo `concorrente`, preenchido em 126 de 347.
- **AG quase sem concorrente no histórico.** Só 72 das 784 perdas AG (de todo o período) têm concorrente. O preenchimento chega a ~100% a partir de **set/26** (o histórico registra os campos de concorrente desde 13/07/2026). Em AG, o concorrente vem quase só quando o motivo é PREÇO. CE está ~100% preenchido nas perdas desde nov/25.
- **Perdas sem motivo.** AG tem 93 perdidas sem motivo no FY26 e CE tem 74, mesmo com concorrente preenchido. O motivo "OUTROS" responde por 176 das 302 perdas AG que têm motivo. Vale revisar a lista de motivos com o comercial.
- **Valores das canceladas.** O `preco_total` das canceladas soma R$ 711 Mi no FY. Antes de exibir, conferir outliers e oportunidades duplicadas (é comum recriar a oportunidade depois de cancelar).
- **Normalização de nomes de concorrente:**
  - `JBC` → `JCB`.
  - `CASE IH` (AG) × `CASE` (CE).
  - Aplicar `UPPER`/`TRIM`.
  - Excluir valores que não são marcas: `CONSÓRCIO`, `SEM`, `OUTROS`.
  - Tratar `JOHN DEERE A&T` como categoria separada (provável outro dealer JD ou usado).
- **Preço do concorrente com placeholder.** Há valores como `0,01`; considerar só `> 1.000` no cálculo do Δ de preço.
- **Mapa por município é viável.** O `id_ibge` está preenchido em 449 das 460 oportunidades com concorrente.
- **Exemplos aproximados.** Os pares da tabela "Duelo de modelos" são reais, mas os preços e algumas quantidades foram arredondados. O mesmo vale para as estimativas marcadas com "~" nas telas 4 e 5.
