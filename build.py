# Gerador das páginas internas do site Thayná Cabral Advocacia.
# Uso (Windows): PYTHONUTF8=1 python build.py
# Lê de site/index.html o CSS, os ícones (sprite SVG) e o cabeçalho, gera as páginas de
# serviço em site/<slug>/index.html e atualiza o rodapé da home, o sitemap.xml e o llms.txt.
import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent / 'site'
BASE = 'https://thaynacabraladvocacia.com.br'  # domínio provisório: trocar aqui quando confirmar
HOJE = date.today().isoformat()
WA_NUM = '5584997010660'
WA_LABEL = '(84) 99701-0660'
EMAIL = ''  # sem e-mail por enquanto (domínio sem MX); preencher quando a caixa existir
OAB = 'OAB/RN 21.175'

INDEX = (ROOT / 'index.html').read_text(encoding='utf-8')
CSS = re.search(r'<style>\n(.*?)</style>', INDEX, re.S).group(1)
SPRITE = re.search(r'<svg width="0".*?\n</svg>', INDEX, re.S).group(0)
HEADER = re.search(r'<header class="hdr">.*?</header>', INDEX, re.S).group(0)
HEADER = re.sub(r'(<a\b[^>]*?\shref=")#', r'\1/#', HEADER)  # só links; os <use href="#i-..."> ficam


def wa(msg):
    from urllib.parse import quote
    return f'https://wa.me/{WA_NUM}?text=' + quote(msg)


def slugify(t):
    import unicodedata
    t = unicodedata.normalize('NFKD', re.sub('<[^>]+>', '', t)).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


def ico(name):
    return f'<svg class="ico" aria-hidden="true"><use href="#i-{name}"/></svg>'


# ---------------------------------------------------------------- conteúdo
# Cada página: slug, title (≤ 60), desc (120–160), h1, eyebrow, lead, wa (mensagem),
# secoes [(h2, html)], faq [(pergunta, resposta)], rel (slugs relacionados), crumb.

PAGES = [
    dict(
        slug='advogada-previdenciaria-natal',
        crumb='Direito Previdenciário',
        title='Advogada Previdenciária em Natal-RN | Thayná Cabral',
        desc='Advogada previdenciária em Natal-RN: aposentadoria, BPC/LOAS, auxílio-doença, revisão e recursos contra o INSS. Atendimento presencial e online.',
        eyebrow='Direito Previdenciário · Natal-RN',
        h1='Advogada previdenciária em Natal para orientar o seu caso com o <em>INSS</em>.',
        lead='Pedidos de aposentadoria, BPC/LOAS, auxílio-doença, revisões e recursos contra benefícios negados. Atendimento no escritório em Natal ou online, com explicação clara de cada etapa.',
        wa='Olá, Dra. Thayná! Preciso de orientação sobre um benefício do INSS.',
        secoes=[
            ('Quando procurar uma advogada previdenciária', '''
<p>Muita gente só procura ajuda depois de um benefício negado, mas o melhor momento costuma ser <strong>antes do pedido</strong>. Um erro no cadastro do INSS, um período de trabalho que não aparece no CNIS ou um documento que faltou pode atrasar a concessão por meses ou reduzir o valor do benefício para sempre.</p>
<p>Vale buscar orientação quando:</p>
<ul>
<li>você está perto de se aposentar e não sabe qual regra é mais vantajosa;</li>
<li>o INSS negou o seu pedido ou cortou um benefício;</li>
<li>há períodos de trabalho rural, em condições especiais ou sem carteira assinada;</li>
<li>alguém da família é idoso ou tem deficiência e vive com renda baixa;</li>
<li>o valor da sua aposentadoria parece menor do que deveria.</li>
</ul>'''),
            ('O que fazemos no Direito Previdenciário', '''
<div class="links">
<a href="/aposentadoria-natal/"><strong>Aposentadoria</strong><span>Por idade, tempo de contribuição, especial, rural e da pessoa com deficiência.</span></a>
<a href="/bpc-loas-natal/"><strong>BPC/LOAS</strong><span>Benefício de um salário mínimo para idosos e pessoas com deficiência de baixa renda.</span></a>
<a href="/auxilio-doenca-negado/"><strong>Auxílio-doença negado</strong><span>Recurso e ação judicial quando a perícia do INSS nega ou corta o benefício.</span></a>
<a href="/revisao-beneficio-inss/"><strong>Revisão de benefício</strong><span>Correção de erros no cálculo de aposentadorias e pensões já concedidas.</span></a>
</div>
<p>Também atuamos em pensão por morte, aposentadoria por incapacidade permanente (antiga aposentadoria por invalidez), salário-maternidade, auxílio-acidente e planejamento previdenciário.</p>'''),
            ('Como funciona o caminho até o benefício', '''
<ol class="steps-l">
<li><strong>Análise dos documentos.</strong> Conferimos o CNIS, as carteiras de trabalho e os laudos para descobrir o que você já tem de direito e o que falta provar.</li>
<li><strong>Pedido administrativo.</strong> O requerimento é feito no INSS (pelo Meu INSS) com toda a documentação organizada, o que reduz o risco de negativa.</li>
<li><strong>Recurso.</strong> Se o INSS negar, é possível recorrer ao Conselho de Recursos da Previdência Social (CRPS), em regra no prazo de 30 dias.</li>
<li><strong>Ação judicial.</strong> Quando a via administrativa não resolve, o caso vai à Justiça Federal. No Rio Grande do Norte, os processos tramitam na Justiça Federal do RN (TRF da 5ª Região), com Juizados Especiais Federais em Natal para causas de até 60 salários mínimos.</li>
</ol>'''),
            ('Atendimento em Natal e em todo o Brasil', '''
<p>O escritório fica em Natal-RN e atende com hora marcada. Como o processo previdenciário é todo eletrônico, também atendemos por videochamada clientes do interior do estado e de outras regiões do país, com o mesmo acompanhamento.</p>'''),
        ],
        faq=[
            ('Preciso de advogado previdenciário para pedir um benefício no INSS?', 'Não é obrigatório: o pedido pode ser feito pelo próprio segurado no Meu INSS. A orientação de uma advogada ajuda a escolher a regra certa, reunir as provas e evitar negativas e valores menores, que depois só se corrigem com recurso ou ação.'),
            ('Quanto custa uma advogada previdenciária?', 'Os honorários são combinados na primeira conversa, em contrato escrito, de acordo com a tabela da OAB/RN e o tipo de caso. Você sabe exatamente quanto e como vai pagar antes de começar.'),
            ('O INSS negou meu pedido. O que fazer?', 'Leia o motivo na carta de indeferimento ou no Meu INSS. Dependendo do caso, cabe recurso ao CRPS em até 30 dias, um novo pedido com documentos complementares ou uma ação na Justiça Federal.'),
            ('Vocês atendem quem mora fora de Natal?', 'Sim. O processo previdenciário é eletrônico, e o atendimento pode ser feito por videochamada, com envio de documentos pelo WhatsApp.'),
        ],
        rel=['aposentadoria-natal', 'bpc-loas-natal', 'auxilio-doenca-negado', 'revisao-beneficio-inss'],
    ),
    dict(
        slug='aposentadoria-natal',
        crumb='Aposentadoria',
        title='Advogada de Aposentadoria em Natal-RN | Thayná Cabral',
        desc='Aposentadoria por idade, tempo de contribuição, especial, rural e PcD em Natal-RN. Regras de transição de 2026, planejamento e pedido no INSS.',
        eyebrow='Aposentadoria · Natal-RN',
        h1='Aposentadoria pelo INSS com a regra mais <em>vantajosa</em> para você.',
        lead='Depois da Reforma da Previdência, existem várias regras de aposentadoria, e cada uma resulta em um valor diferente. Analisamos o seu histórico para pedir o benefício no momento certo e pela regra mais vantajosa para o seu histórico.',
        wa='Olá, Dra. Thayná! Quero saber se já posso me aposentar.',
        secoes=[
            ('Tipos de aposentadoria', '''
<ul>
<li><strong>Aposentadoria por idade (urbana):</strong> 62 anos para mulheres e 65 para homens. Tempo mínimo de contribuição: 15 anos para mulheres; para homens, 15 anos se já contribuíam antes da Reforma (13/11/2019) e 20 anos se começaram depois.</li>
<li><strong>Aposentadoria rural:</strong> 55 anos para mulheres e 60 para homens, com 15 anos de atividade rural comprovada, inclusive em regime de economia familiar. É muito comum no interior do Rio Grande do Norte.</li>
<li><strong>Aposentadoria especial:</strong> para quem trabalhou exposto a agentes nocivos à saúde (ruído, produtos químicos, agentes biológicos), comprovados por PPP e laudos.</li>
<li><strong>Aposentadoria da pessoa com deficiência:</strong> prevista na Lei Complementar 142/2013, com tempo de contribuição reduzido conforme o grau da deficiência, ou por idade (55 anos para mulheres e 60 para homens, com 15 anos de contribuição e deficiência comprovada durante igual período).</li>
<li><strong>Regras de transição:</strong> para quem já contribuía antes da Reforma, como as regras de pontos, de idade mínima progressiva e de pedágio.</li>
</ul>'''),
            ('Regras de transição em 2026', '''
<p>Quem já contribuía antes de 13/11/2019 pode usar regras de transição, que costumam ser mais vantajosas. Em 2026:</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Tabela: regras de transição em 2026"><table>
<thead><tr><th>Regra</th><th>Mulheres</th><th>Homens</th></tr></thead>
<tbody>
<tr><td>Pontos (idade + tempo de contribuição)</td><td>93 pontos e 30 anos de contribuição</td><td>103 pontos e 35 anos de contribuição</td></tr>
<tr><td>Idade mínima progressiva</td><td>59 anos e 6 meses e 30 anos de contribuição</td><td>64 anos e 6 meses e 35 anos de contribuição</td></tr>
<tr><td>Pedágio de 100%</td><td>57 anos, 30 anos de contribuição e o dobro do tempo que faltava em 2019</td><td>60 anos, 35 anos de contribuição e o dobro do tempo que faltava em 2019</td></tr>
</tbody></table></div>
<p>As exigências de pontos e de idade sobem a cada ano. Por isso, adiar ou antecipar o pedido em alguns meses pode mudar a regra aplicável e o valor do benefício.</p>'''),
            ('Planejamento previdenciário', '''
<p>O planejamento é uma análise completa do seu histórico (CNIS, carteiras, carnês e PPP) que mostra <strong>quando</strong> você pode se aposentar, <strong>por qual regra</strong> e <strong>com qual valor estimado</strong>. Ele também aponta períodos que faltam no cadastro do INSS, como trabalho rural, tempo especial ou vínculos sem registro, que podem ser comprovados antes do pedido.</p>'''),
            ('Documentos para dar entrada', '''
<ul>
<li>Documento de identidade e CPF;</li>
<li>comprovante de residência;</li>
<li>todas as carteiras de trabalho e carnês de contribuição;</li>
<li>extrato do CNIS, que pode ser baixado no Meu INSS;</li>
<li>para atividade especial: PPP e laudos técnicos (LTCAT);</li>
<li>para atividade rural: documentos que mostrem o trabalho no campo, como declaração do sindicato, notas de produção e cadastro de imóvel rural.</li>
</ul>'''),
        ],
        faq=[
            ('Qual a idade para se aposentar em 2026?', 'Na regra geral, 62 anos para mulheres e 65 para homens. Quem já contribuía antes da Reforma de 2019 pode se aposentar antes por uma regra de transição: em 2026, a idade mínima progressiva é de 59 anos e 6 meses para mulheres e 64 anos e 6 meses para homens, com 30 anos de contribuição (mulheres) ou 35 (homens).'),
            ('Trabalhei na roça sem carteira assinada. Esse tempo conta?', 'Sim. O trabalho rural, inclusive em regime de economia familiar, pode ser reconhecido com documentos da época e testemunhas, e conta para a aposentadoria rural ou somado ao tempo urbano na aposentadoria híbrida.'),
            ('Quanto tempo o INSS leva para analisar a aposentadoria?', 'O prazo varia conforme a agência e o tipo de benefício. Um pedido bem documentado tende a ser analisado mais rápido e corre menos risco de exigências e negativas.'),
            ('Posso continuar trabalhando depois de aposentado?', 'Na maioria das aposentadorias, sim. A exceção é a aposentadoria especial: quem a recebe não pode continuar exercendo atividade exposta a agentes nocivos.'),
        ],
        rel=['advogada-previdenciaria-natal', 'revisao-beneficio-inss', 'bpc-loas-natal'],
    ),
    dict(
        slug='bpc-loas-natal',
        crumb='BPC/LOAS',
        title='BPC/LOAS em Natal-RN: Quem Tem Direito | Thayná Cabral',
        desc='Quem tem direito ao BPC/LOAS, como pedir, renda exigida e o que fazer se o INSS negar. Advogada em Natal-RN para idosos e pessoas com deficiência.',
        eyebrow='BPC/LOAS · Natal-RN',
        h1='BPC/LOAS: um salário mínimo por mês para quem mais <em>precisa.</em>',
        lead='O Benefício de Prestação Continuada garante um salário mínimo mensal a idosos e pessoas com deficiência de baixa renda, mesmo sem nunca ter contribuído para o INSS. Ajudamos no pedido e no recurso quando o benefício é negado.',
        wa='Olá, Dra. Thayná! Quero saber se tenho direito ao BPC/LOAS.',
        secoes=[
            ('Quem tem direito ao BPC/LOAS', '''
<ul>
<li><strong>Idosos</strong> a partir de 65 anos;</li>
<li><strong>pessoas com deficiência</strong> de qualquer idade, inclusive crianças, com impedimento de longo prazo (pelo menos 2 anos) de natureza física, mental, intelectual ou sensorial;</li>
<li>que vivam em família de <strong>baixa renda</strong>;</li>
<li>que estejam inscritas no <strong>CadÚnico</strong>, com o cadastro atualizado.</li>
</ul>
<p>Não é preciso ter contribuído para o INSS. O BPC está previsto na Lei Orgânica da Assistência Social (Lei 8.742/1993, por isso o nome LOAS).</p>'''),
            ('Como pedir o BPC/LOAS', '''
<ol class="steps-l">
<li><strong>Inscreva ou atualize o CadÚnico</strong> no CRAS mais perto de casa. As informações de renda e de quem mora na casa precisam bater com as do pedido.</li>
<li><strong>Faça o pedido no INSS</strong> pelo Meu INSS (site ou aplicativo) ou pelo telefone 135, escolhendo o Benefício Assistencial à Pessoa Idosa ou à Pessoa com Deficiência.</li>
<li><strong>Separe os documentos:</strong> identidade, CPF e comprovante de residência e, para a pessoa com deficiência, laudos e relatórios médicos com o CID e a duração do impedimento.</li>
<li><strong>Acompanhe a perícia médica e a avaliação social</strong>, no caso da pessoa com deficiência, e responda às exigências do INSS dentro do prazo.</li>
</ol>
<p>A Lei 15.077/2024 tornou obrigatório o <strong>cadastro biométrico</strong> (como o da CNH, do título de eleitor ou da Carteira de Identidade Nacional) para pedir e para manter o benefício.</p>'''),
            ('Qual a renda exigida', '''
<p>O critério geral é renda familiar <strong>por pessoa de até 1/4 do salário mínimo</strong>. Para calcular, soma-se a renda de quem mora na mesma casa (requerente, cônjuge, pais, irmãos solteiros, filhos e enteados solteiros) e divide-se pelo número de pessoas.</p>
<p>Esse limite não é absoluto. O Supremo Tribunal Federal já reconheceu que a situação de vulnerabilidade pode ser provada por outros meios, e a Justiça analisa a realidade da família: gastos com remédios, fraldas, tratamentos e condições da moradia.</p>'''),
            ('Por que o INSS nega o BPC', '''
<ul>
<li>renda por pessoa acima de 1/4 do salário mínimo no cálculo do INSS;</li>
<li>CadÚnico desatualizado ou com informações diferentes das do pedido;</li>
<li>perícia médica ou avaliação social que não reconheceu a deficiência;</li>
<li>falta de documentos médicos que mostrem a duração do impedimento.</li>
</ul>
<p>Em muitos desses casos, a negativa pode ser revertida com recurso administrativo ou ação na Justiça Federal, com laudos e uma avaliação social que mostrem a realidade da família.</p>'''),
            ('O que é bom saber', '''
<ul>
<li>O BPC não é aposentadoria: não paga 13º salário e não deixa pensão por morte.</li>
<li>O benefício é revisto periodicamente, e o CadÚnico precisa ser mantido atualizado.</li>
<li>A pessoa com deficiência que começa a trabalhar pode ter o BPC suspenso e voltar a recebê-lo se perder o emprego.</li>
</ul>'''),
        ],
        faq=[
            ('Quem recebe Bolsa Família pode receber BPC?', 'Receber Bolsa Família não impede o pedido. Desde junho de 2025 (Decreto 12.534/2025), o INSS passou a somar o Bolsa Família na renda da família; a regra é questionada na Justiça, e há decisões que a afastam. O cadastro no CadÚnico precisa estar correto e atualizado.'),
            ('Criança com autismo tem direito ao BPC?', 'Pode ter. O transtorno do espectro autista é considerado deficiência para todos os efeitos legais. Se a família tiver baixa renda e o impedimento for de longo prazo, a criança pode receber o BPC.'),
            ('O BPC foi negado por renda. Ainda tenho chance?', 'Sim, em muitos casos. A Justiça analisa a situação concreta da família, como gastos com saúde e condições de moradia, e não apenas o limite de 1/4 do salário mínimo.'),
            ('Quanto tempo demora o BPC?', 'Depende da fila do INSS, da perícia e da avaliação social. Um pedido com CadÚnico em dia e laudos completos tende a andar mais rápido.'),
        ],
        rel=['advogada-previdenciaria-natal', 'auxilio-doenca-negado', 'aposentadoria-natal'],
    ),
    dict(
        slug='auxilio-doenca-negado',
        crumb='Auxílio-doença negado',
        title='Auxílio-Doença Negado: O Que Fazer | Advogada em Natal',
        desc='Auxílio-doença negado ou cortado pelo INSS? Veja os motivos mais comuns, o prazo do recurso e quando entrar na Justiça. Advogada em Natal-RN.',
        eyebrow='Auxílio-doença · Natal-RN',
        h1='Auxílio-doença negado: o que fazer <em>agora.</em>',
        lead='A negativa do INSS não é o fim. Dependendo do motivo, é possível pedir de novo, recorrer ou entrar na Justiça Federal com uma nova perícia. Explicamos o caminho mais rápido para o seu caso.',
        wa='Olá, Dra. Thayná! Meu auxílio-doença foi negado/cortado e preciso de orientação.',
        secoes=[
            ('O que é o auxílio-doença hoje', '''
<p>Desde a Reforma da Previdência, o auxílio-doença se chama <strong>auxílio por incapacidade temporária</strong>. Ele é pago ao segurado que fica incapaz para o trabalho por mais de 15 dias por doença ou acidente. Os requisitos são:</p>
<ul>
<li><strong>qualidade de segurado:</strong> estar contribuindo ou dentro do período de graça;</li>
<li><strong>carência de 12 contribuições</strong>, que não é exigida em caso de acidente de qualquer natureza nem para doenças graves previstas em lei, como câncer, cardiopatia grave e doença de Parkinson;</li>
<li><strong>incapacidade comprovada</strong> por perícia médica ou por análise de documentos médicos.</li>
</ul>'''),
            ('Motivos mais comuns da negativa', '''
<ul>
<li><strong>"Não constatação de incapacidade":</strong> o perito do INSS entendeu que você pode trabalhar. É o motivo mais frequente;</li>
<li><strong>falta de carência</strong> ou <strong>perda da qualidade de segurado</strong>, muitas vezes por erro do INSS no cadastro de contribuições;</li>
<li><strong>doença anterior à filiação</strong> ao INSS;</li>
<li><strong>documentos médicos incompletos</strong>, sem CID, data de início da doença ou descrição das limitações.</li>
</ul>'''),
            ('Os caminhos depois da negativa', '''
<ol class="steps-l">
<li><strong>Novo pedido</strong>, com laudos e exames mais completos, quando o problema foi a documentação.</li>
<li><strong>Recurso ao CRPS</strong>, em regra no prazo de 30 dias da ciência da decisão, pelo Meu INSS.</li>
<li><strong>Ação na Justiça Federal</strong>, em que um perito nomeado pelo juiz faz uma nova avaliação. No RN, causas de até 60 salários mínimos tramitam nos Juizados Especiais Federais, sem custas na primeira instância.</li>
</ol>
<p>Se o benefício foi <strong>cortado</strong> (cessado), atenção ao <strong>pedido de prorrogação</strong>, que deve ser feito nos 15 dias anteriores à data de cessação. Se o prazo passou, ainda cabem recurso e ação judicial.</p>
<p>Quando a doença ou o acidente tem relação com o trabalho, o benefício é acidentário: a ação corre na Justiça Estadual e pode haver reflexos trabalhistas, como estabilidade de 12 meses após o retorno.</p>'''),
            ('Como se preparar para a perícia', '''
<ul>
<li>Leve laudos recentes com CID, data de início da doença, tratamento e <strong>limitações para o trabalho</strong>;</li>
<li>reúna exames, receitas e relatórios de internação;</li>
<li>explique ao perito quais tarefas da sua função você não consegue fazer.</li>
</ul>'''),
        ],
        faq=[
            ('Qual o prazo para recorrer do auxílio-doença negado?', 'Em regra, 30 dias a partir da ciência da decisão, pelo Meu INSS. Depois desse prazo, ainda é possível fazer um novo pedido ou entrar com ação na Justiça Federal.'),
            ('Vale mais a pena recorrer ou entrar na Justiça?', 'Depende do motivo da negativa e da urgência. Na Justiça, a perícia é feita por um médico nomeado pelo juiz, e é possível pedir os valores atrasados desde a negativa. Analisamos o caso para indicar o caminho mais rápido.'),
            ('Recebo os valores atrasados se ganhar na Justiça?', 'Sim. Reconhecido o direito, o INSS paga os valores desde a data do pedido ou da cessação indevida, com correção. Causas de até 60 salários mínimos costumam ser pagas por RPV.'),
            ('Posso trabalhar enquanto espero o resultado?', 'Quem recebe auxílio-doença não pode trabalhar na atividade para a qual está incapaz. Se o benefício foi negado e você voltou ao trabalho por necessidade, isso precisa ser explicado no processo.'),
        ],
        rel=['advogada-previdenciaria-natal', 'bpc-loas-natal', 'revisao-beneficio-inss'],
    ),
    dict(
        slug='revisao-beneficio-inss',
        crumb='Revisão de benefício',
        title='Revisão de Aposentadoria e Benefício do INSS | Natal-RN',
        desc='Revisão de aposentadoria e pensão do INSS: erros de cálculo, tempo especial ou rural ignorado e salários errados. Prazo de 10 anos. Advogada em Natal-RN.',
        eyebrow='Revisão de benefício · Natal-RN',
        h1='Revisão de aposentadoria: quando o INSS <em>calculou errado.</em>',
        lead='Erros no cadastro e no cálculo do INSS são comuns e podem reduzir o seu benefício por toda a vida. A revisão corrige o valor e permite cobrar as diferenças dos últimos 5 anos.',
        wa='Olá, Dra. Thayná! Quero saber se minha aposentadoria pode ser revisada.',
        secoes=[
            ('Quando a revisão é possível', '''
<ul>
<li><strong>Vínculos ou salários que não aparecem no CNIS</strong> e ficaram fora do cálculo;</li>
<li><strong>tempo especial não reconhecido</strong>, como trabalho exposto a ruído, agentes químicos ou biológicos;</li>
<li><strong>tempo rural ignorado</strong>, inclusive o trabalho em regime de economia familiar na juventude;</li>
<li><strong>atividades concomitantes</strong> (dois empregos ao mesmo tempo) calculadas de forma errada;</li>
<li><strong>tempo de serviço militar, de aluno-aprendiz ou de trabalho no exterior</strong> não contado;</li>
<li><strong>regra de aposentadoria menos vantajosa</strong> aplicada quando havia outra que pagava mais.</li>
</ul>'''),
            ('Prazo para pedir a revisão', '''
<p>O prazo para revisar o ato de concessão é de <strong>10 anos</strong>, contados do mês seguinte ao do primeiro pagamento (art. 103 da Lei 8.213/1991). Passado esse prazo, o direito à revisão se perde.</p>
<p>As diferenças atrasadas são pagas, em regra, dos <strong>últimos 5 anos</strong> antes do pedido. Por isso, quanto antes a revisão for feita, maior o valor recuperado.</p>'''),
            ('E a revisão da vida toda?', '''
<p>A chamada revisão da vida toda, que permitia incluir os salários anteriores a julho de 1994 no cálculo, <strong>foi afastada pelo Supremo Tribunal Federal em 2024</strong>. Hoje essa revisão não é mais possível. Existem outras revisões possíveis, que dependem da análise do seu processo de concessão.</p>'''),
            ('Como analisamos o seu benefício', '''
<ol class="steps-l">
<li>Pedimos a cópia do processo administrativo e a carta de concessão, que mostra como o INSS fez o cálculo.</li>
<li>Comparamos o cálculo com o seu CNIS, as carteiras de trabalho e os documentos de tempo especial ou rural.</li>
<li>Se houver diferença, explicamos quanto o benefício pode aumentar e qual o caminho: pedido de revisão no INSS ou ação na Justiça Federal.</li>
</ol>'''),
        ],
        faq=[
            ('Pedir revisão pode diminuir minha aposentadoria?', 'Em situações específicas, sim, por isso a análise prévia é essencial. Antes de qualquer pedido, conferimos se a revisão é vantajosa.'),
            ('Pensão por morte também pode ser revisada?', 'Sim. A pensão é calculada a partir do benefício do falecido. Se houve erro nesse cálculo, ou na aposentadoria que deu origem à pensão, é possível revisar dentro do prazo de 10 anos.'),
            ('Quanto tempo demora uma revisão?', 'No INSS, depende da fila de análise. Na Justiça Federal, o tempo varia conforme a complexidade do caso. Você acompanha cada etapa com informações claras.'),
            ('Preciso guardar documentos antigos?', 'Sim. Carteiras de trabalho, carnês, contracheques e PPP são as principais provas para corrigir o cálculo. Se você não tiver algum documento, há outros meios de prova a avaliar.'),
        ],
        rel=['advogada-previdenciaria-natal', 'aposentadoria-natal', 'auxilio-doenca-negado'],
    ),

    # ------------------------------------------------------------ Trabalhista
    dict(
        area='trab',
        slug='advogada-trabalhista-natal',
        crumb='Direito Trabalhista',
        title='Advogada Trabalhista em Natal-RN | Thayná Cabral',
        desc='Advogada trabalhista em Natal-RN: verbas rescisórias, rescisão indireta, horas extras, vínculo sem carteira e acidente de trabalho. Presencial e online.',
        eyebrow='Direito Trabalhista · Natal-RN',
        h1='Advogada trabalhista em Natal para defender os direitos de quem <em>trabalha.</em>',
        lead='Verbas rescisórias não pagas, horas extras, trabalho sem carteira, rescisão indireta e acidente de trabalho. Analisamos o seu caso e explicamos, com clareza, o que pode ser cobrado da empresa.',
        wa='Olá, Dra. Thayná! Preciso de orientação sobre uma questão trabalhista.',
        secoes=[
            ('Quando procurar uma advogada trabalhista', '''
<p>O momento mais comum é logo depois da saída da empresa, mas muitas situações pedem orientação <strong>ainda durante o contrato</strong>, quando é possível reunir provas com mais facilidade. Vale buscar ajuda quando:</p>
<ul>
<li>a empresa não pagou a rescisão no prazo ou pagou valores menores;</li>
<li>você trabalha além da jornada e não recebe horas extras;</li>
<li>trabalhou ou trabalha sem carteira assinada;</li>
<li>a empresa atrasa salários, não deposita o FGTS ou trata você com abuso;</li>
<li>sofreu acidente ou adoeceu por causa do trabalho.</li>
</ul>'''),
            ('O que fazemos no Direito Trabalhista', '''
<div class="links">
<a href="/verbas-rescisorias/"><strong>Verbas rescisórias</strong><span>Rescisão não paga, paga com atraso ou calculada errado.</span></a>
<a href="/rescisao-indireta/"><strong>Rescisão indireta</strong><span>Quando a falta grave é da empresa e o trabalhador pode sair com todos os direitos.</span></a>
<a href="/horas-extras/"><strong>Horas extras</strong><span>Jornada além do limite, intervalo não concedido e banco de horas irregular.</span></a>
<a href="/trabalho-sem-carteira-assinada/"><strong>Trabalho sem carteira</strong><span>Reconhecimento do vínculo e dos direitos de todo o período.</span></a>
<a href="/acidente-de-trabalho/"><strong>Acidente de trabalho</strong><span>Estabilidade, benefício do INSS e indenização contra a empresa.</span></a>
</div>'''),
            ('Prazo para entrar com a ação', '''
<p>O trabalhador tem até <strong>2 anos após o fim do contrato</strong> para entrar com a ação, e pode cobrar os direitos dos <strong>últimos 5 anos</strong>, contados da data em que a ação é proposta (art. 7º, XXIX, da Constituição). Cada mês de espera pode representar um mês de direitos perdidos.</p>'''),
            ('Advogada trabalhista online', '''
<p>O processo trabalhista é eletrônico, então o atendimento pode ser feito <strong>online</strong>, por videochamada, com envio de documentos pelo WhatsApp. As audiências podem ser presenciais ou por videoconferência, conforme a vara.</p>
<p>Isso permite atender trabalhadores do interior do Rio Grande do Norte e de outros estados. A ação costuma ser proposta no local onde o trabalho foi prestado (art. 651 da CLT), e avaliamos cada caso antes de começar.</p>'''),
            ('Como funciona o processo', '''
<ol class="steps-l">
<li><strong>Análise do caso.</strong> Conferimos contrato, carteira de trabalho, contracheques, extrato do FGTS, termo de rescisão e as provas que você tem, como mensagens e testemunhas.</li>
<li><strong>Tentativa de acordo</strong>, quando faz sentido, antes ou durante o processo.</li>
<li><strong>Ação na Justiça do Trabalho.</strong> Em Natal, as ações tramitam nas Varas do Trabalho do TRT da 21ª Região, em processo eletrônico. Muitos casos terminam em acordo nas primeiras audiências.</li>
</ol>'''),
        ],
        faq=[
            ('Posso entrar com ação trabalhista ainda trabalhando na empresa?', 'Pode. A lei não proíbe, mas é preciso avaliar o momento e os riscos. Em alguns casos, como atraso de salários ou falta de depósito do FGTS, o caminho pode ser a rescisão indireta.'),
            ('Quanto custa uma ação trabalhista?', 'Os honorários são combinados na primeira conversa, em contrato escrito, de acordo com a tabela da OAB/RN. Quem não pode pagar as custas do processo pode pedir a justiça gratuita.'),
            ('Preciso ter testemunhas?', 'Nem sempre. Documentos, mensagens, e-mails, fotos e registros de ponto também são provas. Quando o caso depende de testemunha, colegas de trabalho e ex-colegas podem depor.'),
            ('A empresa pode me prejudicar por eu entrar na Justiça?', 'Retaliação por exercer o direito de ação é ilegal e pode gerar indenização. Se você ainda trabalha na empresa, avaliamos juntos a melhor estratégia.'),
        ],
        rel=['verbas-rescisorias', 'rescisao-indireta', 'horas-extras', 'trabalho-sem-carteira-assinada', 'acidente-de-trabalho'],
    ),
    dict(
        area='trab',
        slug='verbas-rescisorias',
        crumb='Verbas rescisórias',
        title='Verbas Rescisórias Não Pagas: O Que Fazer | Natal-RN',
        desc='Rescisão não paga ou paga errado? Veja o que você deve receber em cada tipo de demissão, o prazo de 10 dias e as multas. Advogada trabalhista em Natal-RN.',
        eyebrow='Verbas rescisórias · Natal-RN',
        h1='Verbas rescisórias: o que a empresa precisa <em>pagar</em> na sua saída.',
        lead='A empresa tem 10 dias, contados do fim do contrato, para pagar a rescisão. Se não pagou, atrasou ou calculou errado, é possível cobrar a diferença e as multas na Justiça do Trabalho.',
        wa='Olá, Dra. Thayná! A empresa não pagou (ou pagou errado) minha rescisão.',
        secoes=[
            ('O que você recebe em cada tipo de saída', '''
<div class="table-wrap" tabindex="0" role="region" aria-label="Tabela: verbas por tipo de saída"><table>
<thead><tr><th>Tipo de saída</th><th>Verbas</th></tr></thead>
<tbody>
<tr><td>Demissão sem justa causa</td><td>Saldo de salário, aviso prévio, 13º proporcional, férias vencidas e proporcionais com 1/3, saque do FGTS com multa de 40% e seguro-desemprego.</td></tr>
<tr><td>Pedido de demissão</td><td>Saldo de salário, 13º proporcional, férias vencidas e proporcionais com 1/3. Sem multa do FGTS, sem saque e sem seguro-desemprego.</td></tr>
<tr><td>Acordo (art. 484-A da CLT)</td><td>Metade do aviso prévio indenizado, multa de 20% do FGTS, saque de até 80% do FGTS e as demais verbas integrais. Sem seguro-desemprego.</td></tr>
<tr><td>Justa causa</td><td>Saldo de salário e férias vencidas com 1/3.</td></tr>
</tbody></table></div>
<p>O <strong>aviso prévio</strong> é de 30 dias, com mais 3 dias por ano completo de trabalho, até o limite de 90 dias (Lei 12.506/2011).</p>'''),
            ('Prazo de pagamento e multas', '''
<p>As verbas rescisórias devem ser pagas em até <strong>10 dias</strong> contados do fim do contrato (art. 477, § 6º, da CLT). Se a empresa atrasar, deve pagar uma <strong>multa de um salário</strong> do trabalhador (art. 477, § 8º).</p>
<p>Se o caso chegar à Justiça e a empresa não pagar, na primeira audiência, as verbas que ela mesma reconhece como devidas, esses valores são acrescidos de <strong>50%</strong> (art. 467 da CLT).</p>'''),
            ('Erros comuns na rescisão', '''
<ul>
<li>horas extras, adicionais e comissões que não entraram na média das férias e do 13º;</li>
<li>FGTS com depósitos faltando ao longo do contrato, o que reduz também a multa de 40%;</li>
<li>aviso prévio sem os dias proporcionais ao tempo de casa;</li>
<li>justa causa aplicada sem motivo grave ou sem provas;</li>
<li>pedido de demissão "forçado", quando na verdade a saída foi decisão da empresa.</li>
</ul>
<p>Confira o seu extrato do FGTS no aplicativo da Caixa: depósitos faltando são um dos problemas mais frequentes.</p>'''),
            ('Justa causa injusta', '''
<p>A justa causa só pode ser aplicada nas hipóteses do art. 482 da CLT e precisa de prova, proporcionalidade e aplicação imediata. Se for revertida na Justiça, o trabalhador recebe tudo o que receberia numa demissão sem justa causa, e, conforme o caso, indenização por danos morais.</p>'''),
        ],
        faq=[
            ('A empresa disse que vai pagar a rescisão parcelada. Pode?', 'A lei exige o pagamento em até 10 dias após o fim do contrato. O parcelamento só é válido se for acordado e homologado, por exemplo, em acordo judicial. Fora disso, o atraso gera a multa do art. 477.'),
            ('Assinei o termo de rescisão. Ainda posso cobrar diferenças?', 'Sim. Assinar o termo comprova o que foi pago, mas não impede cobrar na Justiça as verbas que ficaram de fora ou foram calculadas errado, dentro do prazo de 2 anos.'),
            ('Quanto tempo tenho para cobrar a rescisão?', 'Até 2 anos após o fim do contrato, podendo cobrar direitos dos últimos 5 anos contados da data da ação.'),
            ('Fui demitido por justa causa. Tenho direito ao seguro-desemprego?', 'Não, enquanto a justa causa valer. Se ela for revertida na Justiça, o trabalhador passa a ter direito às verbas da demissão sem justa causa, inclusive a indenização correspondente ao seguro-desemprego, quando cabível.'),
        ],
        rel=['advogada-trabalhista-natal', 'rescisao-indireta', 'horas-extras'],
    ),
    dict(
        area='trab',
        slug='rescisao-indireta',
        crumb='Rescisão indireta',
        title='Rescisão Indireta: Quando Pedir e Direitos | Natal-RN',
        desc='Rescisão indireta é a "justa causa do patrão": salário atrasado, FGTS não depositado, assédio. Veja quando cabe e o que você recebe. Advogada em Natal-RN.',
        eyebrow='Rescisão indireta · Natal-RN',
        h1='Rescisão indireta: quando a falta grave é da <em>empresa.</em>',
        lead='Se a empresa descumpre obrigações sérias, o trabalhador pode encerrar o contrato e receber tudo o que receberia se fosse demitido sem justa causa. Mas o caminho exige cuidado: um passo errado pode virar pedido de demissão.',
        wa='Olá, Dra. Thayná! Acho que meu caso pode ser de rescisão indireta.',
        secoes=[
            ('Quando cabe a rescisão indireta', '''
<p>As hipóteses estão no art. 483 da CLT. As mais comuns na prática são:</p>
<ul>
<li><strong>atraso frequente de salários</strong> ou pagamento "por fora";</li>
<li><strong>falta de depósito do FGTS</strong> ou de recolhimento do INSS;</li>
<li><strong>assédio moral ou sexual</strong>, humilhações e tratamento com rigor excessivo;</li>
<li>exigência de serviços superiores às forças do trabalhador, proibidos por lei ou alheios ao contrato;</li>
<li>exposição a <strong>perigo manifesto</strong>, como falta de equipamentos de proteção;</li>
<li>redução do trabalho de forma a reduzir muito o salário de quem ganha por produção.</li>
</ul>'''),
            ('Direitos na rescisão indireta', '''
<p>Reconhecida a rescisão indireta, o trabalhador recebe as mesmas verbas da <a href="/verbas-rescisorias/">demissão sem justa causa</a>: saldo de salário, aviso prévio proporcional, 13º e férias proporcionais com 1/3, saque do FGTS com multa de 40% e as guias do seguro-desemprego. Também podem ser cobradas as dívidas que motivaram a saída, como salários e FGTS atrasados, e, em casos de assédio, indenização por danos morais.</p>'''),
            ('Como fazer da forma certa', '''
<ol class="steps-l">
<li><strong>Reúna provas</strong> antes de qualquer passo: extrato do FGTS, contracheques, mensagens, áudios, e-mails e nomes de testemunhas.</li>
<li><strong>Busque orientação antes de sair.</strong> Em alguns casos, como atraso de salário e falta de FGTS, a lei permite continuar trabalhando enquanto o processo corre (art. 483, § 3º). Em outros, o afastamento precisa ser bem documentado.</li>
<li><strong>Entre com a ação</strong> na Justiça do Trabalho pedindo o reconhecimento da rescisão indireta e o pagamento das verbas.</li>
</ol>
<p><strong>Atenção:</strong> simplesmente parar de ir ao trabalho, sem orientação, pode ser interpretado como abandono de emprego ou pedido de demissão.</p>'''),
        ],
        faq=[
            ('O que acontece se a Justiça não reconhecer a rescisão indireta?', 'Em regra, a saída passa a ser tratada como pedido de demissão, e o trabalhador perde verbas como a multa de 40% e o seguro-desemprego. Por isso, a análise das provas antes de agir é tão importante.'),
            ('Preciso pedir demissão para entrar com rescisão indireta?', 'Não. Pedir demissão é justamente o que deve ser evitado. A rescisão indireta é pedida na Justiça, com ou sem afastamento do trabalho, conforme o caso.'),
            ('FGTS atrasado é motivo para rescisão indireta?', 'A falta de depósito do FGTS é uma das hipóteses mais aceitas pela Justiça do Trabalho como descumprimento grave do contrato. O extrato da Caixa é a principal prova.'),
            ('Posso continuar trabalhando enquanto o processo corre?', 'Nos casos de descumprimento das obrigações do contrato, como salário atrasado e FGTS não depositado, sim (art. 483, § 3º, da CLT). Em situações de assédio ou perigo, o afastamento costuma ser necessário.'),
        ],
        rel=['advogada-trabalhista-natal', 'verbas-rescisorias', 'horas-extras'],
    ),
    dict(
        area='trab',
        slug='horas-extras',
        crumb='Horas extras',
        title='Horas Extras Não Pagas: Como Cobrar | Advogada Natal',
        desc='Trabalha além da jornada e não recebe? Veja como cobrar horas extras, intervalo não concedido e reflexos no FGTS, férias e 13º. Advogada em Natal-RN.',
        eyebrow='Horas extras · Natal-RN',
        h1='Horas extras não pagas: como cobrar o tempo que você <em>trabalhou.</em>',
        lead='Chegar antes, sair depois, almoçar em 20 minutos ou responder mensagens fora do expediente pode gerar horas extras. Elas valem pelo menos 50% a mais e refletem no FGTS, nas férias e no 13º.',
        wa='Olá, Dra. Thayná! Trabalho (ou trabalhei) além do horário e não recebi horas extras.',
        secoes=[
            ('O que conta como hora extra', '''
<p>A jornada normal é de até <strong>8 horas por dia e 44 por semana</strong> (art. 7º, XIII, da Constituição), salvo regras específicas da categoria. O tempo além disso é hora extra e deve ser pago com adicional de, no mínimo, <strong>50%</strong>. O trabalho em domingos e feriados sem folga compensatória é pago em dobro.</p>
<p>Situações comuns:</p>
<ul>
<li>chegar antes do horário ou sair depois, com o ponto "britânico" (sempre igual);</li>
<li>intervalo de almoço menor que 1 hora em jornadas acima de 6 horas;</li>
<li>trabalho por mensagens, ligações e e-mails fora do expediente, quando exigido;</li>
<li>banco de horas sem acordo válido ou com horas que nunca foram compensadas;</li>
<li>cursos e reuniões obrigatórios fora do horário.</li>
</ul>'''),
            ('Intervalo de almoço não concedido', '''
<p>Quem trabalha mais de 6 horas tem direito a intervalo de pelo menos 1 hora. Se a empresa concede menos, deve pagar o <strong>tempo suprimido com adicional de 50%</strong> (art. 71, § 4º, da CLT). Também há o intervalo de 11 horas entre o fim de uma jornada e o início da outra.</p>'''),
            ('Reflexos: por que o valor cresce', '''
<p>Horas extras habituais entram no cálculo de outras verbas: <strong>descanso semanal remunerado, férias com 1/3, 13º salário, FGTS com multa de 40% e aviso prévio</strong>. Por isso, cobrar horas extras de 5 anos costuma representar um valor bem maior do que a soma das horas.</p>'''),
            ('Como provar as horas extras', '''
<ul>
<li><strong>Cartões de ponto:</strong> empresas com mais de 20 empregados são obrigadas a controlar a jornada (art. 74, § 2º, da CLT). Se a empresa não apresentar os registros, a jornada informada pelo trabalhador pode prevalecer;</li>
<li><strong>mensagens e e-mails</strong> com horário, registros de acesso a sistemas e fotos;</li>
<li><strong>testemunhas</strong>, como colegas que trabalhavam no mesmo horário.</li>
</ul>
<p>Cargos de gestão com poder de mando e gratificação de pelo menos 40%, e trabalho externo sem possibilidade de controle, podem estar fora do controle de jornada (art. 62 da CLT). Cada caso precisa ser analisado.</p>'''),
        ],
        faq=[
            ('Quanto vale a hora extra?', 'O valor da hora normal acrescido de, no mínimo, 50%. Convenções coletivas podem prever percentuais maiores. Domingos e feriados trabalhados sem folga compensatória são pagos em dobro.'),
            ('Meu ponto era sempre igual. Isso ajuda?', 'Sim. Registros de ponto com horários idênticos todos os dias (ponto britânico) costumam ser desconsiderados pela Justiça do Trabalho, e a jornada pode ser provada por testemunhas e outros meios.'),
            ('Cargo de confiança recebe hora extra?', 'Depende. Só fica fora do controle de jornada quem tem poder real de gestão e recebe gratificação de pelo menos 40% do salário. Ter o título de gerente, sem esses requisitos, não basta.'),
            ('Posso cobrar horas extras de quanto tempo?', 'Dos últimos 5 anos, contados da data da ação, desde que a ação seja proposta em até 2 anos após o fim do contrato.'),
        ],
        rel=['advogada-trabalhista-natal', 'verbas-rescisorias', 'trabalho-sem-carteira-assinada'],
    ),
    dict(
        area='trab',
        slug='trabalho-sem-carteira-assinada',
        crumb='Trabalho sem carteira',
        title='Trabalho Sem Carteira Assinada: Seus Direitos | Natal',
        desc='Trabalhou sem carteira assinada? Veja como provar o vínculo e cobrar FGTS, férias, 13º e INSS de todo o período. Advogada trabalhista em Natal-RN.',
        eyebrow='Vínculo de emprego · Natal-RN',
        h1='Trabalhou sem carteira assinada? Os seus direitos <em>continuam valendo.</em>',
        lead='Quando existe relação de emprego, a falta de registro não tira os direitos do trabalhador. É possível pedir o reconhecimento do vínculo e cobrar tudo o que deixou de ser pago, inclusive o tempo para a aposentadoria.',
        wa='Olá, Dra. Thayná! Trabalhei (ou trabalho) sem carteira assinada.',
        secoes=[
            ('Quando existe vínculo de emprego', '''
<p>Pela CLT (arts. 2º e 3º), há relação de emprego quando o trabalho reúne:</p>
<ul>
<li><strong>pessoalidade:</strong> é você quem trabalha, sem poder mandar outra pessoa no seu lugar;</li>
<li><strong>habitualidade:</strong> o trabalho é contínuo, não eventual;</li>
<li><strong>subordinação:</strong> você segue ordens, horários e regras da empresa;</li>
<li><strong>salário:</strong> o trabalho é pago.</li>
</ul>
<p>O nome dado ao contrato não importa. "Freelancer fixo", "prestador de serviço" ou MEI contratado como PJ podem ser, na prática, empregados (a chamada pejotização).</p>'''),
            ('O que pode ser cobrado', '''
<ul>
<li>anotação da carteira de trabalho com as datas e o salário reais;</li>
<li>FGTS de todo o período, com multa de 40% se a saída foi sem justa causa;</li>
<li>13º salário e férias com 1/3;</li>
<li>aviso prévio e demais <a href="/verbas-rescisorias/">verbas rescisórias</a>;</li>
<li>horas extras e adicionais, se houver;</li>
<li>recolhimento do INSS, que passa a contar para a <a href="/aposentadoria-natal/">aposentadoria</a> e garante cobertura de benefícios.</li>
</ul>'''),
            ('Empregada doméstica e diarista', '''
<p>Quem trabalha em casa de família <strong>mais de 2 dias por semana</strong> para o mesmo empregador é empregado doméstico e tem direito à carteira assinada, FGTS, férias, 13º e controle de jornada (Lei Complementar 150/2015). Até 2 dias por semana, em regra, é diarista, sem vínculo.</p>'''),
            ('Como provar o vínculo', '''
<ul>
<li>mensagens de WhatsApp com ordens, escalas e cobranças;</li>
<li>comprovantes de pagamento, PIX e transferências regulares;</li>
<li>fotos com uniforme, crachá, e-mails corporativos e registros em sistemas;</li>
<li>testemunhas, como colegas, clientes e fornecedores.</li>
</ul>'''),
        ],
        faq=[
            ('Trabalhei como MEI, mas cumpria horário e recebia ordens. Tenho direitos?', 'Pode ter. Se estavam presentes pessoalidade, habitualidade, subordinação e salário, a Justiça pode reconhecer o vínculo de emprego mesmo com contrato de prestação de serviços ou CNPJ.'),
            ('Qual o prazo para pedir o reconhecimento do vínculo?', 'A cobrança das verbas deve ser feita em até 2 anos após o fim do trabalho, alcançando os últimos 5 anos. Já o pedido de anotação na carteira para fins previdenciários não prescreve (art. 11, §1º, da CLT).'),
            ('O tempo sem carteira conta para a aposentadoria?', 'Sim, quando o vínculo é reconhecido e as contribuições ficam registradas. Esse é um ponto que costuma ser esquecido e pode antecipar a aposentadoria.'),
            ('Ainda trabalho sem registro. Posso pedir a carteira assinada?', 'Sim. O registro é obrigação do empregador desde o primeiro dia. Avaliamos com você se é o caso de conversar, notificar ou entrar com ação.'),
        ],
        rel=['advogada-trabalhista-natal', 'verbas-rescisorias', 'aposentadoria-natal'],
    ),
    dict(
        area='trab',
        slug='acidente-de-trabalho',
        crumb='Acidente de trabalho',
        title='Acidente de Trabalho: Direitos e Indenização | Natal-RN',
        desc='Sofreu acidente de trabalho ou doença ocupacional? Veja CAT, estabilidade de 12 meses, benefício do INSS e indenização da empresa. Advogada em Natal-RN.',
        eyebrow='Acidente de trabalho · Natal-RN',
        h1='Acidente de trabalho: estabilidade, benefício e <em>indenização.</em>',
        lead='Quem sofre acidente ou adoece por causa do trabalho tem proteção dupla: benefícios do INSS e direitos contra a empresa, como estabilidade no emprego e indenização por danos.',
        wa='Olá, Dra. Thayná! Sofri um acidente de trabalho (ou doença ocupacional) e preciso de orientação.',
        secoes=[
            ('O que é acidente de trabalho', '''
<ul>
<li><strong>acidente típico:</strong> ocorre durante o trabalho, como quedas, cortes e lesões com máquinas;</li>
<li><strong>doença ocupacional:</strong> causada ou agravada pelo trabalho, como LER/DORT, problemas de coluna, perda auditiva e transtornos psicológicos ligados ao ambiente de trabalho;</li>
<li><strong>acidente a serviço da empresa</strong> fora do local de trabalho, como em viagens e entregas.</li>
</ul>
<p>A empresa deve emitir a <strong>CAT</strong> (Comunicação de Acidente de Trabalho). Se não emitir, o próprio trabalhador, o sindicato, o médico ou um familiar podem fazer isso.</p>'''),
            ('Direitos junto ao INSS', '''
<ul>
<li><strong>auxílio por incapacidade temporária acidentário</strong> (o antigo auxílio-doença acidentário) a partir do 16º dia de afastamento, sem exigência de carência;</li>
<li><strong>auxílio-acidente</strong>, de 50% do salário de benefício, se ficar sequela que reduza a capacidade para o trabalho, pago mesmo depois da volta ao emprego;</li>
<li><strong>aposentadoria por incapacidade permanente</strong>, se não houver possibilidade de reabilitação.</li>
</ul>
<p>Se o INSS negar ou cortar o benefício, veja o que fazer em <a href="/auxilio-doenca-negado/">auxílio-doença negado</a>.</p>'''),
            ('Direitos contra a empresa', '''
<ul>
<li><strong>estabilidade de 12 meses</strong> após o fim do auxílio acidentário (art. 118 da Lei 8.213/1991): a empresa não pode demitir sem justa causa nesse período;</li>
<li><strong>depósito do FGTS</strong> durante todo o afastamento por acidente;</li>
<li><strong>indenização por danos morais, materiais e estéticos</strong>, quando a empresa teve culpa (falta de equipamento de proteção, treinamento ou fiscalização) ou quando a atividade é de risco;</li>
<li><strong>pensão mensal</strong> proporcional à perda da capacidade de trabalho, em casos de sequela permanente.</li>
</ul>'''),
            ('O que fazer depois do acidente', '''
<ol class="steps-l">
<li>Procure atendimento médico e guarde todos os laudos, exames e atestados.</li>
<li>Peça a emissão da CAT e guarde uma cópia.</li>
<li>Anote nomes de testemunhas e fotografe o local e as condições de trabalho.</li>
<li>Busque orientação para garantir o benefício correto no INSS e avaliar a indenização.</li>
</ol>'''),
        ],
        faq=[
            ('Fui demitido logo depois de voltar do afastamento. Pode?', 'Se você recebeu auxílio acidentário, tem estabilidade de 12 meses após o retorno. A demissão sem justa causa nesse período pode gerar reintegração ou indenização do período restante.'),
            ('A empresa não emitiu a CAT. E agora?', 'A CAT pode ser emitida pelo próprio trabalhador, por familiar, sindicato, médico ou autoridade pública, inclusive pela internet. A falta da CAT não impede o reconhecimento do acidente.'),
            ('Doença psicológica pode ser acidente de trabalho?', 'Pode. Depressão, ansiedade e síndrome de burnout ligadas às condições de trabalho podem ser reconhecidas como doença ocupacional, com os mesmos direitos.'),
            ('Qual o prazo para pedir indenização?', 'A ação contra a empresa segue o prazo trabalhista: 5 anos contados da ciência inequívoca da incapacidade, respeitado o limite de 2 anos após o fim do contrato.'),
        ],
        rel=['advogada-trabalhista-natal', 'auxilio-doenca-negado', 'verbas-rescisorias'],
    ),

    # ------------------------------------------------------------ Cível
    dict(
        area='civ',
        slug='advogada-civel-natal',
        crumb='Direito Cível',
        title='Advogada Cível e de Família em Natal-RN | Thayná Cabral',
        desc='Advogada cível em Natal-RN: direito do consumidor, indenizações, divórcio, pensão alimentícia e inventário. Atendimento presencial e online.',
        eyebrow='Direito Cível e Família · Natal-RN',
        h1='Advogada cível em Natal para proteger você, a sua família e o seu <em>patrimônio.</em>',
        lead='Problemas com empresas e bancos, indenizações, divórcio, pensão alimentícia e inventário. Orientação clara para resolver, sempre que possível, de forma rápida e com menos desgaste.',
        wa='Olá, Dra. Thayná! Preciso de orientação sobre uma questão cível ou de família.',
        secoes=[
            ('O que fazemos no Direito Cível', '''
<div class="links">
<a href="/direito-do-consumidor-natal/"><strong>Direito do consumidor</strong><span>Nome negativado, cobrança indevida, plano de saúde, voos e compras.</span></a>
<a href="/divorcio-natal/"><strong>Divórcio</strong><span>Em cartório ou na Justiça, com partilha de bens, guarda e pensão.</span></a>
<a href="/pensao-alimenticia-natal/"><strong>Pensão alimentícia</strong><span>Pedido, revisão e cobrança de pensão atrasada.</span></a>
<a href="/inventario-natal/"><strong>Inventário</strong><span>Partilha de bens em cartório ou judicial, com prazos e impostos.</span></a>
<a href="/indenizacao-danos-morais-natal/"><strong>Danos morais</strong><span>Indenização por ofensas, falhas de serviço e acidentes.</span></a>
<a href="/nome-negativado-indevidamente/"><strong>Nome negativado</strong><span>Retirada do nome do Serasa e SPC e indenização.</span></a>
</div>
<p>Também atuamos em indenizações por danos materiais, contratos, ações de cobrança, guarda e regulamentação de convivência.</p>'''),
            ('Resolver no cartório ou na Justiça', '''
<p>Muitas questões de família podem ser resolvidas <strong>em cartório</strong>, de forma mais rápida, quando há acordo entre as partes, como divórcio consensual e inventário. Quando não há acordo, ou a lei exige, o caminho é a Justiça, nas Varas de Família e Cíveis da Comarca de Natal ou nos Juizados Especiais Cíveis para causas de menor valor.</p>'''),
            ('Como funciona o atendimento', '''
<ol class="steps-l">
<li><strong>Conversa inicial</strong> para entender a situação e os documentos que você já tem.</li>
<li><strong>Caminhos possíveis</strong>, com vantagens, prazos e custos de cada um, incluindo a tentativa de acordo.</li>
<li><strong>Contrato de honorários por escrito</strong> e acompanhamento de cada etapa.</li>
</ol>'''),
        ],
        faq=[
            ('Preciso de advogado no Juizado Especial Cível?', 'Em causas de até 20 salários mínimos, não é obrigatório na primeira instância. Entre 20 e 40 salários mínimos, e para recorrer, é obrigatório. Mesmo nas causas menores, a orientação ajuda a pedir corretamente e a provar o dano.'),
            ('Divórcio e inventário podem ser feitos em cartório?', 'Sim, quando há acordo e são cumpridos os requisitos da lei. O cartório exige a presença de advogado, e o procedimento costuma ser bem mais rápido do que o judicial.'),
            ('Quanto custa?', 'Os honorários são combinados na primeira conversa, em contrato escrito, de acordo com a tabela da OAB/RN e a complexidade do caso.'),
            ('Atendem fora de Natal?', 'Sim. Processos judiciais são eletrônicos e muitos atos de cartório podem ser feitos de forma digital, o que permite atender clientes de outras cidades.'),
        ],
        rel=['direito-do-consumidor-natal', 'divorcio-natal', 'pensao-alimenticia-natal', 'inventario-natal'],
    ),
    dict(
        area='civ',
        slug='direito-do-consumidor-natal',
        crumb='Direito do consumidor',
        title='Advogada de Direito do Consumidor em Natal-RN',
        desc='Nome negativado indevidamente, cobrança indevida, plano de saúde que negou cobertura ou voo cancelado? Veja seus direitos. Advogada em Natal-RN.',
        eyebrow='Direito do consumidor · Natal-RN',
        h1='Problemas com empresas e bancos? Conheça os seus direitos de <em>consumidor.</em>',
        lead='Negativação indevida, cobranças que você não reconhece, plano de saúde que nega tratamento e voos cancelados. O Código de Defesa do Consumidor prevê a devolução de valores e, conforme o caso, indenização.',
        wa='Olá, Dra. Thayná! Tenho um problema com uma empresa e preciso de orientação.',
        secoes=[
            ('Situações mais comuns', '''
<ul>
<li><strong><a href="/nome-negativado-indevidamente/">Nome negativado indevidamente</a></strong> no Serasa ou SPC por dívida já paga ou que não existe: segundo o STJ, o dano moral é presumido;</li>
<li><strong>cobrança indevida paga:</strong> o consumidor tem direito à devolução em dobro do que pagou a mais, com correção (art. 42, parágrafo único, do CDC), salvo engano justificável;</li>
<li><strong>descontos não autorizados</strong> em conta, cartão ou benefício do INSS, como empréstimos e seguros que você não contratou;</li>
<li><strong>plano de saúde</strong> que nega cirurgia, exame, medicamento ou internação indicada pelo médico;</li>
<li><strong>voo cancelado ou atrasado</strong>, extravio de bagagem e overbooking;</li>
<li><strong>produto com defeito</strong> não resolvido em 30 dias, e compras on-line não entregues.</li>
</ul>'''),
            ('Descontos indevidos no benefício do INSS', '''
<p>Aposentados e pensionistas são alvo frequente de empréstimos consignados e mensalidades de associações que nunca autorizaram. É possível pedir o cancelamento, a devolução dos valores descontados e, conforme o caso, indenização. Confira o extrato do benefício no Meu INSS.</p>'''),
            ('Prazos e onde reclamar', '''
<ul>
<li>Antes da Justiça, uma reclamação no <strong>consumidor.gov.br</strong> ou no <strong>Procon</strong> pode resolver e serve como prova;</li>
<li>o prazo para pedir indenização por danos causados por produto ou serviço é de <strong>5 anos</strong> (art. 27 do CDC);</li>
<li>causas de até 40 salários mínimos podem tramitar no <strong>Juizado Especial Cível</strong>, sem custas na primeira instância.</li>
</ul>'''),
            ('Provas que ajudam', '''
<ul>
<li>prints de cobranças, faturas, extratos e da consulta ao Serasa ou SPC;</li>
<li>protocolos de atendimento, e-mails e conversas com a empresa;</li>
<li>notas fiscais, contratos e comprovantes de pagamento;</li>
<li>no caso de plano de saúde, a negativa por escrito e o pedido médico.</li>
</ul>'''),
        ],
        faq=[
            ('Meu nome foi negativado por uma dívida que já paguei. Tenho direito a indenização?', 'Em regra, sim. A negativação indevida gera dano moral presumido, segundo o STJ. Uma exceção é quando a pessoa já tinha outras negativações legítimas na mesma época.'),
            ('Paguei uma cobrança indevida. Recebo em dobro?', 'O CDC garante a devolução em dobro do valor pago indevidamente, com correção e juros, salvo engano justificável da empresa.'),
            ('Voo atrasado dá direito a indenização?', 'Depende das circunstâncias. A companhia deve dar assistência (comunicação, alimentação e hospedagem conforme o tempo de espera). A indenização por dano moral depende de prejuízos concretos, como perder um compromisso ou passar a noite no aeroporto.'),
            ('O plano de saúde negou meu tratamento. O que fazer?', 'Peça a negativa por escrito e o relatório médico. Em casos urgentes, é possível pedir uma decisão liminar na Justiça para garantir o tratamento rapidamente.'),
        ],
        rel=['advogada-civel-natal', 'revisao-beneficio-inss', 'inventario-natal'],
    ),
    dict(
        area='civ',
        slug='indenizacao-danos-morais-natal',
        crumb='Danos morais',
        title='Indenização por Danos Morais em Natal-RN | Thayná Cabral',
        desc='Quando cabe indenização por danos morais, como provar, qual o prazo e onde pedir. Advogada em Natal-RN com atendimento presencial e online.',
        eyebrow='Danos morais · Natal-RN',
        h1='Indenização por danos morais: quando o prejuízo vai além do <em>dinheiro.</em>',
        lead='Ofensas, negativação indevida, falhas graves de serviço e acidentes podem gerar o dever de indenizar. Explicamos se o seu caso tem fundamento, quais provas reunir e qual o caminho mais adequado.',
        wa='Olá, Dra. Thayná! Quero saber se o meu caso dá direito a indenização por danos morais.',
        secoes=[
            ('O que é dano moral', '''
<p>Dano moral é a ofensa a direitos ligados à pessoa, como a <strong>honra, a imagem, a intimidade e a integridade física e psíquica</strong>. Quem causa esse dano por ação, omissão ou negligência tem o dever de indenizar (arts. 186 e 927 do Código Civil e art. 5º, V e X, da Constituição).</p>
<p>Nem todo aborrecimento gera indenização. A Justiça analisa a gravidade do fato, a repercussão na vida da pessoa e as provas apresentadas.</p>'''),
            ('Situações que costumam gerar indenização', '''
<ul>
<li><a href="/nome-negativado-indevidamente/">nome negativado indevidamente</a> no Serasa ou SPC;</li>
<li>descontos não autorizados em conta ou no benefício do INSS;</li>
<li>ofensas e exposição em redes sociais e grupos de WhatsApp;</li>
<li>acidentes de trânsito com lesão;</li>
<li>falha grave de serviço, como <a href="/direito-do-consumidor-natal/">plano de saúde</a> que nega tratamento urgente;</li>
<li>erro médico e falhas no atendimento de saúde;</li>
<li><a href="/acidente-de-trabalho/">acidente ou doença causada pelo trabalho</a>, que é julgado pela Justiça do Trabalho.</li>
</ul>'''),
            ('Danos morais, materiais e estéticos', '''
<p>O <strong>dano material</strong> é o prejuízo financeiro comprovado: o que você gastou ou perdeu (danos emergentes) e o que deixou de ganhar (lucros cessantes). O <strong>dano moral</strong> é o sofrimento causado pelo fato. Quando há marca ou deformidade permanente, pode haver também <strong>dano estético</strong>. Os três podem ser pedidos na mesma ação.</p>'''),
            ('Prazo para pedir', '''
<ul>
<li><strong>3 anos</strong> é a regra geral para a reparação civil (art. 206, §3º, V, do Código Civil);</li>
<li><strong>5 anos</strong> quando o dano vem de produto ou serviço, numa relação de consumo (art. 27 do CDC);</li>
<li>na Justiça do Trabalho, <strong>2 anos</strong> após o fim do contrato.</li>
</ul>
<p>Em regra, o prazo conta a partir do momento em que a pessoa soube do dano e de quem o causou.</p>'''),
            ('Provas que ajudam', '''
<ul>
<li>prints com data, link e nome do autor; para conteúdo que pode ser apagado, a <strong>ata notarial</strong> em cartório dá mais segurança;</li>
<li>boletim de ocorrência, laudos, receitas e atestados médicos;</li>
<li>protocolos de atendimento, e-mails e conversas com a empresa;</li>
<li>contato de testemunhas que presenciaram o fato.</li>
</ul>'''),
        ],
        faq=[
            ('Qual o valor da indenização por danos morais?', 'Não existe tabela. O juiz considera a gravidade do fato, a repercussão, a situação das partes e decisões em casos parecidos. Por isso não é possível saber o valor antes da sentença.'),
            ('Preciso de advogado para pedir danos morais?', 'No Juizado Especial Cível, em causas de até 20 salários mínimos, não é obrigatório na primeira instância. Entre 20 e 40 salários mínimos, e para recorrer, é obrigatório. Acima disso, a ação vai para a Justiça comum.'),
            ('Ofensa em grupo de WhatsApp dá direito a indenização?', 'Pode dar, conforme o conteúdo e o alcance da ofensa. Guarde prints que mostrem o autor, a data e o grupo. Também pode haver crime contra a honra, e nesse caso o prazo para a queixa-crime é de 6 meses a partir do dia em que você soube quem é o autor.'),
            ('Quanto tempo demora um processo de danos morais?', 'Depende do caso e de onde ele tramita. No Juizado Especial costuma ser mais rápido, e muitos processos terminam em acordo já na audiência de conciliação.'),
        ],
        rel=['nome-negativado-indevidamente', 'direito-do-consumidor-natal', 'advogada-civel-natal'],
    ),
    dict(
        area='civ',
        slug='nome-negativado-indevidamente',
        crumb='Nome negativado',
        title='Nome Negativado Indevidamente: O Que Fazer | Natal-RN',
        desc='Nome no Serasa ou SPC por dívida paga, que não é sua ou sem aviso? Veja como limpar o nome e quando cabe indenização. Advogada em Natal-RN.',
        eyebrow='Direito do consumidor · Natal-RN',
        h1='Nome negativado indevidamente: como limpar o nome e quando cabe <em>indenização.</em>',
        lead='Dívida já paga, conta que você não abriu, cobrança de valor errado ou negativação sem aviso. Nesses casos, é possível pedir a retirada do nome dos cadastros e, conforme o caso, indenização.',
        wa='Olá, Dra. Thayná! Meu nome foi negativado indevidamente e preciso de orientação.',
        secoes=[
            ('Quando a negativação é indevida', '''
<ul>
<li><strong>dívida já paga:</strong> depois do pagamento, o credor tem <strong>5 dias úteis</strong> para pedir a retirada do nome (Súmula 548 do STJ);</li>
<li><strong>dívida que não é sua:</strong> contas, cartões ou empréstimos abertos por terceiros com os seus dados;</li>
<li><strong>valor errado</strong> ou dívida que está sendo discutida;</li>
<li><strong>sem aviso prévio:</strong> você deve ser comunicado por escrito antes da inclusão (art. 43, §2º, do CDC);</li>
<li><strong>mais de 5 anos:</strong> a informação negativa não pode ficar nos cadastros por mais de 5 anos (art. 43, §1º, do CDC), mesmo que a dívida não tenha sido paga.</li>
</ul>'''),
            ('O que fazer agora', '''
<ol class="steps-l">
<li><strong>Consulte o seu CPF</strong> de graça no Serasa, no SPC, na Boa Vista e no Registrato, do Banco Central, e salve os comprovantes da consulta.</li>
<li><strong>Reúna as provas:</strong> comprovantes de pagamento, contratos, faturas e, em caso de fraude, o boletim de ocorrência.</li>
<li><strong>Reclame com a empresa</strong> e no consumidor.gov.br, e anote os protocolos.</li>
<li><strong>Se não resolver,</strong> é possível pedir na Justiça a retirada do nome com urgência (liminar) e indenização.</li>
</ol>'''),
            ('Quando cabe indenização', '''
<p>Segundo o STJ, a inscrição indevida em cadastro de inadimplentes gera <strong>dano moral presumido</strong>: não é preciso provar o constrangimento. A exceção é quando a pessoa já tinha outras negativações legítimas na mesma época (Súmula 385 do STJ). Mesmo nesse caso, é possível pedir a retirada da negativação indevida.</p>
<p>Em fraudes bancárias praticadas por terceiros, o banco responde pelos danos (Súmula 479 do STJ). Veja também a página sobre <a href="/indenizacao-danos-morais-natal/">indenização por danos morais</a>.</p>'''),
        ],
        faq=[
            ('Quanto tempo a empresa tem para tirar meu nome depois que eu pago?', 'Cinco dias úteis, contados do pagamento integral da dívida (Súmula 548 do STJ). Se o nome continuar negativado depois disso, guarde o comprovante e a consulta atualizada.'),
            ('Tenho direito a indenização se já tinha outra negativação?', 'Em regra, não, se as outras negativações eram legítimas e anteriores (Súmula 385 do STJ). Ainda assim, é possível exigir a retirada da negativação indevida.'),
            ('Descobri uma dívida de um cartão que nunca pedi. E agora?', 'Faça um boletim de ocorrência, conteste a dívida com a empresa e guarde os protocolos. A empresa responde pelos danos de fraude feita por terceiros, e a Justiça pode determinar a retirada do nome com urgência.'),
            ('Preciso pagar para consultar meu nome?', 'Não. Serasa, SPC e Boa Vista oferecem consulta gratuita do CPF, e o Registrato, do Banco Central, mostra gratuitamente empréstimos e contas em seu nome.'),
        ],
        rel=['indenizacao-danos-morais-natal', 'direito-do-consumidor-natal', 'advogada-civel-natal'],
    ),
    dict(
        area='civ',
        slug='divorcio-natal',
        crumb='Divórcio',
        title='Advogada de Divórcio em Natal-RN | Thayná Cabral',
        desc='Divórcio em Natal-RN: consensual em cartório ou litigioso na Justiça, partilha de bens, guarda dos filhos e pensão. Advogada de família.',
        eyebrow='Divórcio · Natal-RN',
        h1='Divórcio com orientação clara e o mínimo de <em>desgaste.</em>',
        lead='O divórcio pode ser feito em cartório, quando há acordo, ou na Justiça. Explicamos cada caminho, os prazos e o que acontece com os bens, a guarda dos filhos e a pensão.',
        wa='Olá, Dra. Thayná! Preciso de orientação sobre divórcio.',
        secoes=[
            ('Divórcio em cartório ou na Justiça', '''
<p>Desde a Emenda Constitucional 66/2010, não é preciso separação prévia nem tempo mínimo de casamento para se divorciar, e não é necessário apontar culpado.</p>
<ul>
<li><strong>Divórcio extrajudicial (em cartório):</strong> quando o casal está de acordo sobre o divórcio e a partilha. É feito por escritura pública, com advogado, e costuma ser concluído rapidamente. Desde 2024, o CNJ admite o divórcio em cartório mesmo com filhos menores, desde que guarda, convivência e pensão já tenham sido resolvidas na Justiça;</li>
<li><strong>divórcio judicial consensual:</strong> quando há acordo, mas as questões dos filhos ainda precisam ser definidas pelo juiz;</li>
<li><strong>divórcio litigioso:</strong> quando não há acordo. Mesmo assim, o divórcio em si pode ser decretado logo, e as discussões sobre bens e filhos seguem no processo.</li>
</ul>'''),
            ('Partilha de bens', '''
<p>A divisão depende do <strong>regime de bens</strong>. No mais comum, a comunhão parcial (aplicada quando não há pacto antenupcial), dividem-se os bens adquiridos de forma onerosa durante o casamento. Ficam de fora, em regra, os bens anteriores ao casamento e os recebidos por herança ou doação. Na união estável, sem contrato escrito, valem as mesmas regras da comunhão parcial.</p>'''),
            ('Filhos: guarda, convivência e pensão', '''
<p>A <strong>guarda compartilhada</strong> é a regra quando ambos os pais estão aptos (Lei 13.058/2014). Ela divide as decisões sobre a vida da criança, mas não significa que a criança more metade do tempo com cada um. Também são definidos o regime de convivência e a <a href="/pensao-alimenticia-natal/">pensão alimentícia</a>.</p>'''),
            ('Documentos para o divórcio', '''
<ul>
<li>certidão de casamento atualizada e pacto antenupcial, se houver;</li>
<li>documentos pessoais dos dois e certidões de nascimento dos filhos;</li>
<li>documentos dos bens: matrículas de imóveis, documentos de veículos, extratos e contratos;</li>
<li>informações sobre renda, para a definição da pensão.</li>
</ul>'''),
        ],
        faq=[
            ('Quanto tempo demora um divórcio?', 'O divórcio em cartório, com documentos em ordem, costuma sair em poucas semanas. O judicial consensual leva alguns meses, e o litigioso depende da complexidade das discussões sobre bens e filhos.'),
            ('Meu cônjuge não quer se divorciar. Posso me divorciar mesmo assim?', 'Sim. O divórcio é um direito, e não depende da concordância do outro. Nesse caso, ele é feito na Justiça.'),
            ('Preciso de advogado para o divórcio em cartório?', 'Sim. A lei exige a presença de advogado na escritura de divórcio. Um único advogado pode atender o casal quando há acordo.'),
            ('Posso me divorciar e deixar a partilha para depois?', 'Pode. O divórcio pode ser feito antes, e a partilha dos bens resolvida depois, em cartório ou na Justiça.'),
        ],
        rel=['advogada-civel-natal', 'pensao-alimenticia-natal', 'inventario-natal'],
    ),
    dict(
        area='civ',
        slug='pensao-alimenticia-natal',
        crumb='Pensão alimentícia',
        title='Pensão Alimentícia em Natal-RN: Pedir, Revisar, Cobrar',
        desc='Como pedir, revisar ou cobrar pensão alimentícia atrasada em Natal-RN. Valor, até quando é paga e prisão por dívida de pensão. Advogada de família.',
        eyebrow='Pensão alimentícia · Natal-RN',
        h1='Pensão alimentícia: pedir, revisar e cobrar o que é <em>devido.</em>',
        lead='A pensão garante o sustento de quem não pode se manter sozinho, principalmente dos filhos. O valor depende da necessidade de quem recebe e da possibilidade de quem paga, e pode ser revisto quando a situação muda.',
        wa='Olá, Dra. Thayná! Preciso de orientação sobre pensão alimentícia.',
        secoes=[
            ('Como o valor é definido', '''
<p>Não existe percentual fixo em lei. O juiz considera o <strong>binômio necessidade e possibilidade</strong> (art. 1.694 do Código Civil): as despesas de quem recebe (alimentação, escola, saúde, moradia, lazer) e a renda de quem paga. O valor pode ser fixado em percentual do salário, quando há emprego formal, ou em valor fixo.</p>'''),
            ('Até quando a pensão é paga', '''
<ul>
<li>Para filhos, em regra, até os 18 anos, podendo se estender até os 24 anos se estiverem cursando faculdade ou curso técnico;</li>
<li>a pensão <strong>não termina automaticamente</strong> aos 18 anos: o fim depende de decisão judicial (Súmula 358 do STJ);</li>
<li>a gestante pode pedir <strong>alimentos gravídicos</strong> durante a gravidez (Lei 11.804/2008), que se convertem em pensão após o nascimento;</li>
<li>na falta ou impossibilidade dos pais, os avós podem ser chamados a complementar.</li>
</ul>'''),
            ('Revisão da pensão', '''
<p>Se a situação de quem paga ou de quem recebe mudar, como desemprego, aumento de renda, novas despesas de saúde ou escola, é possível pedir a <strong>revisão</strong> para aumentar ou diminuir o valor. Até a nova decisão, continua valendo o valor anterior: deixar de pagar por conta própria gera dívida.</p>'''),
            ('Pensão atrasada', '''
<p>A cobrança pode ser feita por dois caminhos (art. 528 do Código de Processo Civil):</p>
<ul>
<li><strong>pelo rito da prisão:</strong> para as 3 últimas parcelas vencidas antes da ação e as que vencerem durante o processo, o devedor pode ser preso por 1 a 3 meses se não pagar (Súmula 309 do STJ);</li>
<li><strong>pelo rito da penhora:</strong> para parcelas mais antigas, com bloqueio de contas, penhora de bens, desconto em salário e protesto do nome.</li>
</ul>'''),
        ],
        faq=[
            ('A pensão é sempre 30% do salário?', 'Não. Esse número é só uma referência popular. O valor é definido caso a caso, conforme a necessidade de quem recebe e a possibilidade de quem paga.'),
            ('Fiquei desempregado. Posso parar de pagar a pensão?', 'Não. É preciso pedir a revisão na Justiça. Enquanto não houver nova decisão, o valor anterior continua devido e as parcelas não pagas viram dívida.'),
            ('O pai não paga a pensão. O que posso fazer?', 'É possível cobrar na Justiça. Para as três últimas parcelas, o devedor pode ser preso se não pagar; para as anteriores, cabe penhora de bens, bloqueio de contas e desconto em salário.'),
            ('Posso pedir pensão sem estar casada com o pai?', 'Sim. O direito à pensão é do filho e não depende de casamento ou união entre os pais. Se a paternidade não estiver registrada, ela pode ser investigada no mesmo processo.'),
        ],
        rel=['advogada-civel-natal', 'divorcio-natal', 'inventario-natal'],
    ),
    dict(
        area='civ',
        slug='inventario-natal',
        crumb='Inventário',
        title='Advogada de Inventário em Natal-RN | Thayná Cabral',
        desc='Inventário em cartório ou judicial em Natal-RN: prazo de 2 meses, ITCMD, documentos e partilha entre herdeiros. Advogada para inventário e partilha.',
        eyebrow='Inventário · Natal-RN',
        h1='Inventário: a partilha dos bens com orientação sobre prazos, impostos e <em>documentos.</em>',
        lead='Quando alguém falece deixando bens, é o inventário que transfere o patrimônio aos herdeiros. Ele pode ser feito em cartório, quando há acordo, ou na Justiça. Orientamos sobre prazos, impostos e documentos.',
        wa='Olá, Dra. Thayná! Preciso de orientação sobre inventário.',
        secoes=[
            ('Inventário em cartório ou judicial', '''
<ul>
<li><strong>Inventário extrajudicial (em cartório):</strong> quando todos os herdeiros estão de acordo com a partilha. É feito por escritura pública, com advogado, e costuma ser muito mais rápido. Desde 2024, o CNJ passou a admitir o inventário em cartório também em situações antes restritas à Justiça, como a existência de herdeiros menores, com regras específicas;</li>
<li><strong>inventário judicial:</strong> obrigatório quando não há acordo entre os herdeiros e em outros casos previstos em lei.</li>
</ul>'''),
            ('Prazo e impostos', '''
<p>O inventário deve ser aberto em até <strong>2 meses</strong> a partir do falecimento (art. 611 do Código de Processo Civil). O atraso pode gerar multa sobre o ITCMD, o imposto estadual sobre heranças, cobrado no Rio Grande do Norte pela Secretaria de Estado da Tributação (SET-RN).</p>
<p>Enquanto o inventário não termina, os bens, em regra, só podem ser vendidos ou transferidos com autorização judicial (alvará), e contas bancárias e imóveis ficam indisponíveis para os herdeiros.</p>'''),
            ('Documentos necessários', '''
<ul>
<li>certidão de óbito e documentos pessoais do falecido;</li>
<li>certidão de casamento ou prova de união estável, e documentos do cônjuge ou companheiro;</li>
<li>documentos de todos os herdeiros;</li>
<li>documentos dos bens: matrículas de imóveis, documentos de veículos, extratos bancários e de investimentos;</li>
<li>certidões negativas de débitos do falecido e testamento, se houver.</li>
</ul>'''),
            ('Quem são os herdeiros', '''
<p>Pelo Código Civil, os herdeiros necessários são os <strong>descendentes</strong> (filhos, netos), os <strong>ascendentes</strong> (pais, avós) e o <strong>cônjuge</strong> (a situação do companheiro em união estável é tratada de forma semelhante pelos tribunais). Com os filhos, o cônjuge concorre conforme o regime de bens; com os pais, herda independentemente do regime. Na falta desses, herdam os irmãos, sobrinhos, tios e primos, nessa ordem.</p>'''),
        ],
        faq=[
            ('Qual o prazo para abrir o inventário?', 'Dois meses a partir do falecimento. Passado esse prazo, o inventário ainda pode ser feito, mas pode haver multa sobre o imposto de herança (ITCMD).'),
            ('Quanto tempo demora um inventário?', 'Em cartório, com documentos em ordem e imposto pago, costuma ser concluído em poucos meses ou menos. O judicial pode levar bem mais, conforme o número de bens e as divergências entre herdeiros.'),
            ('O falecido deixou só dinheiro no banco. Preciso de inventário?', 'Valores pequenos, como saldos de FGTS, PIS e restituições, podem ser liberados por alvará judicial sem inventário completo (Lei 6.858/1980). Para outros bens, o inventário é necessário.'),
            ('Um herdeiro não concorda com a partilha. E agora?', 'Sem acordo, o inventário precisa ser feito na Justiça. Ainda assim, buscamos uma solução negociada sempre que possível, para reduzir tempo e custos.'),
        ],
        rel=['advogada-civel-natal', 'divorcio-natal', 'pensao-alimenticia-natal'],
    ),
]
BY_SLUG = {p['slug']: p for p in PAGES}

AREAS = {
    'prev': dict(nome='Direito Previdenciário', curto='Previdenciário', head='advogada-previdenciaria-natal'),
    'trab': dict(nome='Direito Trabalhista', curto='Trabalhista', head='advogada-trabalhista-natal'),
    'civ': dict(nome='Direito Cível', curto='Cível e Família', head='advogada-civel-natal'),
}


def area(p):
    return AREAS[p.get('area', 'prev')]

# ---------------------------------------------------------------- partes comuns

PAGE_CSS = '''
.crumbs{max-width:1280px;margin:0 auto;padding:32px var(--pad-x) 0;font-size:13px;color:var(--soft)}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.crumbs li+li::before{content:"/";margin-right:8px;color:#CBD5E1}
.crumbs a{color:var(--muted)}
.crumbs a:hover{color:var(--gold-d)}
.phero{max-width:1280px;margin:0 auto;padding:clamp(32px,5vw,64px) var(--pad-x) clamp(48px,6vw,80px);display:flex;flex-direction:column;gap:28px}
.phero h1{margin:0;max-width:900px;font-family:var(--serif);font-weight:400;font-size:clamp(38px,4.6vw,64px);line-height:1.08;letter-spacing:-.01em;text-wrap:balance}
.phero .hero__sub{max-width:720px}
.layout{max-width:1280px;margin:0 auto;padding:0 var(--pad-x) var(--sec-y);display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:clamp(40px,5vw,80px);align-items:start}
@media (max-width:959px){.layout{grid-template-columns:minmax(0,1fr)}}
.prose{max-width:760px;font-size:16px;line-height:1.8;color:var(--text)}
.prose h2{margin:56px 0 16px;font-family:var(--serif);font-weight:500;font-size:clamp(28px,3vw,38px);line-height:1.15;color:var(--ink);text-wrap:balance}
.prose h2:first-child{margin-top:0}
.prose p{margin:0 0 16px;text-wrap:pretty}
.prose ul{margin:0 0 16px;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.prose ul li{position:relative;padding-left:24px}
.prose ul li::before{content:"";position:absolute;left:0;top:.85em;width:12px;height:1px;background:var(--gold)}
.prose strong{color:var(--ink);font-weight:600}
.prose a{color:var(--gold-d);border-bottom:1px solid rgba(197,160,89,.4)}
.steps-l{margin:0 0 16px;padding:0;list-style:none;counter-reset:s;display:flex;flex-direction:column;gap:16px}
.steps-l li{position:relative;padding-left:48px;counter-increment:s}
.steps-l li::before{content:counter(s,upper-roman);position:absolute;left:0;top:-2px;font-family:var(--serif);font-size:26px;color:var(--gold-d)}
.table-wrap{overflow-x:auto;margin:0 0 16px;border-radius:20px;border:1px solid rgba(197,160,89,.3);background:rgba(255,255,255,.6)}
.prose table{width:100%;border-collapse:collapse;font-size:14px;line-height:1.55;min-width:520px}
.prose th,.prose td{padding:14px 18px;text-align:left;vertical-align:top;border-bottom:1px solid rgba(15,23,42,.07)}
.prose th{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-d)}
.prose tr:last-child td{border-bottom:0}
.links{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:12px;margin:0 0 20px}
.prose .links a,.related a{display:flex;flex-direction:column;gap:6px;padding:22px 24px;border-radius:22px;border:var(--glass-line);background:var(--glass-bg);box-shadow:var(--glass-shadow);color:var(--ink);transition:transform .3s,background .3s}
.prose .links a:hover,.related a:hover{transform:translateY(-4px);background:rgba(255,255,255,.75);color:var(--ink)}
.prose .links strong,.related strong{font-family:var(--serif);font-size:22px;font-weight:500}
.prose .links span,.related span{font-size:14px;line-height:1.6;color:var(--muted)}
.note{margin-top:40px;padding:20px 24px;border-left:2px solid var(--gold);background:rgba(242,238,230,.5);border-radius:0 16px 16px 0;font-size:14px;line-height:1.7;color:var(--muted)}
.aside{position:sticky;top:110px;border-radius:28px;padding:28px;display:flex;flex-direction:column;gap:18px}
.aside__who{display:flex;align-items:center;gap:14px}
.aside__who img{width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:50% 25%;border:1px solid rgba(197,160,89,.6)}
.aside__who strong{display:block;font-family:var(--serif);font-size:22px;font-weight:500}
.aside__who span{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-d)}
.aside p{margin:0;font-size:14px;line-height:1.7;color:var(--muted)}
.aside .btn{justify-content:center;height:54px;padding:0 20px;font-size:13px}
.aside ul{margin:0;padding:16px 0 0;border-top:1px solid rgba(197,160,89,.25);list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--muted)}
.aside li{display:flex;gap:10px;align-items:center}
.aside li .ico{color:var(--gold-d);font-size:16px}
@media (max-width:959px){.aside{position:static}}
.related{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:16px}
'''


def footer():
    cols = ''
    for k, ar in AREAS.items():
        links = ''.join(f'<a href="/{p["slug"]}/">{"Visão geral" if p["slug"] == ar["head"] else p["crumb"]}</a>'
                        for p in PAGES if p.get('area', 'prev') == k)
        cols += f'''
      <nav class="ftr__col" aria-label="{ar['nome']}">
        <span>{ar['curto']}</span>
        {links}
      </nav>'''
    w = wa('Olá, Dra. Thayná! Gostaria de agendar uma consulta.')
    return f'''<!-- FOOTER (gerado por build.py) -->
<footer class="ftr">
  <div class="wrap">
    <div class="ftr__grid">
      <div class="ftr__col">
        <img src="/assets/img/logotipo-light.webp" alt="Thayná Cabral Advocacia" width="190" height="106" loading="lazy" style="width:190px;height:auto">
        <p>Advogada em Natal-RN. Direito Previdenciário, Trabalhista e Cível com atendimento presencial e online.</p>
        <div class="ftr__line">{ico('pin')}Natal, Rio Grande do Norte<br>Presencial com hora marcada e online</div>
        <a data-wa href="{html.escape(w)}" target="_blank" rel="noopener">{ico('wa')}{WA_LABEL}</a>
        {f'<a href="mailto:{EMAIL}">{ico("mail")}{EMAIL}</a>' if EMAIL else ''}
      </div>{cols}
      <nav class="ftr__col" aria-label="Rodapé">
        <span>Escritório</span>
        <a href="/#sobre">Sobre a advogada</a>
        <a href="/#areas">Áreas de atuação</a>
        <a href="/#duvidas">Perguntas frequentes</a>
        <a href="https://antecipayprecatorios.com.br/equipe/thayna-cabral/" target="_blank" rel="noopener">Artigos sobre precatórios</a>
      </nav>
    </div>
    <div class="ftr__legal">
      <span>Thayná Cabral · {OAB} · Conteúdo meramente informativo, em conformidade com o Provimento nº 205/2021 do CFOAB.</span>
      <div>
        <a href="/privacidade.html">Política de Privacidade</a>
        <span>© 2026 Thayná Cabral Advocacia</span>
      </div>
    </div>
  </div>
</footer>
<!-- /FOOTER -->'''


def faq_html(faq):
    out = []
    for q, a in faq:
        out.append(f'''      <details class="qa glass">
        <summary><h3>{html.escape(q)}</h3><span class="plus" aria-hidden="true"><svg class="ico"><use href="#i-plus"/></svg></span></summary>
        <div class="qa__a"><p>{html.escape(a)}</p></div>
      </details>''')
    return '\n'.join(out)


def jsonld(p):
    url = f'{BASE}/{p["slug"]}/'
    crumbs = [('Início', f'{BASE}/')]
    ar = area(p)
    if p['slug'] != ar['head']:
        crumbs.append((ar['nome'], f'{BASE}/{ar["head"]}/'))
    crumbs.append((p['crumb'], url))
    return {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'Service',
                '@id': url + '#servico',
                'name': re.sub('<[^>]+>', '', p['h1']).rstrip('.'),
                'serviceType': p['crumb'],
                'description': p['desc'],
                'url': url,
                'provider': {'@id': f'{BASE}/#escritorio'},
                'areaServed': [{'@type': 'City', 'name': 'Natal'}, {'@type': 'State', 'name': 'Rio Grande do Norte'}, {'@type': 'Country', 'name': 'Brasil'}],
            },
            {
                '@type': 'LegalService',
                '@id': f'{BASE}/#escritorio',
                'name': 'Thayná Cabral Advocacia',
                'url': f'{BASE}/',
                'telephone': '+55-84-99701-0660',
                'image': f'{BASE}/og.jpg',
                'address': {'@type': 'PostalAddress', 'addressLocality': 'Natal', 'addressRegion': 'RN', 'addressCountry': 'BR'},
            },
            {
                '@type': 'BreadcrumbList',
                'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(crumbs)],
            },
            {
                '@type': 'FAQPage',
                'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']],
            },
        ],
    }, crumbs


def render(p):
    url = f'{BASE}/{p["slug"]}/'
    ld, crumbs = jsonld(p)
    w = html.escape(wa(p['wa']))
    crumbs_html = ''.join(
        f'<li><a href="{u.replace(BASE, "")}">{html.escape(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{html.escape(n)}</li>'
        for i, (n, u) in enumerate(crumbs))
    secoes = '\n'.join(f'<h2 id="{slugify(h)}">{h}</h2>{b}' for h, b in p['secoes'])
    rel = ''.join(
        f'<a href="/{s}/"><strong>{BY_SLUG[s]["crumb"]}</strong><span>{html.escape(BY_SLUG[s]["desc"].split(". ")[0])}.</span></a>'
        for s in p['rel'])
    og_title = re.sub('<[^>]+>', '', p['h1']).rstrip('.') + ' | Thayná Cabral Advocacia'
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['title'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0B1120">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Thayná Cabral Advocacia">
<meta property="og:title" content="{html.escape(og_title)}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Dra. Thayná Cabral, advogada em Natal-RN, {OAB}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico?v=3" sizes="any">
<link rel="icon" href="/favicon-192.png?v=3" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=3">
<link rel="preload" href="/assets/fonts/cormorant-garamond-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/cormorant-garamond-latin-wght-italic.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.FX)document.documentElement.classList.remove('js')}},2500)</script>
<script src="/assets/js/fx.js" defer></script>
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
<style>
{CSS}{PAGE_CSS}</style>
</head>
<body>
{SPRITE}
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="bg" aria-hidden="true"></div>

{HEADER}

<main id="conteudo">
<nav class="crumbs" aria-label="Você está em"><ol>{crumbs_html}</ol></nav>

<section class="phero" aria-labelledby="h1">
  <p class="eyebrow" style="margin:0">{p['eyebrow']}</p>
  <h1 id="h1">{p['h1']}</h1>
  <p class="hero__sub">{p['lead']}</p>
  <div class="hero__ctas">
    <a class="btn btn--gold" data-wa href="{w}" target="_blank" rel="noopener"><svg class="wa-i" aria-hidden="true"><use href="#i-wa"/></svg><span class="long">Falar com a advogada no WhatsApp</span><span class="short">Falar no WhatsApp</span></a>
    <a class="link" href="#duvidas">Ver perguntas frequentes</a>
  </div>
</section>

<div class="layout">
  <article class="prose">
{secoes}
    <p class="note">Conteúdo informativo, atualizado em 2026. Cada caso tem particularidades e precisa de análise individual dos documentos.</p>
  </article>
  <aside class="aside glass" aria-label="Fale com a advogada">
    <div class="aside__who">
      <picture><source srcset="/assets/img/thayna-cabral.webp" type="image/webp"><img src="/assets/img/thayna-cabral.jpg" alt="" width="64" height="64" loading="lazy"></picture>
      <div><strong>Dra. Thayná Cabral</strong><span>Advogada · {OAB}</span></div>
    </div>
    <p>Envie um resumo da sua situação pelo WhatsApp. Respondemos para marcar o atendimento, presencial em Natal ou online.</p>
    <a class="btn btn--gold" data-wa href="{w}" target="_blank" rel="noopener"><svg class="wa-i" aria-hidden="true"><use href="#i-wa"/></svg>Falar no WhatsApp</a>
    <ul>
      <li>{ico('pin')}Natal-RN e online</li>
      <li>{ico('clock')}Consulta com hora marcada</li>
      <li>{ico('seal')}{OAB}</li>
    </ul>
  </aside>
</div>

<section id="duvidas" class="sec sec--sand" aria-labelledby="faq-t">
  <div class="wrap faq">
    <div class="faq__head">
      <p class="eyebrow" style="margin:0">Perguntas Frequentes</p>
      <h2 id="faq-t" class="h2">Dúvidas sobre <em>{p['crumb'] if p['crumb'].startswith(('Direito', 'BPC')) else p['crumb'][0].lower() + p['crumb'][1:]}.</em></h2>
      <p class="lead">Não encontrou a sua dúvida? Envie pelo WhatsApp e retornamos com orientação.</p>
    </div>
    <div class="faq__list">
{faq_html(p['faq'])}
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="rel-t">
  <div class="wrap">
    <div class="sec__head"><div><p class="eyebrow" style="margin:0">Veja também</p><h2 id="rel-t" class="h2">Outros temas do <em>{area(p)['nome']}.</em></h2></div></div>
    <div class="related">{rel}</div>
  </div>
</section>

<section class="sec" style="padding-top:0" aria-labelledby="cta-t">
  <div class="cta glass">
    <img src="/assets/img/simbolo-gold.webp" alt="" width="145" height="144" loading="lazy">
    <h2 id="cta-t" class="h2">Quer entender o seu caso? <em>Converse com a Dra. Thayná.</em></h2>
    <p class="lead">Conte um pouco sobre a sua situação. Retornamos com clareza sobre os próximos passos.</p>
    <a class="btn btn--gold" style="height:60px;padding:0 32px;margin-top:8px" data-wa href="{w}" target="_blank" rel="noopener"><svg class="wa-i" aria-hidden="true"><use href="#i-wa"/></svg><span class="long">Falar com a advogada no WhatsApp</span><span class="short">Falar no WhatsApp</span></a>
  </div>
</section>
</main>

{footer()}

<a class="wa" data-wa href="{w}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp"><svg aria-hidden="true"><use href="#i-wa"/></svg></a>

<script>
(function(){{
  var b=document.querySelector('.menu-btn'),m=document.getElementById('mnav');
  function set(o){{b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fechar menu':'Abrir menu');m.classList.toggle('open',o)}}
  b.addEventListener('click',function(){{set(b.getAttribute('aria-expanded')!=='true')}});
  m.addEventListener('click',function(e){{if(e.target.closest('a'))set(false)}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&b.getAttribute('aria-expanded')==='true'){{set(false);b.focus()}}}});
}})();
document.addEventListener('click',function(e){{var a=e.target.closest('[data-wa]');if(a&&window.clarity)window.clarity('event','whatsapp_click')}});
</script>
</body>
</html>
'''


def check(p, out):
    erros = []
    if len(p['title']) > 60:
        erros.append(f'title com {len(p["title"])} caracteres')
    if not 120 <= len(p['desc']) <= 160:
        erros.append(f'description com {len(p["desc"])} caracteres')
    if out.count('<h1') != 1:
        erros.append('mais de um H1')
    internos = set(re.findall(r'href="(/[a-z][^"#]*/)"', out)) - {'/' + p['slug'] + '/'}
    if len(internos) < 3:
        erros.append(f'só {len(internos)} links internos')
    return erros


def build_sitemap():
    # o lastmod só muda quando o conteúdo do <main> muda (CSS, cabeçalho e rodapé não contam)
    urls = ['/'] + [f'/{p["slug"]}/' for p in PAGES] + ['/privacidade.html']
    reg = Path(__file__).parent / 'lastmod.json'
    datas = json.loads(reg.read_text(encoding='utf-8')) if reg.exists() else {}
    for u in urls:
        f = ROOT / u.strip('/') if u.endswith('.html') else ROOT / u.strip('/') / 'index.html'
        s = f.read_text(encoding='utf-8')
        m = re.search(r'<main.*?</main>', s, re.S)
        h = hashlib.sha1((m.group(0) if m else s).encode()).hexdigest()[:12]
        if datas.get(u, {}).get('hash') != h:
            datas[u] = {'hash': h, 'data': HOJE}
    reg.write_text(json.dumps(datas, indent=1) + '\n', encoding='utf-8', newline='\n')
    body = '\n'.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{datas[u]["data"]}</lastmod></url>' for u in urls)
    (ROOT / 'sitemap.xml').write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n',
        encoding='utf-8', newline='\n')


def build_llms():
    p = ROOT / 'llms.txt'
    s = p.read_text(encoding='utf-8')
    linhas = ['- [Página inicial](%s/): áreas de atuação, sobre a advogada, como funciona o atendimento e perguntas frequentes.' % BASE]
    linhas += [f'- [{pg["crumb"]}]({BASE}/{pg["slug"]}/): {pg["desc"]}' for pg in PAGES]
    linhas.append(f'- [Política de Privacidade]({BASE}/privacidade.html)')
    s = re.sub(r'(## Páginas\n).*?(\n\n## )', lambda m: m.group(1) + '\n'.join(linhas) + m.group(2), s, flags=re.S)
    p.write_text(s, encoding='utf-8', newline='\n')


def update_index_footer():
    p = ROOT / 'index.html'
    s = p.read_text(encoding='utf-8')
    if '<!-- FOOTER' in s:
        s = re.sub(r'<!-- FOOTER.*?<!-- /FOOTER -->', lambda m: footer(), s, flags=re.S)
    else:
        s = re.sub(r'<footer class="ftr">.*?</footer>', lambda m: footer(), s, flags=re.S)
    p.write_text(s, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    falhas = 0
    for p in PAGES:
        out = render(p)
        d = ROOT / p['slug']
        d.mkdir(exist_ok=True)
        (d / 'index.html').write_text(out, encoding='utf-8', newline='\n')
        erros = check(p, out)
        falhas += bool(erros)
        print(f'{"OK " if not erros else "ERRO"} /{p["slug"]}/  title {len(p["title"])} · desc {len(p["desc"])}' + (' · ' + '; '.join(erros) if erros else ''))
    update_index_footer()
    build_sitemap()
    build_llms()
    print('home (rodapé), sitemap.xml e llms.txt atualizados')
    raise SystemExit(1 if falhas else 0)
