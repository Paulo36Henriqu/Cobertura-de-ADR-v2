# Prompt para o Claude Design: INFO do Sistema de Cobertura

> Anexar junto com o prompt:
> 1. o print da página INFO da Segmentação ("Como calculamos o potencial (ROB)"), como referência de estilo;
> 2. o print da página principal do Sistema de Cobertura, como referência de marca e de cores.

---

Crie uma página informativa (INFO) para um painel do Power BI chamado **Sistema de Cobertura**, da Nissey Máquinas (concessionária John Deere). O objetivo é explicar a vendedores, CENs e gerentes **como cada número do painel é calculado**, de um jeito que dê para entender em 1 minuto de leitura.

Siga **o mesmo estilo visual da página INFO da Segmentação de Clientes** (imagem anexa "Como calculamos o potencial (ROB)"): faixa verde no topo com o título à esquerda e "Nissey Máquinas | John Deere" à direita, uma cadeia de fórmula em caixas ligadas por operadores (× ÷ =), um exemplo fictício com números, blocos de premissas e uma faixa "LEIA COM ATENÇÃO" no rodapé.

## Formato

- 2 páginas em 16:9 (1280 × 720 px), para exportar como PNG e usar de fundo de página no Power BI.
- Página 1: **Como calculamos a cobertura**. Página 2: **Da cobertura à meta**.
- Fundo cinza bem claro (#F3F4F1), cards brancos com cantos levemente arredondados e cabeçalho de seção em faixa verde com título branco em caixa alta (igual à referência).
- Cores da marca: verde John Deere #367C2B, verde escuro #1E4D17, amarelo #FFDE00 (só para destaques, como a aba ativa no painel). Texto grafite #333.
- Fonte sem serifa, limpa (Segoe UI ou parecida). Títulos de seção em caixa alta.
- Nada de ícones decorativos em excesso. Prioridade é legibilidade: tamanho mínimo de texto equivalente a 11 px na tela de 1280 px.
- Tudo em português do Brasil.

---

## Página 1: COMO CALCULAMOS A COBERTURA

### Bloco 1 (topo, largura total): cadeia da fórmula

Três linhas de caixas, como a cadeia do ROB:

**Linha 1, Demanda**
`Área cultivada (ha)` ÷ `Hectares por máquina (ha/máq.)` = **DEMANDA (máquinas)**
- Legenda da Área: "IBGE · PAM, área plantada por município"
- Legenda do ha/máq.: "premissa por produto (tabela ao lado)"
- Legenda da Demanda: "quantas máquinas a área comporta, arredondado para cima"

**Linha 2, % Cobertura**
`Parque válido (máquinas)` ÷ `Demanda (máquinas)` = **% COBERTURA**
- Legenda do Parque válido: "chassis localizados na cidade e dentro da vida útil · ERP / Operation Center"
- Nota curta abaixo da linha: "**Limite de 100%:** quando o parque passa da demanda calculada pela área, a demanda sobe até o parque caber nela. A cidade fica entre 93% e 96% e o cliente e o grupo ficam em até 100%. Indústria e metas continuam usando a demanda pela área."

**Linha 3, Gap**
`Demanda` − `Parque válido` = **GAP (máquinas faltando)**
- Nota em destaque (caixa laranja clara, como a "PREMISSA" da referência): "O gap é calculado em cada **cidade × produto** e só depois somado. Cidade com frota sobrando **não compensa** cidade com falta."

### Bloco 2 (esquerda): EXEMPLO FICTÍCIO · CIDADE MODELO

Tabela com uma cidade inventada que tem 20.000 ha de grãos, 36.000 ha de pastagem e 100 ha de café:

| Produto | Área base | ÷ ha/máq. | Demanda | Parque válido | % Cob. | Gap |
|---|---|---|---|---|---|---|
| TR6 | 20.000 ha grãos | ÷ 800 | 25 | 4 | 16% (laranja) | 21 |
| TR5 | 36.000 ha pastagem | ÷ 1.800 | 20 | 1 | 5% (vermelho) | 19 |
| CA | 20.000 ha grãos | ÷ 700 | 32 * | 30 | 94% (verde) | 2 |
| TRCE | 100 ha café | ÷ 25 | 4 | 1 | 25% (verde-claro) | 3 |
| **Total** | | | **81** | **36** | **44%** | **45** |

- Pintar a célula de % Cob. com a escala de cores (Bloco 4).
- Rodapé da tabela: "* 20.000 ÷ 700 = 28,6, que arredonda para 29. Como o parque (30) passou de 29, a demanda sobe até a cobertura ficar abaixo de 100%: 30 ÷ 94% = 31,9, que arredonda para 32."
- Card lateral (como o card "Potencial / Faturamento / Participação" da referência): **Demanda 81 · Parque 36 · Cobertura 44% · Gap 45**.
- Caixa de leitura (verde claro): "**Leitura:** a cidade comporta 81 máquinas e tem 36 em uso, então a cobertura é de 44%. O gap é a soma das faltas de cada produto (21 + 19 + 2 + 3 = 45). A colheitadeira que passou da conta não aparece como 103%. Ela vira demanda, e a cobertura nunca passa de 100%."

### Bloco 3 (direita, em cima): PREMISSAS POR PRODUTO

| Produto | Descrição | Base de área | ha por máquina | Vida útil |
|---|---|---|---|---|
| TR G | Tratores grandes (grãos) | Grãos | 1.000 | 5 anos |
| TR6 | Tratores série 6 (grãos) | Grãos | 800 | 10 anos |
| TR5 | Tratores série 5 (pastagem) | Pastagem | 1.800 | 10 anos |
| TRCE | Tratores culturas especiais | Culturas especiais | 25 | 10 anos |
| CA | Colheitadeiras | Grãos | 700 * | 7 anos |
| PV | Pulverizadores | Grãos | 1.500 | 7 anos |
| PL | Plantadeiras (em **linhas**) | Grãos | 30 ha por linha ** | 10 anos |

Logo abaixo da tabela de premissas, adicione uma tabela compacta **"QUAIS MODELOS ENTRAM EM CADA PRODUTO"** (mesma largura, fonte um pouco menor, famílias em negrito):

| Produto | Famílias / modelos John Deere |
|---|---|
| TR G | Séries **7J, 7M, 8R e 9R** (7185J a 7230J, 7M 230, 8270R a 8400R, 9R 440, 9R 540, 9640R) e antigos **7500, 7505, 7515, 7715, 7815, 8420, 8430 e 9520** |
| TR6 | Série 6 média e grande: **6165J, 6170J/M, 6180J, 6190J/M, 6205J, 6210J/M** · série 6 pequena **ainda em revisão**: 6100E, 6110D/E/J, 6125D/E, 6130J, 6145J · antigos **6415, 6600, 6605 e 6615** |
| TR5 | Série **5E** (5055E a 5090E), antigos **5303, 5403, 5603, 5605 e 5705** e os série 6 de até 150 cv: **6100J, 6115J, 6125J, 6135J, 6135M, 6150J e 6150M** |
| TRCE | Tratores estreitos/fruteiros: **3036EN, 5060E e 5080EN** |
| CA | Série **S** (S430 a S790), **S5 e S7** (S5 500, S7 700, S7 800) e **X9 1000** |
| PV | Série **M4000** (M4025, M4030, M4040) e **PV400R** |
| PL | Séries **1100, 2100, 3100FT e DB** (DB40, DB50, DB74, DB90) |

Nota embaixo dela: "**TR5 × TR6:** a fronteira é a potência e o uso, não o número da série. Os tratores série 6 de até 150 cv (6100J a 6150M) contam como **TR5**, porque boa parte deles roda em pastagem. Os série 6 pequenos das linhas D, E e os 6130J/6145J seguem em TR6 até a revisão terminar. A 5060E conta como **TRCE** (cultura especial), não como TR5. Modelos fora destes 7 produtos (colhedoras de cana, forrageiras, construção, monitores, GPS etc.) não entram na cobertura."

Notas pequenas embaixo:
- **Grãos:** soja, arroz, feijão, algodão, sorgo, trigo, girassol e amendoim. O **milho fica fora** porque a safrinha é plantada na mesma área da soja.
- **Culturas especiais:** café, cacau, açaí, guaraná, urucum e mamão.
- **Área mínima:** cidade com menos de 500 ha da cultura tem demanda zero (exceto TRCE).
- \* Nas colheitadeiras, o ha por máquina pode variar por microrregião.
- \*\* PL: 1,5 ha por linha por dia × 20 dias de janela de plantio = 30 ha por linha.

### Bloco 4 (direita, embaixo): ESCALA DE CORES

Duas mini-legendas lado a lado:

**A · Escala absoluta** (cards, mapa e tabela A)
- Vermelho #C0392B: Crítico, abaixo de 10%
- Laranja #E67E22: Atenção, de 10% a 20%
- Verde-claro #A8C23A: Adequado, de 20% a 40%
- Verde #367C2B: Coberto, 40% ou mais
- Cinza #BDBDBD: Sem demanda

**B · Relativa à média da ADR** (tabela B por filial)
- Vermelho: menos de 0,75× a média
- Laranja: de 0,75× a 1×
- Verde-claro: de 1× a 1,5×
- Verde: 1,5× ou mais
- Frase curta: "Mostra quem está atrás dos colegas, mesmo quando todos estão críticos."

### Rodapé: faixa "LEIA COM ATENÇÃO" (ícone de exclamação laranja, como na referência)

Quatro colunas curtas:
1. **Chassi sem cidade não conta** como parque de nenhuma cidade e deixa a cobertura mais baixa do que é. Corrija na página Parque.
2. **PL é medida em linhas**, não em máquinas, e por isso fica fora do total geral. Para ver a PL, filtre só ela.
3. **CRM (ganhas / abertas)** é creditado ao **CEN dono da oportunidade**, não ao CEN da cidade.
4. **ha por máquina e vida útil são premissas ajustáveis.** Mudou a premissa, mudam demanda e gap.

---

## Página 2: DA COBERTURA À META

### Bloco 1 (topo, largura total): cadeia da meta

`Indústria projetada (máquinas/ano)` × `Meta de M.S. (%)` = **VENDAS DA META** ÷ `Taxa de conversão (23%)` = **NEGÓCIOS NECESSÁRIOS**

- Indústria projetada: "mercado total do ano fiscal, todas as marcas, distribuído por estado e por cidade conforme a participação de cada uma"
- Meta de M.S.: "meta oficial por estado e grupo de produto"
- Taxa de conversão: "fração das oportunidades do CRM que viram venda"

Abaixo, duas fórmulas menores lado a lado:
- **MS realizado** = Ganhas no FY ÷ Indústria projetada
- **Esperado até hoje** = Meta × % do ano fiscal já passado. O FY vai de novembro a outubro (FY27 = nov/26 a out/27). O % é contado até a data de referência no topo do painel.

### Bloco 1B (faixa estreita abaixo da cadeia): PV E PL · INDÚSTRIA ESTIMADA

PV e PL não têm indústria oficial. Por isso, a indústria deles é estimada pela demanda da cobertura:

`Demanda (máquinas)` × `Renovação de 10% ao ano` = **INDÚSTRIA ESTIMADA PV**
`Demanda (linhas)` ÷ `22 linhas (1 plantadeira média)` × `10% ao ano` = **INDÚSTRIA ESTIMADA PL (unidades)**

- Meta de M.S. e taxa de conversão de PV e PL: as mesmas do TR.
- Nota de fonte (caixa laranja clara, como a "PREMISSA"): "**Taxa de renovação de 10% ao ano:** validada em conversa com as marcas **[MARCA 1]** e **[MARCA 2]**, que indicaram **[resultado da conversa]**."
  > ⚠️ Antes de enviar ao Claude Design, troque os colchetes pelas marcas e pelo resultado reais. Se não puder citar as marcas, troque por "validada com fabricantes concorrentes".

### Bloco 2 (esquerda): EXEMPLO FICTÍCIO · META DE UMA CIDADE

- Indústria da cidade: 30 tratores/ano
- Meta 33% → **10 vendas**
- ÷ 23% de conversão → **43 negócios** no funil
- Ganhas até agora: 6 → MS realizado 20%
- Ano fiscal 50% decorrido → esperado 5 → **no ritmo** (verde)

Mini legenda do % da meta comparado ao esperado: verde no ritmo (100%+), verde-claro acima de 80%, laranja acima de 50%, vermelho abaixo de 50%.

### Bloco 3 (direita): CENÁRIOS DE META POR MUNICÍPIO

Explicar que a meta oficial é um % único por estado e que os cenários sugerem uma meta por cidade usando a cobertura:

Mostre o cálculo em 3 passos numerados:

1. **Share de frota** = Parque válido ÷ Demanda pela área (limitado a 100%). É quanto da frota da cidade já é nossa.
2. **Avanço** = share de frota + **fator** × (100% − share de frota). É conquistar uma fatia do que ainda não é nosso.
3. **Trava:** o avanço não passa do **teto**. Se a cidade já tem share acima do teto, vale o próprio share. E a meta nunca fica abaixo do **piso** = % × meta oficial do estado.

Fórmula compacta (fonte menor, abaixo dos passos): `Meta = MAIOR( piso × meta oficial ; MENOR( avanço ; MAIOR( teto ; share de frota ) ) )`

Depois, **Vendas do cenário** = Indústria da cidade × Meta do cenário, e **Negócios** = Vendas ÷ taxa de conversão. O cenário padrão do painel é o **Moderado**, e um slicer troca o cenário.

Tabela:

| Cenário | Fator do gap | Piso | Teto |
|---|---|---|---|
| Conservador | 10% | 50% da meta oficial | 60% |
| Moderado | 25% | 75% da meta oficial | 75% |
| Agressivo | 40% | 100% da meta oficial | 90% |

Exemplos em duas linhas (meta oficial de 33%):
- "Share de frota de 20%, cenário Moderado: 20% + 25% × 80% = **40%** (acima do piso de 75% × 33% = 24,8% e abaixo do teto de 75%)."
- "Share de frota de 5%, cenário Conservador: 5% + 10% × 95% = 14,5%, abaixo do piso de 50% × 33% = 16,5%. A meta fica em **16,5%**."

Nota: "Entram todas as cidades com indústria: tratores e colheitadeiras pela indústria oficial, PV e PL pela indústria estimada (Bloco 1B). **Fatores, pisos e tetos são a proposta atual** e ainda podem ser ajustados."

### Bloco 4 (faixa do meio, opcional se couber): CLIENTE E GRUPO ECONÔMICO

Duas caixas curtas:
- **Por Cliente:** mesma conta, mas a área vem das **propriedades cadastradas no CRM** e o parque vem do **CPF/CNPJ** do cliente. Área baixa no CRM = mercado que ainda não enxergamos.
- **Por Grupo:** soma todas as propriedades e CNPJs do grupo antes de calcular. Aqui a sobra de uma empresa **compensa** a falta de outra do mesmo grupo.

### Rodapé: faixa "LEIA COM ATENÇÃO"

1. **Meta CEN** cobre tratores + colheitadeiras. Com filtro de produto, ela é rateada pelo mix de vendas projetado.
2. **Cenários são sugestão**: os fatores, pisos e tetos podem ser ajustados.
3. **Ganhas e abertas** vêm do CRM John Deere, no ano fiscal corrente.
4. **Data de referência** no topo do painel mostra a última atualização dos dados.

---

## O que NÃO fazer
- Não usar números reais da ADR: só os exemplos fictícios acima, para a página não ficar desatualizada.
- Não inventar fórmulas, premissas ou nomes de produto além dos listados.
- Não usar gráficos decorativos. Esta página explica a conta, não mostra resultado.
