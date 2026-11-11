# Prompt para o Claude Design: AJUSTES no INFO do Sistema de Cobertura (v2)

> Anexar junto com o prompt:
> 1. `INFO_Cobertura_p1` (página 1 atual: "Como calculamos a cobertura");
> 2. `INFO_Cobertura_p2` (página 2 atual: "Da cobertura à meta").
>
> Antes de enviar, preencha os colchetes `[ ]` (cor nova e logo).

---

Anexei as duas páginas atuais do INFO do **Sistema de Cobertura** (Nissey Máquinas · John Deere). **Não refaça do zero.** Mantenha o layout, a estrutura de blocos, o formato (2 páginas 16:9, 1280 × 720 px, para fundo de página do Power BI), a fonte e a legibilidade (texto mínimo de 11 px). Aplique só os ajustes abaixo e devolva as duas páginas completas.

## Ajustes gerais (páginas 1 e 2)

### G1. Trocar a cor verde

- Troque o verde forte das faixas (topo, cabeçalhos de seção, caixas de resultado) por **[COR NOVA, ex.: grafite #2B2F33 com destaque em verde #367C2B só nos detalhes]**.
- **Não mude** as cores da escala de cobertura (vermelho #C0392B, laranja #E67E22, verde-claro #A8C23A, verde #367C2B, cinza #BDBDBD) nem as cores do semáforo do ritmo da meta. Elas precisam bater com o painel.
- Mantenha o amarelo #FFDE00 só para destaques (selo "PÁGINA X DE 2" e "PADRÃO").

### G2. Logo e selo INFO

- **[ESCOLHA UMA]** Remova a logo John Deere do topo **ou** deixe-a pequena (no máximo a altura do texto "Nissey Máquinas").
- Adicione um selo **"INFO"** bem visível no topo, à esquerda do título (ex.: etiqueta arredondada "INFO" antes de "COMO CALCULAMOS A COBERTURA").

---

## Página 1: COMO CALCULAMOS A COBERTURA

### P1.1. Exemplo fictício com todos os produtos

O bloco **EXEMPLO FICTÍCIO · CIDADE MODELO** hoje mostra só TR6, TR5, CA e TRCE. Ele precisa mostrar **todos os 7 produtos** da tabela de premissas. Mesma cidade inventada (20.000 ha de grãos, 36.000 ha de pastagem, 100 ha de café). Substitua a tabela por esta:

| Produto | Área base | ÷ ha/máq. | Dem. | Parque | % Cob. | Gap |
|---|---|---|---|---|---|---|
| TR G | 20.000 ha grãos | ÷ 1.000 | 20 | 3 | 15% (laranja) | 17 |
| TR6 | 20.000 ha grãos | ÷ 800 | 25 | 4 | 16% (laranja) | 21 |
| TR5 | 36.000 ha pastagem | ÷ 1.800 | 20 | 1 | 5% (vermelho) | 19 |
| TRCE | 100 ha café | ÷ 25 | 4 | 1 | 25% (verde-claro) | 3 |
| CA | 20.000 ha grãos | ÷ 700 | 32 * | 30 | 94% (verde) | 2 |
| PV | 20.000 ha grãos | ÷ 1.500 | 14 | 5 | 36% (verde-claro) | 9 |
| **Total (sem PL)** | | | **115** | **44** | **38%** (verde-claro) | **71** |
| PL (linhas) ** | 20.000 ha grãos | ÷ 30 ha/linha | 667 linhas | 220 linhas | 33% (verde-claro) | 447 linhas |

- A linha de **PL** fica **abaixo do total**, separada por uma linha fina e em cinza/itálico, porque é medida em linhas e não entra no total.
- Rodapé da tabela:
  - "\* 20.000 ÷ 700 = 28,6, que arredonda para 29. Como o parque (30) passou de 29, a demanda sobe até a cobertura ficar abaixo de 100%: 30 ÷ 94% = 31,9, que arredonda para 32."
  - "\*\* PL: 220 linhas = 10 plantadeiras de 22 linhas. Fica fora do total."
- Card de resumo: **Demanda 115 · Parque 44 · Cobertura 38% · Gap 71**.
- Caixa de leitura: "**Leitura:** a cidade comporta 115 máquinas e tem 44 em uso, então a cobertura é de 38%. O gap é a soma das faltas de cada produto (17 + 21 + 19 + 3 + 2 + 9 = 71). A colheitadeira que passou da conta não aparece como 103%: ela vira demanda, e a cobertura nunca passa de 100%."
- Se faltar espaço, reduza o espaçamento das linhas da tabela, mas não corte produtos.

### P1.2. Quadro "QUAIS MODELOS ENTRAM EM CADA PRODUTO"

Substitua o quadro inteiro por este. O CA agora se divide em três portes, e os tratores antigos e os série 6/7 pequenos foram para o TR5:

| Produto | Famílias / modelos John Deere |
|---|---|
| TR G | Séries **7J, 7M, 8R e 9R** (7185J a 7230J, 7M 230, 8270R a 8400R, 9R 440, 9R 540, 9640R) e antigos **7715, 7815, 8420, 8430 e 9520** |
| TR6 | Série 6 acima de 150 cv: **6165J, 6170J/M, 6180J, 6190J/M, 6205J e 6210J/M** |
| TR5 | Série **5E** (5055E a 5090E) e antigos **5303, 5403, 5603, 5605 e 5705** · série 6 até 150 cv: **6100E/J, 6110D/E/J, 6115J, 6125D/E/J, 6130J, 6135J/M, 6145J e 6150J/M** · antigos **6415, 6600, 6605, 6615, 7500, 7505 e 7515** |
| TRCE | Tratores estreitos/fruteiros: **3036EN, 5060E e 5080EN** |
| CA P | **S430, S440**, **CA1165/1175** e **9470 STS** |
| CA M | **S540, S550, S5 500**, **CA1450/1470** e **9570 STS** |
| CA G | **S660 a S790, S7 700, S7 800, X9 1000**, **CA1550/1570** e **9650 a 9770 STS** |
| PV | Série **M4000** (M4025, M4030, M4040) e **PV400R** |
| PL | Séries **1100, 2100, 3100FT e DB** (DB40, DB50, DB74, DB90) |

Troque a nota que fica embaixo do quadro por:

"**TR5 × TR6 × TR G:** a fronteira é a potência e o uso, não o número da série. Tratores de **até 150 cv** contam como **TR5**, porque boa parte deles roda em pastagem. Isso vale para os série 6 pequenos e para os antigos 6000 e 7500. A 5060E conta como **TRCE**. **CA:** a demanda de colheitadeiras é calculada pela área de grãos e depois repartida entre P, M e G pelo mix de vendas da indústria. Modelos fora destes produtos (cana, forrageiras, construção, monitores, GPS etc.) não entram."

### P1.3. Tabela de premissas

- **TR G:** vida útil passa de 5 para **7 anos**.
- A linha **CA** vira "**CA (P, M e G)**", com 700 ha por máquina \* e 7 anos de vida útil para os três portes.

O resto da página 1 (cadeia da fórmula, escala de cores, notas e rodapé) **fica igual**.

---

## Página 2: DA COBERTURA À META

### P2.1. "Meta de M.S." vira "Objetivo JD (2030)"

Na cadeia do topo, troque a caixa `Meta de M.S. (%)` por **`Objetivo JD (2030) (%)`**.

- Legenda nova: "participação de mercado que a John Deere quer atingir até 2030 (ex.: 33% em tratores)".
- Se couber, abaixo da cadeia, uma mini-tabela de uma linha com o objetivo por porte:
  **Tratores:** Pequeno (TR5/TRCE) 34% · Médio (TR6) 40% · Grande (TR G) 60% — **Colheitadeiras:** CA P 49% · CA M 49% · CA G 60% — **PV e PL:** 33%.
- Troque "Meta de M.S." por "Objetivo JD (2030)" em **todos os lugares** da página 2 (bloco PV e PL, exemplo, cenários, notas). "Meta oficial do estado" vira "objetivo JD do estado".

### P2.2. "Participação" vira "relevância"

Na legenda da **Indústria projetada**, troque:
- de: "distribuído por estado e cidade conforme a participação de cada uma"
- para: "**distribuído por estado e cidade conforme a relevância de cada uma**"

### P2.3. Remover o "MS realizado"

- Apague a fórmula "**MS realizado** = Ganhas no FY ÷ Indústria projetada" abaixo da cadeia.
- No exemplo da cidade, apague o "→ MS realizado 20%" (ver P2.5).
- O espaço liberado vai para o novo "Esperado até hoje" (P2.4).

### P2.4. "Esperado até hoje" com a nova regra (sazonalidade)

O esperado **não é mais linear** (Meta × % do ano passado). Agora cada produto tem uma **curva de vendas ao longo do ano fiscal**, tirada do histórico de faturamento (FY23 a FY26). Substitua o texto atual por:

> **Esperado até hoje** = Meta × **% acumulado da curva de vendas do produto** até a data de referência. A curva vem do histórico de vendas FY23–FY26, por trimestre fiscal. O FY vai de novembro a outubro (FY27 = nov/26 a out/27). Com vários produtos selecionados, o % é a média ponderada pela meta de cada um.

Adicione uma mini-tabela "**Quanto se vende em cada trimestre do FY**" (pode ser uma mini barra horizontal empilhada por produto, sem eixo, com os % escritos):

| Produto | Q1 (nov–jan) | Q2 (fev–abr) | Q3 (mai–jul) | Q4 (ago–out) |
|---|---|---|---|---|
| TR G e PL | 19% | 8% | 25% | 48% |
| TR6 | 14% | 44% | 16% | 26% |
| TR5 | 19% | 17% | 27% | 37% |
| TRCE | 15% | 15% | 30% | 40% |
| CA (G, M e P) | 29% | 11% | 17% | 44% |
| PV | 21% | 13% | 23% | 43% |

Nota curta embaixo: "Dentro do trimestre, o peso é igual para os 3 meses. PL segue a curva do TR G."

### P2.5. Exemplo da meta da cidade explicado pelos cenários

O bloco **EXEMPLO FICTÍCIO · META DE UMA CIDADE** hoje aplica o objetivo do estado direto (30 × 33%). Ele precisa usar o **cenário**, como explicado no bloco "Cenários de meta por município" ao lado, e mostrar os **três cenários** para a mesma cidade.

Cidade do exemplo: indústria de **30 tratores grandes (TR G)/ano**, objetivo JD do estado **33%**, **share de frota 20%** (2 de 10 tratores da demanda já são nossos, o mesmo exemplo do bloco de cenários).

Tabela do exemplo (o Moderado destacado com o selo "PADRÃO"):

| | Conservador | **Moderado** | Agressivo |
|---|---|---|---|
| Share de frota (já é nosso) | 20% | 20% | 20% |
| + fatia do que falta (80%) | 10% → +8% | 25% → +20% | 40% → +32% |
| = Meta da cidade | **28%** | **40%** | **52%** |
| Piso (fator × 33%) | 16,5% ✓ | 24,8% ✓ | 33% ✓ |
| Vendas (30 × meta) | 8 | **12** | 16 |
| Negócios (÷ 23%) | 35 | **52** | 70 |

Abaixo, a linha do ritmo, só para o Moderado:

- "Fim do Q2 (abril): a curva do TR G acumula 19% + 8% = **27%** → esperado 12 × 27% = **3,25 vendas**."
- "Ganhas até agora: **4** → 4 ÷ 3,25 = 123% → **NO RITMO**" (selo verde, como hoje).
- Nota pequena: "Pela regra antiga (linear, 50% do ano), o esperado seria 6 e a cidade apareceria atrasada (4 de 6 = 67%, laranja). A curva respeita que o TR G vende quase metade do ano no Q4."

Mantenha a mini-legenda do % da meta comparado ao esperado (verde no ritmo 100%+, verde-claro > 80%, laranja > 50%, vermelho < 50%).

O bloco **CENÁRIOS DE META POR MUNICÍPIO** fica igual (só troque "meta oficial" por "objetivo JD"). O exemplo novo deve usar os mesmos números dele (share 20%, Moderado 40%) para as duas partes contarem a mesma história.

### P2.6. Rodapé "LEIA COM ATENÇÃO"

Fica igual, trocando "Meta" por "Objetivo JD" onde aparecer.

---

## Conferência antes de entregar

- [ ] Nenhum "Meta de M.S." nem "MS realizado" sobrou na página 2.
- [ ] "participação" da legenda da indústria virou "relevância".
- [ ] Exemplo da página 1 com os 7 produtos; PL fora do total; total 115 / 44 / 38% / 71.
- [ ] Exemplo da página 2 com os 3 cenários e o esperado pela curva (3,25, não 6).
- [ ] Verde das faixas trocado; cores da escala de cobertura e do semáforo intactas.
- [ ] Selo "INFO" no topo; logo removida ou reduzida.
- [ ] Nada de números reais da ADR e nenhuma fórmula ou premissa nova além das listadas.
