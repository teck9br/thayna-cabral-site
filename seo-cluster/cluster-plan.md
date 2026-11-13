# Cluster de conteúdo: advogado previdenciário Natal

Gerado em 12/11/2026. Dados: Ubersuggest (volume Brasil e Natal, Google Brasil em pt). Mapa interativo: `cluster-map.html`. Dados completos e matriz de links: `cluster-plan.json`.

## O que os dados mostram

1. **A busca local é pequena.** Em Natal, só "advogado previdenciário natal rn" tem volume medido (110/mês). As variações "advogado inss natal" e "advogado previdenciário natal inss" aparecem com 0. A página `/advogada-previdenciaria-natal/` já mira esse termo, e o que mais pesa nele é o Google Meu Negócio, ainda pendente.
2. **O volume está nas dúvidas, no Brasil todo.** "Aposentadoria especial" tem 90.500 buscas/mês, "BPC LOAS" 60.500, "auxílio-doença" 27.100, "aposentadoria por idade para mulher" 22.200 e "pensão por morte" 14.800. Como a Dra. atende online em todo o Brasil, um artigo que responde a essas dúvidas pode trazer cliente de fora de Natal.
3. **Os concorrentes são escritórios pequenos.** Além do gov.br, a primeira página tem escritórios com autoridade de domínio entre 4 e 39: lemosdemiranda.adv.br (29) é o 1º orgânico em "aposentadoria por idade para mulher", e bocchiadvogados.com.br (39), mariateixeiraadv.com.br (4) e barbieriadvogados.com (27) também aparecem. Um site novo consegue competir.
4. **Falta uma página de serviço para pensão por morte.** São 14.800 buscas/mês só no termo principal e outras 3.600 em "quem tem direito à pensão por morte", com intenção de contratar alta (família que perdeu alguém), e o site não tem página sobre o tema.

## Sobreposição dos resultados do Google

Comparei 11 páginas de resultados (top 10 orgânico). Nenhum par de termos dividiu 4 ou mais URLs: o máximo foi 1 URL em comum, entre "pensão por morte quem tem direito" e "tabela de idade". Por isso cada termo abaixo ganha a sua própria página, sem fusões. Os resultados se repetem por domínio (previdenciarista, jusbrasil, bocchi), não por página.

*Limitação:* a comparação não cobriu todos os pares, alguns resultados vieram com só 3 a 5 orgânicos e parte das coletas é de setembro e outubro de 2026. Os agrupamentos também se apoiam em intenção e termo principal.

## Arquitetura

A página-mãe continua sendo `/advogada-previdenciaria-natal/`. Cada página de serviço que já existe vira o centro do seu grupo, e os artigos novos ficam em `/blog/`, como no site da Antecipay. Um artigo (busca nacional, intenção de aprender) leva o leitor para a página de serviço (busca local, intenção de contratar), que tem o botão de WhatsApp.

| Grupo | Centro (já existe) | Artigos novos (`/blog/…`) | Termo principal | Busca/mês* |
|---|---|---|---|---|
| **Aposentadoria** | `/aposentadoria-natal/` | aposentadoria-por-idade-mulher | aposentadoria por idade para mulher | 22.200 |
| | | aposentadoria-rural | aposentadoria por idade rural | 14.700 |
| | | aposentadoria-quem-nunca-contribuiu | aposentadoria por idade nunca contribuiu | 12.300 |
| | | aposentadoria-especial | aposentadoria especial | 90.500 |
| **BPC/LOAS** | `/bpc-loas-natal/` | como-pedir-bpc-loas | como dar entrada no bpc loas | 2.180 |
| | | bpc-loas-autismo | bpc loas para autistas | 870 |
| | | bpc-loas-renda | bpc loas renda familiar | não medido |
| **Auxílio-doença** | `/auxilio-doenca-negado/` | auxilio-doenca-quem-tem-direito | auxílio doença quem tem direito | 7.880 |
| | | valor-auxilio-doenca | auxílio doença valor | 9.200 |
| | | prorrogacao-auxilio-doenca | pedido de prorrogação de auxílio doença | 1.620 |
| | | inss-negou-quem-paga-salario | se o inss negar o auxílio doença quem paga | 1.270 |
| **Pensão por morte** | **`/pensao-por-morte-natal/` (página nova no `build.py`)** | pensao-por-morte-tabela-idade | tabela de idade para receber pensão por morte | 7.350 |
| | | pensao-por-morte-filhos | pensão por morte para filhos | 4.700 |
| | | acumular-pensao-e-aposentadoria | sou aposentada posso receber pensão por morte | 2.150 |

\*Brasil, soma do termo principal com as variações que entram no mesmo artigo (a lista de cada um está no JSON).

No total: 1 página de serviço nova e 14 artigos, cerca de 20 mil palavras (artigos de 1.200 a 1.800 palavras).

**Canibalização evitada:** "bpc loas quem tem direito" (9.900) já é o alvo do título de `/bpc-loas-natal/`, então nenhum artigo usa esse termo. Os artigos de BPC tratam de assuntos mais específicos.

**Ficaram de fora:**
- Calendário do BPC: é notícia e muda todo mês.
- Consignado do BPC: cabe no Direito Bancário.
- Notícias do STF sobre aposentadoria especial: entram com data dentro do artigo, não como página própria.
- Termos do "Meu INSS": quem busca quer o aplicativo.

## Links internos (69 no mapa e mais 4 para outras áreas)

- Cada artigo linka a página de serviço do seu grupo, e a página de serviço linka todos os artigos do grupo. Isso pede uma seção "Leia também" nas páginas geradas pelo `build.py`.
- Cada artigo linka 2 artigos do mesmo grupo.
- Pontes entre grupos:
  - nunca contribuí ↔ como pedir BPC (quem não tem direito à aposentadoria muitas vezes tem direito ao BPC do idoso);
  - acúmulo de pensão → aposentadoria da mulher;
  - BPC e autismo → pensão para filhos;
  - auxílio-doença → aposentadoria especial.
- Links para as outras áreas:
  - "quem paga o salário" → `/advogada-trabalhista-natal/` (limbo previdenciário);
  - auxílio-doença → `/acidente-de-trabalho/`;
  - aposentadoria especial → `/revisao-beneficio-inss/`;
  - pensão por morte → `/inventario-natal/`.
- Todas as páginas recebem 3 ou mais links e nenhuma fica órfã. O texto do link é sempre o termo, nunca "clique aqui".

## Ordem de execução

| # | O quê | Por quê | Depende de |
|---|---|---|---|
| 0 | Instalar o Microsoft Clarity | Sem ele não dá para saber se o blog gera cliques no WhatsApp (o evento `whatsapp_click` já existe) | — |
| 1 | `/pensao-por-morte-natal/` no `build.py` | Falta no site, tem volume alto e intenção de contratar | — |
| 2 | Estrutura do `/blog/` (gerador como o `build_blog.py` da Antecipay, schema Article com autora e OAB, sitemap, "Leia também" nas páginas de serviço) | Base para todos os artigos | — |
| 3 | Aposentadoria da mulher, rural e "nunca contribuí" | Volume alto, concorrência fraca, e a aposentadoria rural fala direto com o interior do RN | 2 |
| 4 | Auxílio-doença: quem tem direito, e "quem paga o salário" | Leva para a página de auxílio negado e para a área trabalhista | 2 |
| 5 | Tabela de idade e pensão para filhos | Alimentam a página nova do item 1 | 1, 2 |
| 6 | Os artigos restantes de BPC e auxílio | Volume menor | 2 |
| 7 | Aposentadoria especial | Maior volume, mas o gov.br domina e o assunto está mudando no STF. Escrever quando a regra estiver estável e com data | 2 |

## Como saber se deu certo (ou não)

- **Sinal de que está funcionando** (Search Console, 8 a 12 semanas depois de publicar): impressões em `/blog/` e posição média abaixo de 20 nos termos principais.
- **Sinal de falha:** muitas impressões sem cliques indicam que título ou descrição não convencem; muitos cliques sem `whatsapp_click` no Clarity indicam que a ponte do artigo para a página de serviço não funciona. Nesse caso, reforce a chamada no meio do artigo antes de escrever mais artigos.
- **Canibalização:** se um artigo começar a aparecer em "advogado … natal" no lugar da página de serviço, o artigo está local demais. Tire "Natal" do título dele.

## Regras de conteúdo (lembrete)

- A Dra. Thayná revisa cada artigo antes de publicar.
- Respeitar o Provimento 205/2021: sem promessa de resultado, sem depoimento, sem "especialista".
- Valores (salário mínimo de 2026, teto, idades de transição) com data e revisão em janeiro.
- O artigo de aposentadoria especial depende de decisões do STF em andamento: data na frente e revisão a cada mudança.
