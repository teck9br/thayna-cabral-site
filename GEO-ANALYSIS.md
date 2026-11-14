# Análise GEO (busca por IA): thaynacabraladvocacia.com.br

Data: 14/11/2026 · Escopo: 35 páginas (home, 21 de serviço com as 3 páginas-mãe, índice do blog, 13 artigos), arquivos locais de `site/` conferidos com o site no ar.

Ponto de partida: o Google diz que otimizar para a busca com IA "continua sendo SEO" (guia de otimização para IA do Search Central). As recomendações abaixo são SEO aplicado às respostas de IA, não uma disciplina à parte.

## 1. Nota GEO: 68/100

| Critério | Peso | Nota | Resumo |
|---|---|---|---|
| Citabilidade | 25 | 19 | Artigos com "Resposta rápida", números de 2026 e exemplos de cálculo. Nas páginas de serviço, o H1 é um slogan e a resposta direta vem depois. |
| Estrutura | 20 | 16 | Hierarquia H1→H2→H3 limpa, listas, FAQ em todas as páginas, tabelas em 7 páginas. Os H2 das páginas de serviço são afirmações, não perguntas. |
| Multimídia | 15 | 5 | Só fotos (2 por página). Nenhum vídeo, infográfico ou calculadora. |
| Autoridade e marca | 20 | 9 | Artigos com autora + OAB + data. Páginas de serviço sem data. **Nenhum link para fonte primária** (lei, INSS, STF) em todo o site. `sameAs` só aponta para a Antecipay. Sem Perfil da Empresa no Google nem redes sociais. |
| Acesso técnico | 20 | 19 | HTML estático (sem dependência de JavaScript), todos os robôs liberados, sitemap e IndexNow ativos. |

## 2. Prontidão por plataforma (qualitativa: não medida com ferramenta)

- **Google AI Overviews / AI Mode:** boa base técnica; depende de ranquear no top 10 e de sinais locais (falta o Perfil da Empresa). AI Mode pesa atualidade e autoridade da entidade, os pontos mais fracos hoje.
- **ChatGPT Search:** `OAI-SearchBot` liberado e recebendo 200. Pouca presença da marca fora do site, então a citação fica restrita a perguntas muito específicas.
- **Perplexity:** `PerplexityBot` liberado. A Perplexity cita muito fóruns e comunidades, onde a marca não aparece.
- **Bing Copilot:** IndexNow já usado; bom.

## 3. Acesso dos robôs de IA (cada um com o que governa)

Testado no ar em 14/11/2026: `/bpc-loas-natal/` respondeu 200 com o HTML completo (48 KB) para todos.

| Robô | Governa | Situação |
|---|---|---|
| Googlebot | Busca Google, AI Overviews e AI Mode | Liberado (`User-agent: *`) |
| OAI-SearchBot | Citação no ChatGPT Search | Liberado |
| ChatGPT-User | Navegação do ChatGPT a pedido do usuário | Liberado |
| PerplexityBot | Busca da Perplexity | Liberado |
| Claude-SearchBot | Citação na busca do Claude | Liberado |
| Applebot | Siri, Spotlight, Safari | Liberado (`*`) |
| Bingbot | Bing e Copilot | Liberado (`*`) |
| GPTBot | Só treino de modelos da OpenAI | Liberado |
| ClaudeBot | Só treino de modelos da Anthropic | Liberado |
| Google-Extended | Treino e grounding do Gemini/Vertex (não afeta AI Overviews) | Liberado |
| CCBot, Applebot-Extended | Só treino | Liberados por `*` |

Os robôs de treino são escolha de licenciamento, não de visibilidade. Correção pequena: o comentário do `robots.txt` diz que liberar esses robôs faz aparecer no Gemini; quem decide o AI Overviews/AI Mode é o Googlebot. Não muda nada no funcionamento.

## 4. llms.txt

Presente (`/llms.txt`, 200), com dados do escritório, áreas e lista de páginas gerada pelo `build.py`. O Google diz que não usa nem precisa desse arquivo; nenhum grande buscador de IA confirmou usá-lo. **Peso zero na nota.** Pode ficar como está: custa nada manter.

## 5. Menções à marca

| Canal | Situação |
|---|---|
| Perfil da Empresa no Google | **Não existe** (pendência no CLAUDE.md). Maior lacuna para buscas locais e para o AI Mode. |
| Instagram / LinkedIn / YouTube | Não existem ou não estão ligados no `sameAs`. |
| Wikipedia / Wikidata | Não se aplica a um escritório desse porte; não vale o esforço. |
| Cadastro Nacional dos Advogados (OAB) | Existe por natureza; vale citar no texto do Sobre como forma de conferência. |
| Página na Antecipay | Único `sameAs` atual. |

Os estudos de terceiros (Ahrefs, 12/2025) apontam menções em YouTube e Reddit como mais ligadas à citação por IA do que backlinks. Para advocacia, o equivalente realista é: Perfil da Empresa, Instagram e vídeos curtos respondendo às mesmas perguntas dos artigos, sempre dentro do Provimento 205/2021.

## 6. Citabilidade por trecho

**Bons exemplos (prontos para serem citados):**
- Blogs: o bloco "Resposta rápida" logo depois do título, nos 13 artigos. Exatamente o formato que favorece a citação (resposta no primeiro terço da página).
- `blog/bpc-loas-renda/` › "Como fazer a conta": exemplo numérico (aposentadoria de R$ 2.000 ÷ 2 = R$ 1.000 por pessoa) que se sustenta sozinho.
- `bpc-loas-natal/` › "Quem tem direito": lista objetiva (65 anos, impedimento de pelo menos 2 anos, CadÚnico).

**Fracos:**
- H1 das páginas de serviço em forma de slogan ("BPC/LOAS: um salário mínimo por mês para quem mais precisa."). O texto logo abaixo já é bom; o problema é o título não responder a uma pergunta.
- H2 "O que é bom saber": genérico, não diz do que trata o trecho.
- Trechos que afirmam decisões do STF ou mudanças de lei sem dizer qual decisão ou qual lei com link.

## 7. Renderização no servidor

Sem problema: HTML estático, conteúdo inteiro no `<main>` sem JavaScript (o `fx.js` só dá sombra ao cabeçalho). Robôs que não rodam JS (GPTBot, PerplexityBot) leem tudo.

## 8. As 5 mudanças de maior impacto

1. **Criar o Perfil da Empresa no Google** e pôr a URL no `sameAs` do JSON-LD. Maior efeito em "advogada previdenciária Natal" no mapa, no AI Overviews e no AI Mode.
2. **Citar fontes primárias com link** em páginas de serviço e artigos: Lei 8.213/91, Lei 8.742/93 (LOAS) art. 20, EC 103/2019, Lei 15.077/2024, portarias de valores de 2026, decisões do STF com o número (ex.: RE 567.985 sobre o critério de renda do BPC). Fonte: planalto.gov.br, gov.br/inss, portal.stf.jus.br. Em tema "seu dinheiro, sua vida", é o sinal de confiança que mais falta. Dá para fazer no `build.py`/`posts.py` com um campo `fontes` renderizado como "Fontes" no fim da página.
3. **Data de atualização visível nas páginas de serviço** ("Atualizado em novembro de 2026", com `dateModified` no JSON-LD), tirada do `lastmod.json` que já existe. Os valores de 2026 e as regras de transição mudam todo ano; a data mostra que a página está em dia.
4. **H2 em forma de pergunta nas páginas de serviço**, com a resposta na primeira frase: "Quem tem direito ao BPC/LOAS?", "Qual a renda exigida para o BPC em 2026?", "Por que o INSS nega o BPC?". Trocar "O que é bom saber" por um título que diga o assunto. Abaixo do H1, uma frase-resposta de 40–60 palavras (já existe na maioria; conferir).
5. **Uma calculadora simples** (renda por pessoa do BPC ou tabela da pensão por morte por idade) em HTML/JS sem servidor, no artigo correspondente. É o único item que dá conteúdo próprio, que outros sites não têm, e cobre o critério de multimídia. Manter o texto e a tabela no HTML para os robôs que não rodam JS.

## 9. Recomendações de schema

- `Person` (Dra. Thayná): acrescentar ao `sameAs` o Perfil da Empresa, Instagram e LinkedIn assim que existirem; `knowsAbout` com as áreas ("Direito Previdenciário", "BPC/LOAS"…).
- Páginas de serviço: `dateModified` no `Service`/`WebPage`, igual à data visível.
- Artigos: `citation` com as leis e decisões citadas (opcional, coerente com o item 2).
- Manter `FAQPage` só na home e nas páginas de serviço; o Google encerrou esse resultado em 05/2026, mas o conteúdo em pergunta e resposta continua útil para as IAs. Não precisa expandir.

## 10. Trechos para reescrever (exemplos)

| Página | Hoje | Sugestão |
|---|---|---|
| `bpc-loas-natal/` H2 | "Qual a renda exigida" | "Qual a renda exigida para o BPC em 2026?" + 1ª frase: "A renda por pessoa da família precisa ser de até R$ 405,25 (1/4 do salário mínimo de 2026), mas a Justiça aceita renda maior quando há gastos com remédios ou tratamento." |
| `bpc-loas-natal/` | "O Supremo Tribunal Federal já reconheceu…" | Nomear a decisão (RE 567.985, 2013) com link para o STF. |
| `bpc-loas-natal/` H2 | "O que é bom saber" | "O BPC dá direito a 13º ou pensão?" (ou o assunto real do bloco). |
| Páginas de serviço, topo | Sem data | "Atualizado em 14 de novembro de 2026 · Dra. Thayná Cabral, OAB/RN 21.175". |
| Artigos, fim | "Leia também" | Antes dele, um bloco "Fontes" com 2–4 links oficiais. |

Os valores e as decisões citados aqui precisam ser conferidos pela Dra. Thayná antes de entrar no site.
