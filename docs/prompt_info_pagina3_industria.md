# Prompt para o Claude Design: INFO do Sistema de Cobertura, PÁGINA 3 (Indústria por cidade)

> Anexar junto com o prompt as páginas 1 e 2 do INFO (já com os ajustes do `prompt_ajuste_info_v2.md`), como referência de estilo.
>
> Antes de enviar, confirme o campo entre colchetes `[ ]` (de onde vem o % de cada estado).

---

Crie a **página 3** do INFO do **Sistema de Cobertura** (Nissey Máquinas · John Deere), no **mesmo estilo das páginas 1 e 2 anexas**: mesmo topo (selo "INFO", título à esquerda, "Nissey Máquinas" à direita), mesmas cores, cards brancos com cabeçalho em faixa, cadeia de fórmula em caixas ligadas por operadores (× ÷ =), exemplo fictício com números e faixa "LEIA COM ATENÇÃO" no rodapé.

- Formato: 16:9, 1280 × 720 px, para exportar como PNG e usar de fundo de página no Power BI.
- Texto mínimo equivalente a 11 px. Tudo em português do Brasil.
- O selo do topo passa a ser **"PÁGINA 3 DE 3"**. Nas páginas 1 e 2, troque para **"PÁGINA 1 DE 3"** e **"PÁGINA 2 DE 3"**.

Título da página: **COMO ESTIMAMOS A INDÚSTRIA POR CIDADE**

A ideia que a página precisa passar em 1 minuto: **a John Deere não informa a indústria por cidade, só o total. Nós repartimos esse total entre as cidades pelo tamanho do mercado de cada uma, que é a demanda calculada pela área (página 1).**

---

## Bloco 1 (topo, largura total): cadeia da indústria

Uma linha de caixas:

`Indústria da ADR (máquinas/ano)` × `% do estado` = **INDÚSTRIA DO ESTADO** × `Relevância da cidade` = **INDÚSTRIA DA CIDADE**

Legendas embaixo de cada caixa:
- **Indústria da ADR:** "mercado total projetado no ano fiscal, todas as marcas, por grupo (tratores e colheitadeiras)"
- **% do estado:** "[CONFIRMAR: fatia de cada estado na indústria, pelo histórico de vendas da indústria]"
- **Relevância da cidade:** "demanda da cidade ÷ demanda do estado, no mesmo grupo de produto"
- **Indústria da cidade:** "máquinas/ano que a cidade deve comprar, de todas as marcas"

Embaixo da cadeia, uma fórmula menor que mostra a relevância:

**Relevância da cidade** = `Demanda da cidade (pela área)` ÷ `Soma da demanda de todas as cidades do estado`

Nota de destaque (caixa laranja clara, como a "PREMISSA"): "**Por que pela demanda?** A demanda já mostra quantas máquinas a área de cada cidade comporta. Cidade com mais área de grãos ou de pastagem recebe uma fatia maior da indústria. Ela é a mesma demanda da página 1, **sem o limite de 100%**: a frota que passou da conta não muda a indústria nem a meta."

## Bloco 2 (esquerda, o maior): EXEMPLO FICTÍCIO · DO ESTADO À CIDADE MODELO

Use a **mesma cidade modelo da página 1** (20.000 ha de grãos, 36.000 ha de pastagem e 100 ha de café). Mostre em duas etapas.

**Etapa 1 · Indústria do estado** (duas linhas compactas):

| Grupo | Indústria da ADR | × % do estado | = Indústria do estado | Demanda do estado |
|---|---|---|---|---|
| Tratores | 1.000/ano | × 60% | **600/ano** | 3.000 máquinas |
| Colheitadeiras | 100/ano | × 60% | **60/ano** | 1.500 máquinas |

**Etapa 2 · Fatia da cidade**, uma linha por produto:

| Produto | Demanda da cidade | ÷ Demanda do estado | = Relevância | × Indústria do estado | = Indústria da cidade |
|---|---|---|---|---|---|
| TR G | 20 | ÷ 3.000 | 0,67% | × 600 | **4,0** |
| TR6 | 25 | ÷ 3.000 | 0,83% | × 600 | **5,0** |
| TR5 | 20 | ÷ 3.000 | 0,67% | × 600 | **4,0** |
| TRCE | 4 | ÷ 3.000 | 0,13% | × 600 | **0,8** |
| **Tratores** | **69** | | **2,3%** | | **13,8/ano** |
| CA P | 4 | ÷ 1.500 | 0,27% | × 60 | **0,16** |
| CA M | 4 | ÷ 1.500 | 0,27% | × 60 | **0,16** |
| CA G | 21 | ÷ 1.500 | 1,40% | × 60 | **0,84** |
| **Colheitadeiras** | **29** \* | | **1,9%** | | **1,2/ano** |

- Rodapé da tabela: "\* A demanda de CA da cidade é 29 (20.000 ÷ 700, pela área). Os 32 da página 1 têm o limite de 100%, que não entra aqui. Os 29 são repartidos entre P, M e G pelo mix de vendas da indústria do estado (ex.: 14% P, 14% M, 72% G → 4, 4 e 21)."
- Caixa de leitura (verde claro): "**Leitura:** a cidade tem 2,3% da demanda de tratores do estado, então recebe 2,3% da indústria: 13,8 tratores/ano de todas as marcas. Com o objetivo JD de 33%, a meta seria de 4,6 tratores/ano (página 2)."

## Bloco 3 (direita, em cima): PV E PL · INDÚSTRIA ESTIMADA

Mova para cá o bloco "PV e PL · Indústria estimada" que hoje está na página 2, com a mesma premissa de renovação de 10% ao ano (Mamoré, Tratoron e Daniel Tratores; idade média de 8 anos dos pulverizadores, BIM³ 2025). Acrescente a conta da cidade modelo:

- **PV:** demanda 14 × 10% = **1,4 pulverizador/ano**
- **PL:** 667 linhas ÷ 22 linhas × 10% = **3,0 plantadeiras/ano**

Frase curta: "PV e PL não têm indústria oficial. Por isso a indústria deles sai direto da demanda da cidade, sem passar pelo estado."

> Na página 2, no lugar do bloco que saiu, deixe só uma linha: "PV e PL: indústria estimada pela demanda × renovação de 10% ao ano (ver página 3)." Use o espaço liberado para dar respiro ao exemplo e aos cenários.

## Bloco 4 (direita, embaixo): QUEM SOMA COM QUEM

Uma tabela pequena com os grupos que dividem a mesma indústria:

| Grupo da indústria | Produtos que somam a demanda | Fonte da indústria |
|---|---|---|
| Tratores | TR G + TR6 + TR5 + TRCE | Oficial John Deere |
| Colheitadeiras | CA P + CA M + CA G | Oficial John Deere |
| Pulverizadores | PV | Estimada (demanda × 10%) |
| Plantadeiras | PL (em linhas ÷ 22) | Estimada (demanda × 10%) |

Nota: "Dentro de um grupo, a relevância de cada produto pesa pela demanda dele. Por isso cidade com muita pastagem recebe mais indústria de TR5, e cidade com muito grão recebe mais TR G e TR6."

## Rodapé: faixa "LEIA COM ATENÇÃO"

Quatro colunas curtas:
1. **É estimativa, não venda registrada.** A indústria por cidade é uma divisão do total do estado, e não o número de máquinas vendidas na cidade.
2. **Cidade sem demanda fica sem indústria.** Cidade com menos de 500 ha da cultura tem demanda zero (exceto TRCE) e não recebe fatia.
3. **Mudou a premissa, muda a indústria da cidade.** Alterar ha por máquina ou a área do IBGE mexe na relevância de cada cidade. O total do estado não muda.
4. **A indústria da cidade é a base da meta.** Vendas da meta = indústria da cidade × objetivo JD (página 2).

---

## O que NÃO fazer
- Não usar números reais da ADR. Use só os números fictícios acima, para a página não ficar desatualizada.
- Não inventar fórmulas, fontes ou premissas além das listadas.
- Não usar gráficos decorativos. A página explica a conta, não mostra resultado.
