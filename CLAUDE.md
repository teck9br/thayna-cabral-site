> **Responda sempre em português do Brasil.**

# Thayná Cabral Advocacia — site

Site do escritório da Dra. Thayná Cabral (OAB/RN 21.175), Natal-RN. Objetivo: atrair clientes pelo WhatsApp e ranquear para buscas locais ("advogada previdenciária Natal", "BPC/LOAS Natal"…). Prioridade das áreas: 1º Previdenciário, 2º Trabalhista, 3º Cível. Modelo de referência: site da Antecipay (`../antecipay-claude-code`).

## Estrutura
- `site/` — o site publicável (HTML estático, sem framework).
  - `index.html` — home, **editada à mão**. É a fonte do CSS (`<style>`), do sprite de ícones SVG e do cabeçalho usados pelas outras páginas. JSON-LD: LegalService + Person (OAB) + WebSite + FAQPage (estático; ao mudar o FAQ da home, atualize o bloco `faq-ld`).
  - O rodapé da home fica entre `<!-- FOOTER -->` e `<!-- /FOOTER -->` e é **gerado** pelo `build.py`: não edite à mão.
  - `assets/fonts/` (Cormorant Garamond e Plus Jakarta Sans, woff2 variável, hospedadas no site; não usar Google Fonts), `assets/img/` (WebP + PNG/JPG), favicons, `og.jpg` (1200x630).
- `build.py` — **gerador** das páginas de serviço (`site/<slug>/index.html`), do rodapé da home, do `sitemap.xml` e da seção "Páginas" do `llms.txt`. Rode `PYTHONUTF8=1 python build.py` depois de editar `index.html` ou `build.py`. Para nova página: acrescente um `dict` em `PAGES` (slug, crumb, title, desc, eyebrow, h1, lead, wa, secoes, faq, rel). O build falha se title > 60, description fora de 120–160, mais de um H1 ou < 3 links internos. O `lastmod` do sitemap vem de `lastmod.json` (hash do `<main>` de cada página): só muda quando o conteúdo muda; versione esse arquivo.
- Fontes com `font-display:block` + preload (inclusive a itálica): com `swap` o texto aparecia em Georgia/Arial e trocava na frente do usuário. Não voltar para `swap`.
- Animações (no estilo da colinatech.com.br): `site/assets/js/fx.js` (sem biblioteca) faz os elementos surgirem ao rolar e dá sombra ao cabeçalho; o CSS fica no fim do `<style>` da home. A lista de seletores existe em dois lugares (`RV` no fx.js e `.js :is(...)` no CSS): mude os dois juntos. Os elementos começam ocultos só com a classe `.js` no `<html>`, posta por um script no `<head>`; se o fx.js não carregar em 2,5 s, a classe sai e tudo aparece. A faixa `.marq` (temas com links, abaixo do hero) é editada à mão na home.
- `gerar_favicon.py` — gera `favicon.ico` (16–64), `favicon-192.png`, `logo-512.png` e `apple-touch-icon.png` a partir do símbolo, com o traço engrossado para ficar legível em 16/32px (o traço original é fino demais e some na aba). Ao regerar, suba o `?v=` dos links de favicon na home, na privacidade e no `build.py`.
- `Thayna Cabral Advocacia*.dc.html`, `support.js`, `image-slot.js` — arquivos do design original (ferramenta de design). Não são publicados.

## Deploy
- GitHub: `github.com/teck9br/thayna-cabral-site` (público), branch `main`. Cada push publica o site no Render (static site configurado por `render.yaml`, pasta `site/`).
- Render: static site `thayna-cabral-site` (Blueprint "Thaynacabral"), endereço provisório `https://thayna-cabral-site.onrender.com` (no ar desde 23/10/2026).
- DNS no Registro.br (modo avançado, ativo desde 23/10/2026; domínio no ar com HTTPS, `www` e `http` redirecionam para `https://thaynacabraladvocacia.com.br`): `A @ 216.24.57.1`, `CNAME www → thayna-cabral-site.onrender.com` e `TXT @ google-site-verification=HrPEgTZx_IGTNxAe20ctzdMsP6YPwVJAE9x7Yb5ywx0` (Search Console, propriedade de domínio). O Render emite o SSL sozinho depois do Verify.
- Fluxo: editar → `PYTHONUTF8=1 python build.py` → commit → push → (após ~1 min) `PYTHONUTF8=1 python indexnow.py aposentadoria-natal/` com as páginas alteradas, ou sem argumentos para o sitemap inteiro. A chave fica em `site/f4ac0f0384f532e08a1b1117c2c64527.txt`.

## Dados (usar sempre iguais)
- Dra. Thayná Cabral · OAB/RN 21.175 · WhatsApp (84) 99701-0660 (`5584997010660`)
- Natal-RN; atendimento presencial com hora marcada e online em todo o Brasil.
- Domínio: `https://thaynacabraladvocacia.com.br` (registrado no Registro.br em 23/10/2026; constante `BASE` no `build.py` + home, robots, sitemap, llms.txt, privacidade).
- **Sem e-mail no site** (decisão de 23/10/2026): o domínio não tem caixa de e-mail (sem MX). Quando criar `contato@thaynacabraladvocacia.com.br`, preencha `EMAIL` no `build.py` (o rodapé volta a mostrar) e recoloque em `email` no JSON-LD da home, na privacidade e no llms.txt. Endereço completo ainda não informado.

## Regras de conteúdo
- Publicidade da advocacia: Provimento 205/2021 do CFOAB. Conteúdo informativo; não prometer resultado, não usar depoimentos de clientes, não usar "especialista" sem título, evitar autoelogio e linguagem de venda.
- Linguagem simples, sem juridiquês. Fatos jurídicos conferidos e datados (as regras de transição mudam todo ano: revisar a tabela em `aposentadoria-natal` em janeiro).
- Microsoft Clarity: o evento `whatsapp_click` já é disparado em todo `[data-wa]`; falta instalar o script com o ID próprio do site.

## Pendências
- Criar o e-mail do domínio; informar endereço; criar Google Meu Negócio; perfis sociais.
- Search Console: sitemap enviado em 26/10/2026 e indexação pedida para home, previdenciária, BPC, aposentadoria, trabalhista, danos morais e nome negativado (limite de ~10 pedidos por dia).
- Páginas (26/10/2026): 5 do Previdenciário, 6 do Trabalhista e 7 do Cível (danos morais e nome negativado entraram pelas sugestões do Ubersuggest), cada área com página-mãe (`AREAS` em `build.py`). A Dra. Thayná ainda precisa revisar os fatos jurídicos antes de publicar.
- Próximas ideias: blog com artigos (como o da Antecipay), páginas por cidade do RN (Parnamirim, Mossoró, São Gonçalo do Amarante).
