# Artigos do blog (site/blog/<slug>/index.html), gerados pelo build.py.
#
# Só vão ao ar os artigos com publicar=True: deixe False enquanto a Dra. Thayná não revisar
# os fatos jurídicos. Com a lista vazia (ou só rascunhos), o build não gera /blog/ nem o link
# "Blog" do rodapé.
#
# Campos de cada artigo:
#   slug        endereço: /blog/<slug>/ (sem acento, com hífens)
#   area        'prev', 'trab' ou 'civ' (padrão 'prev')
#   hub         slug da página de serviço do assunto (precisa existir em PAGES): o artigo
#               linka para ela, e ela mostra o artigo na seção "Artigos sobre…"
#   crumb       nome curto para a trilha de navegação
#   title       H1 (texto puro, sem <em>)
#   seo         <title>: até 60 caracteres
#   desc        meta description: de 120 a 160 caracteres
#   lead        parágrafo abaixo do H1
#   answer      "Resposta rápida": 2 a 4 frases que respondem à pergunta do título
#   secoes      [(h2, html)] com <p>, <ul>, <ol class="steps-l">, <div class="table-wrap"><table>
#   faq         [(pergunta, resposta)] em texto puro (aparecem na página; sem FAQPage no JSON-LD,
#               porque o Google encerrou esse resultado em 05/2026)
#   cta         (título, texto) da caixa que leva à página de serviço, sem linguagem de venda
#               (Provimento 205/2021)
#   wa          mensagem pronta do WhatsApp
#   rel         slugs de outros artigos (2 ou 3) para "Leia também"
#   publicado   'AAAA-MM-DD'
#   atualizado  'AAAA-MM-DD' (troque sempre que mudar o conteúdo)
#   publicar    True para ir ao ar
#
# Plano de artigos e links: seo-cluster/cluster-plan.md

# Valores de 2026 (Decreto 12.797/2025 e Portaria Interministerial MPS/MF 13/2026): revisar em janeiro.
SM = 'R$ 1.621,00'
TETO = 'R$ 8.475,55'
D = '2026-11-12'

POSTS = [
    # ============================================================ Aposentadoria
    dict(
        slug='aposentadoria-por-idade-mulher',
        hub='aposentadoria-natal',
        crumb='Aposentadoria da mulher',
        title='Aposentadoria por idade da mulher: idade, carência e valor em 2026',
        seo='Aposentadoria por Idade da Mulher em 2026: Regras e Valor',
        desc='Com quantos anos a mulher se aposenta por idade em 2026, quantas contribuições precisa e como o INSS calcula o valor. Regras explicadas sem juridiquês.',
        lead='A Reforma da Previdência mudou a idade e o cálculo da aposentadoria da mulher. Veja o que vale em 2026, o que conta como contribuição e como estimar o valor.',
        answer=f'Em 2026, a mulher que trabalha na cidade se aposenta por idade aos <strong>62 anos</strong>, com pelo menos <strong>15 anos de contribuição</strong> (180 meses). O valor é de 60% da média dos salários desde julho de 1994, mais 2% por ano que passar de 15 anos de contribuição, e nunca fica abaixo do salário mínimo ({SM}). A trabalhadora rural se aposenta aos 55 anos.',
        secoes=[
            ('A idade mínima da mulher em 2026', '''
<p>Antes da Reforma da Previdência (Emenda Constitucional 103, de 13 de novembro de 2019), a mulher se aposentava por idade aos 60 anos. A reforma subiu essa idade aos poucos, 6 meses por ano, até chegar a <strong>62 anos em 2023</strong>. Desde então, a idade não muda mais:</p>
<div class="table-wrap"><table>
<tr><th>Ano</th><th>Idade mínima da mulher</th></tr>
<tr><td>2019</td><td>60 anos</td></tr>
<tr><td>2020</td><td>60 anos e 6 meses</td></tr>
<tr><td>2021</td><td>61 anos</td></tr>
<tr><td>2022</td><td>61 anos e 6 meses</td></tr>
<tr><td>2023 em diante</td><td>62 anos</td></tr>
</table></div>
<p>Quem completou a idade da tabela no ano em que ela valia já tem o direito garantido, mesmo que só peça a aposentadoria agora. Por exemplo: a mulher que fez 61 anos em 2021 e já tinha 15 anos de contribuição pode se aposentar pela regra daquele ano.</p>'''),
            ('Quantas contribuições são necessárias', '''
<p>São <strong>15 anos de contribuição</strong>, o que o INSS chama de carência de 180 meses. Entram na conta:</p>
<ul>
<li>os períodos de carteira assinada, mesmo que a empresa não tenha recolhido o INSS;</li>
<li>as contribuições como autônoma, MEI ou facultativa (dona de casa, estudante);</li>
<li>os períodos em que você recebeu auxílio-doença, se ficaram entre períodos de contribuição;</li>
<li>o tempo de serviço público, com certidão do órgão (o tempo rural entra pela aposentadoria híbrida, explicada abaixo).</li>
</ul>
<p>Antes de pedir, confira o <strong>CNIS</strong> (extrato de contribuições do Meu INSS). Empregos antigos costumam faltar ou aparecer sem salário, e cada mês que falta atrasa a aposentadoria.</p>'''),
            ('Como o valor é calculado', '''
<p>O INSS faz a média de <strong>todos os salários de contribuição desde julho de 1994</strong>, corrigidos. A aposentadoria é de <strong>60% dessa média</strong>, mais <strong>2% para cada ano</strong> que passar de 15 anos de contribuição.</p>
<div class="table-wrap"><table>
<tr><th>Tempo de contribuição</th><th>Percentual da média</th></tr>
<tr><td>15 anos</td><td>60%</td></tr>
<tr><td>20 anos</td><td>70%</td></tr>
<tr><td>25 anos</td><td>80%</td></tr>
<tr><td>30 anos</td><td>90%</td></tr>
<tr><td>35 anos</td><td>100%</td></tr>
</table></div>
<p>Exemplo: com média de R$ 3.000 e 22 anos de contribuição, o percentual é 74% (60% + 7 × 2%), e a aposentadoria fica em R$ 2.220. O valor nunca é menor que o salário mínimo ({SM} em 2026) nem maior que o teto do INSS ({TETO}).</p>''' .replace('{SM}', SM).replace('{TETO}', TETO)),
            ('Outras regras que podem ser melhores', '''
<p>A aposentadoria por idade não é a única opção. A mulher que tem muito tempo de contribuição pode se encaixar numa regra de transição da aposentadoria por tempo de contribuição, com valor maior. Quem trabalhou na roça pode usar a <a href="/blog/aposentadoria-rural/">aposentadoria rural</a> (55 anos) ou a híbrida, que soma o tempo rural ao da cidade. As regras de transição estão na página de <a href="/aposentadoria-natal/">aposentadoria</a>.</p>
<p>Se você tem 62 anos ou mais e não chega a 15 anos de contribuição, veja o que fazer em <a href="/blog/aposentadoria-quem-nunca-contribuiu/">aposentadoria para quem nunca contribuiu</a>.</p>'''),
            ('Como pedir', '''
<ol class="steps-l">
<li><strong>Confira o CNIS</strong> no Meu INSS e separe carteiras de trabalho, carnês e contracheques dos períodos que faltam.</li>
<li><strong>Faça o pedido</strong> no Meu INSS (opção "Aposentadoria por idade urbana") ou pelo telefone 135.</li>
<li><strong>Acompanhe as exigências</strong>: se o INSS pedir documentos, o prazo para entregar é curto.</li>
</ol>
<p>Os valores são devidos desde a data do pedido, mesmo que o INSS demore para responder.</p>'''),
        ],
        faq=[
            ('Com quantos anos a mulher se aposenta por idade em 2026?', 'Aos 62 anos, com 15 anos de contribuição, se trabalha na cidade. A trabalhadora rural se aposenta aos 55 anos, com 15 anos de atividade rural.'),
            ('Mulher com 60 anos pode se aposentar?', 'Pela idade, só se completou os requisitos da regra do ano: por exemplo, 60 anos e 15 anos de contribuição até 2019. Se não, pode haver outra regra, como a rural ou uma regra de transição por tempo de contribuição.'),
            ('Dona de casa que paga o INSS se aposenta por idade?', 'Sim. As contribuições como facultativa contam para a aposentadoria por idade. Quem paga pelo plano de 5% (baixa renda) ou de 11% tem direito só à aposentadoria por idade, no valor de um salário mínimo.'),
            ('A aposentada pode continuar trabalhando?', 'Pode. A aposentadoria por idade não impede o trabalho com carteira assinada ou como autônoma, mas as novas contribuições não aumentam o valor da aposentadoria.'),
        ],
        cta=('Quer saber qual regra é melhor para você?', 'O valor depende do seu histórico de contribuições e de períodos que às vezes não aparecem no CNIS.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre aposentadoria da mulher e quero saber se já posso me aposentar.',
        rel=['aposentadoria-rural', 'aposentadoria-quem-nunca-contribuiu', 'acumular-pensao-e-aposentadoria'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='aposentadoria-rural',
        hub='aposentadoria-natal',
        crumb='Aposentadoria rural',
        title='Aposentadoria rural por idade: quem tem direito e como provar',
        seo='Aposentadoria Rural por Idade: Quem Tem Direito e Provas',
        desc='Aposentadoria rural: idade (55 e 60 anos), 15 anos de atividade, quem é segurado especial, documentos que provam o trabalho na roça e a aposentadoria híbrida.',
        lead='Quem trabalhou na agricultura familiar ou na pesca artesanal pode se aposentar mais cedo e sem ter pago o INSS. O desafio é provar o trabalho. Veja as regras e os documentos que ajudam.',
        answer='A aposentadoria rural por idade é concedida à mulher aos <strong>55 anos</strong> e ao homem aos <strong>60 anos</strong>, com <strong>15 anos de atividade rural</strong>. O pequeno agricultor e o pescador artesanal que trabalham em família (segurados especiais) não precisam ter pago o INSS: basta provar o trabalho. O valor é de um salário mínimo.',
        secoes=[
            ('Quem tem direito', '''
<p>A regra vale para o <strong>segurado especial</strong>: quem trabalha na terra ou na pesca para o sustento da família, sem empregados permanentes. Entram nessa categoria:</p>
<ul>
<li>pequeno produtor rural, proprietário ou não, em área de até 4 módulos fiscais;</li>
<li>parceiro, meeiro, arrendatário e comodatário rural;</li>
<li>pescador artesanal e marisqueira;</li>
<li>cônjuge, companheiro e filhos maiores de 16 anos que trabalham junto com a família.</li>
</ul>
<p>O empregado rural com carteira assinada também se aposenta com 55 ou 60 anos, mas precisa de 15 anos de contribuição registrada, como o trabalhador urbano.</p>'''),
            ('Os 15 anos de atividade', '''
<p>São 180 meses de trabalho rural, que podem ser intercalados com outros trabalhos. O período deve ser <strong>próximo da data do pedido</strong> ou da data em que a pessoa completou a idade: quem deixou a roça há muitos anos, em regra, não se aposenta pela regra rural, mas pode usar a híbrida.</p>
<p>A reforma de 2019 não mudou a idade nem o tempo da aposentadoria rural.</p>'''),
            ('Documentos que provam o trabalho rural', '''
<p>O pedido começa com a <strong>autodeclaração do segurado especial</strong>, um formulário do INSS em que a pessoa descreve onde e como trabalhou. Ela precisa vir acompanhada de documentos da época, como:</p>
<ul>
<li>contrato de arrendamento, parceria ou comodato, escritura ou ITR e CCIR do imóvel;</li>
<li>notas fiscais de venda da produção ou bloco de produtor rural;</li>
<li>CAF ou DAP (cadastro da agricultura familiar), Garantia-Safra e contratos do Pronaf;</li>
<li>certidões de casamento ou de nascimento dos filhos com a profissão de lavrador ou agricultor;</li>
<li>ficha do sindicato rural, matrícula escolar dos filhos em escola rural e ficha do posto de saúde.</li>
</ul>
<p>Não é preciso ter um documento para cada ano, mas documentos de anos diferentes fortalecem o pedido. Na Justiça, esses documentos são completados com testemunhas: segundo a Súmula 149 do STJ, testemunha sozinha não basta.</p>'''),
            ('Aposentadoria híbrida: roça e cidade', '''
<p>Quem trabalhou parte da vida na roça e parte na cidade pode somar os dois períodos na <strong>aposentadoria híbrida</strong>. A idade é a urbana: <strong>62 anos para a mulher e 65 para o homem</strong>, com 15 anos ao todo. O STJ decidiu (Tema 1007) que o trabalho rural antigo, mesmo sem contribuição, conta para a híbrida.</p>
<p>O valor da híbrida segue o cálculo da <a href="/blog/aposentadoria-por-idade-mulher/">aposentadoria por idade urbana</a> e pode passar de um salário mínimo.</p>'''),
            ('Por que o INSS nega a aposentadoria rural', '''
<ul>
<li>documentos insuficientes ou de períodos muito antigos;</li>
<li>vínculo urbano de algum membro da família, que o INSS entende como fim da economia familiar;</li>
<li>propriedade maior que 4 módulos fiscais ou contratação de empregados.</li>
</ul>
<p>Muitas negativas são revertidas na Justiça Federal, com a audiência de testemunhas. Veja mais na página de <a href="/aposentadoria-natal/">aposentadoria em Natal</a>.</p>'''),
        ],
        faq=[
            ('Quem nunca pagou o INSS pode se aposentar como rural?', 'Sim, se for segurado especial e provar 15 anos de trabalho rural em regime de economia familiar. A contribuição dele é feita sobre a venda da produção, quando há venda.'),
            ('Com quantos anos a mulher da roça se aposenta?', 'Aos 55 anos, com 15 anos de atividade rural. O homem se aposenta aos 60.'),
            ('Declaração do sindicato ainda serve?', 'Ela não é mais suficiente sozinha. Desde 2019, o INSS usa a autodeclaração do segurado especial, que precisa vir com documentos da época. A ficha do sindicato pode ajudar como um desses documentos.'),
            ('Quem mora na cidade e trabalha na roça tem direito?', 'Pode ter. O que importa é o trabalho rural em família, não o endereço. Morar na cidade perto da área de cultivo é comum e não impede a aposentadoria.'),
        ],
        cta=('Tem trabalho rural para provar?', 'Cada documento conta, e a forma de apresentar a prova faz diferença no INSS e na Justiça.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre aposentadoria rural e quero saber se tenho direito.',
        rel=['aposentadoria-por-idade-mulher', 'aposentadoria-quem-nunca-contribuiu'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='aposentadoria-quem-nunca-contribuiu',
        hub='aposentadoria-natal',
        crumb='Nunca contribuí',
        title='Nunca contribuí com o INSS: posso me aposentar?',
        seo='Nunca Contribuí com o INSS: Posso Me Aposentar?',
        desc='Quem nunca pagou o INSS não tem aposentadoria urbana, mas tem outros caminhos: aposentadoria rural, BPC para idosos a partir de 65 anos e contribuição de 5%.',
        lead='É uma das dúvidas mais comuns de quem chega aos 60 anos sem ter contribuído. A resposta curta é não, mas existem alternativas que muita gente desconhece.',
        answer=f'Quem nunca contribuiu <strong>não tem direito à aposentadoria urbana</strong>, que exige 15 anos de contribuição. Mas há caminhos: a <strong>aposentadoria rural</strong>, para quem trabalhou na agricultura familiar; o <strong>BPC/LOAS</strong>, um salário mínimo ({SM}) para idosos a partir de 65 anos com renda baixa; e começar a contribuir, inclusive com 5% do salário mínimo no caso da dona de casa de baixa renda.',
        secoes=[
            ('Por que não existe aposentadoria sem contribuição', '''
<p>A aposentadoria do INSS é um seguro: só recebe quem pagou ou quem a lei trata como segurado. Na cidade, a aposentadoria por idade exige <strong>15 anos de contribuição</strong>, além da idade mínima (62 anos para a mulher e 65 para o homem).</p>
<p>Antes de concluir que nunca contribuiu, porém, confira o <strong>CNIS</strong> no Meu INSS. Empregos com carteira assinada contam mesmo que a empresa não tenha recolhido, e o trabalho sem carteira pode ser reconhecido na Justiça do Trabalho (veja <a href="/trabalho-sem-carteira-assinada/">trabalho sem carteira assinada</a>).</p>'''),
            ('Caminho 1: aposentadoria rural', '''
<p>Quem trabalhou na roça ou na pesca artesanal com a família pode se aposentar <strong>sem ter pago o INSS</strong>, aos 55 anos (mulher) ou 60 anos (homem), provando 15 anos de atividade rural. Os detalhes estão em <a href="/blog/aposentadoria-rural/">aposentadoria rural por idade</a>.</p>'''),
            ('Caminho 2: BPC/LOAS para idosos', '''
<p>O <strong>BPC</strong> paga um salário mínimo por mês a pessoas com <strong>65 anos ou mais</strong> que vivem em família de baixa renda, sem exigir contribuição. A regra geral é renda de até 1/4 do salário mínimo por pessoa da casa (R$ 405,25 em 2026), mas a Justiça analisa a realidade de cada família.</p>
<p>O BPC não é aposentadoria: não paga 13º e não deixa pensão. Veja <a href="/blog/como-pedir-bpc-loas/">como pedir o BPC/LOAS passo a passo</a> e <a href="/blog/bpc-loas-renda/">como o INSS calcula a renda</a>.</p>'''),
            ('Caminho 3: começar a contribuir', '''
<p>Quem ainda está longe da idade mínima pode começar a pagar. Há três formas para quem não tem emprego:</p>
<div class="table-wrap"><table>
<tr><th>Plano</th><th>Valor em 2026</th><th>Para quem</th></tr>
<tr><td>Facultativo baixa renda (5%)</td><td>R$ 81,05</td><td>Dona de casa sem renda própria, de família inscrita no CadÚnico com renda de até 2 salários mínimos</td></tr>
<tr><td>Plano simplificado (11%)</td><td>R$ 178,31</td><td>Autônomos e facultativos que contribuem sobre o salário mínimo</td></tr>
<tr><td>MEI</td><td>5% do salário mínimo, mais ISS ou ICMS</td><td>Pequeno empreendedor formalizado</td></tr>
</table></div>
<p>Nos planos de 5% e 11%, a aposentadoria é só por idade e de um salário mínimo. Quem começa aos 60 anos precisa de 15 anos de pagamento: por isso, para muitos, o BPC aos 65 é a saída mais próxima.</p>'''),
            ('Dá para pagar o INSS atrasado?', '''
<p>Depende. O <strong>autônomo</strong> que comprova que trabalhou num período pode pagar as contribuições daquele tempo, com juros e multa. Já o <strong>facultativo</strong> (dona de casa, estudante) não pode pagar meses anteriores à inscrição no INSS. Antes de pagar atrasados, faça as contas: em alguns casos o valor é alto e não resolve.</p>'''),
        ],
        faq=[
            ('Tenho 65 anos e nunca contribuí. O que posso receber?', 'Se a sua família tem renda baixa, pode ter direito ao BPC/LOAS, de um salário mínimo por mês. Se trabalhou na roça, pode ter direito à aposentadoria rural.'),
            ('Dona de casa que nunca pagou pode se aposentar?', 'Só se começar a contribuir e completar 15 anos de pagamento. Se for de família de baixa renda inscrita no CadÚnico, pode pagar 5% do salário mínimo. Aos 65 anos, o BPC é outra possibilidade.'),
            ('Quem recebe BPC pode receber aposentadoria depois?', 'Não ao mesmo tempo. Se a pessoa passar a ter direito à aposentadoria, deixa o BPC e fica com a aposentadoria, que paga 13º e deixa pensão.'),
            ('Pagar o INSS só no último ano adianta?', 'Não para a aposentadoria por idade, que exige 15 anos de contribuição. Pode servir para manter a qualidade de segurado e garantir auxílio-doença ou pensão para a família.'),
        ],
        cta=('Não sabe qual caminho serve para você?', 'Tempo rural, emprego antigo sem registro ou um CNIS incompleto podem mudar a resposta.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre quem nunca contribuiu e quero entender o meu caso.',
        rel=['como-pedir-bpc-loas', 'aposentadoria-rural', 'aposentadoria-por-idade-mulher'],
        publicado=D, atualizado=D, publicar=True,
    ),

    # ============================================================ BPC/LOAS
    dict(
        slug='como-pedir-bpc-loas',
        hub='bpc-loas-natal',
        crumb='Como pedir o BPC',
        title='Como pedir o BPC/LOAS passo a passo',
        seo='Como Pedir o BPC/LOAS Passo a Passo: Documentos e Prazos',
        desc='Passo a passo para pedir o BPC/LOAS do idoso ou da pessoa com deficiência: CadÚnico, pedido no Meu INSS, documentos, perícia, biometria e o que fazer se negar.',
        lead='O pedido do BPC é gratuito e pode ser feito pelo celular, mas um erro no CadÚnico ou um laudo incompleto é o bastante para a negativa. Veja a ordem certa e os cuidados de cada etapa.',
        answer='Para pedir o BPC/LOAS: <strong>1)</strong> inscreva ou atualize a família no CadÚnico, no CRAS; <strong>2)</strong> faça o pedido no Meu INSS ou pelo telefone 135; <strong>3)</strong> envie os documentos e, se for pessoa com deficiência, os laudos médicos; <strong>4)</strong> compareça à perícia e à avaliação social. Se o INSS negar, cabe recurso em 30 dias ou ação na Justiça Federal.',
        secoes=[
            ('Antes de tudo: quem pode pedir', '''
<p>O BPC é pago a <strong>idosos a partir de 65 anos</strong> e a <strong>pessoas com deficiência de qualquer idade</strong> com impedimento de longo prazo (2 anos ou mais), desde que a família tenha renda baixa. Não é preciso ter contribuído para o INSS. Os requisitos completos estão na página de <a href="/bpc-loas-natal/">BPC/LOAS</a>.</p>'''),
            ('Passo 1: CadÚnico em dia', '''
<p>O BPC só é analisado com a família inscrita no <strong>Cadastro Único</strong> e com o cadastro atualizado nos últimos 2 anos. A inscrição é feita no CRAS. Leve documento com CPF de <strong>todas</strong> as pessoas que moram na casa e comprovante de residência.</p>
<p>As informações do CadÚnico (quem mora na casa e quanto cada um ganha) precisam ser as mesmas do pedido no INSS. Diferenças entre os dois são uma das causas mais comuns de negativa.</p>'''),
            ('Passo 2: fazer o pedido no INSS', '''
<ol class="steps-l">
<li>Entre no <strong>Meu INSS</strong> (site ou aplicativo) com a conta gov.br, ou ligue para o <strong>135</strong>.</li>
<li>Em "Novo pedido", escolha <strong>Benefício Assistencial à Pessoa Idosa</strong> ou <strong>à Pessoa com Deficiência</strong>.</li>
<li>Preencha os dados da família e anexe os documentos.</li>
<li>Guarde o número do protocolo: é com ele que se acompanha o pedido.</li>
</ol>
<p>Desde a Lei 15.077/2024, é preciso ter <strong>biometria cadastrada</strong> (CNH, título de eleitor ou Carteira de Identidade Nacional) para pedir e para manter o benefício.</p>'''),
            ('Passo 3: documentos', '''
<ul>
<li>documento de identidade e CPF do requerente e de quem mora com ele;</li>
<li>comprovante de residência;</li>
<li>para a pessoa com deficiência: laudos e relatórios médicos recentes, com o <strong>CID</strong>, a descrição das limitações e a previsão de duração;</li>
<li>receitas, exames e relatórios de terapias, que ajudam a mostrar o impedimento no dia a dia;</li>
<li>se houver representante (curador ou responsável), o documento dele e o termo de curatela ou guarda.</li>
</ul>'''),
            ('Passo 4: perícia e avaliação social', '''
<p>O idoso não passa por perícia. A pessoa com deficiência passa por <strong>perícia médica</strong> e por <strong>avaliação social</strong>, em que um assistente social do INSS analisa as barreiras que ela enfrenta em casa, na escola e no trabalho. Leve todos os laudos e explique a rotina com detalhes.</p>
<p>Depois, acompanhe o pedido no Meu INSS. Se aparecer uma <strong>exigência</strong>, responda no prazo: o pedido pode ser arquivado se ela não for cumprida.</p>'''),
            ('Se o INSS negar', '''
<p>Leia o motivo na carta de indeferimento. Dá para <strong>recorrer em 30 dias</strong> ao Conselho de Recursos da Previdência Social, fazer um novo pedido com documentos melhores ou entrar na <strong>Justiça Federal</strong>. Quando a negativa é por renda, a Justiça pode olhar gastos com remédios, fraldas e tratamentos: veja <a href="/blog/bpc-loas-renda/">como funciona a renda no BPC</a>.</p>'''),
        ],
        faq=[
            ('Precisa de advogado para pedir o BPC?', 'Não. O pedido é gratuito e pode ser feito pela própria pessoa no Meu INSS ou no 135. A orientação ajuda a evitar erros no CadÚnico e nos laudos, que estão entre as causas mais comuns de negativa.'),
            ('Quanto tempo o INSS demora para responder?', 'Depende da fila e da agenda de perícia e avaliação social, que no caso da pessoa com deficiência pode levar meses. Se o BPC for concedido, os valores contam desde a data do pedido.'),
            ('O BPC paga 13º?', 'Não. O BPC é um benefício assistencial e não tem 13º salário nem deixa pensão por morte.'),
            ('Quem recebe BPC pode trabalhar?', 'O idoso que passa a ter renda pode perder o benefício se a renda da família passar do limite. A pessoa com deficiência que começa a trabalhar tem o BPC suspenso e pode voltar a recebê-lo se perder o emprego.'),
        ],
        cta=('Vai pedir o BPC ou já foi negado?', 'Um CadÚnico correto e laudos completos fazem diferença no resultado.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre como pedir o BPC e tenho uma dúvida.',
        rel=['bpc-loas-renda', 'bpc-loas-autismo', 'aposentadoria-quem-nunca-contribuiu'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='bpc-loas-autismo',
        hub='bpc-loas-natal',
        crumb='BPC e autismo',
        title='BPC/LOAS para autismo: requisitos, laudo e como pedir',
        seo='BPC/LOAS para Autismo: Requisitos, Laudo e Como Pedir',
        desc='Criança ou adulto com autismo (TEA) pode receber o BPC/LOAS. Veja os requisitos de renda, o que o laudo deve ter, como o INSS avalia e o que fazer se negar.',
        lead='O autismo é considerado deficiência pela lei, e muitas famílias têm direito ao BPC sem saber. O ponto decisivo costuma ser a forma como o laudo e os relatórios descrevem a rotina da pessoa.',
        answer='Sim, a pessoa com <strong>transtorno do espectro autista (TEA)</strong>, criança ou adulta, pode receber o BPC/LOAS, de um salário mínimo por mês. A Lei 12.764/2012 considera o autismo deficiência para todos os efeitos. É preciso que a família tenha <strong>renda baixa</strong> e que o INSS reconheça, na perícia e na avaliação social, impedimentos de longo prazo.',
        secoes=[
            ('Quem tem direito', '''
<p>O diagnóstico de autismo, sozinho, não garante o BPC. São três requisitos:</p>
<ul>
<li><strong>deficiência de longo prazo:</strong> o TEA com limitações que durem ou devam durar 2 anos ou mais, o que costuma acontecer;</li>
<li><strong>barreiras no dia a dia:</strong> dificuldades de comunicação, de convivência, de aprendizagem ou de autonomia, avaliadas pelo INSS;</li>
<li><strong>renda baixa:</strong> em regra, até 1/4 do salário mínimo por pessoa da casa (R$ 405,25 em 2026), com análise da realidade da família na Justiça.</li>
</ul>
<p>Não há idade mínima: bebês e crianças pequenas também podem receber.</p>'''),
            ('O que o laudo deve trazer', '''
<p>O laudo é a peça mais importante do pedido. Ele deve ser recente e, de preferência, de neuropediatra, psiquiatra ou neurologista, com:</p>
<ul>
<li>o diagnóstico e o <strong>CID</strong> (F84 na CID-10 ou 6A02 na CID-11) e o nível de suporte;</li>
<li>a descrição das <strong>limitações concretas</strong>: fala, alimentação, higiene, crises, sono, comportamento, necessidade de supervisão;</li>
<li>os tratamentos em curso e a frequência das terapias;</li>
<li>a informação de que o quadro é de <strong>longa duração</strong>.</li>
</ul>
<p>Junte também relatórios de fonoaudiologia, terapia ocupacional e psicologia, e um relatório da escola sobre a adaptação e o acompanhamento.</p>'''),
            ('Como é a avaliação do INSS', '''
<p>A pessoa com autismo passa por <strong>perícia médica</strong> e por <strong>avaliação social</strong>. No caso de crianças, o INSS compara as limitações com o que é esperado para a idade. Por isso, descreva a rotina real, inclusive nos dias difíceis, e leve os relatórios das terapias.</p>
<p>O passo a passo do pedido está em <a href="/blog/como-pedir-bpc-loas/">como pedir o BPC/LOAS</a>.</p>'''),
            ('A renda da família', '''
<p>O INSS soma a renda de quem mora na casa e divide pelo número de pessoas. Gastos com terapias, remédios e transporte não reduzem a renda no cálculo do INSS, mas são considerados pela Justiça quando a família passa um pouco do limite. Veja <a href="/blog/bpc-loas-renda/">como o INSS calcula a renda do BPC</a>.</p>'''),
            ('Se o INSS negar', '''
<p>As negativas mais comuns no autismo são "não constatação de impedimento de longo prazo" e "renda acima do limite". Nos dois casos, cabe recurso em 30 dias ou ação na <strong>Justiça Federal</strong>, onde há nova perícia e nova avaliação social. Um laudo mais detalhado costuma ser o que muda o resultado.</p>'''),
        ],
        faq=[
            ('Autismo leve (nível 1) dá direito ao BPC?', 'Pode dar, se as limitações forem de longo prazo e afetarem a participação da pessoa no dia a dia, e se a renda da família for baixa. O nível de suporte é considerado, mas não decide sozinho.'),
            ('A mãe que recebe o BPC do filho pode trabalhar?', 'Pode, mas o salário dela entra na renda da família. Se a renda por pessoa passar do limite, o benefício pode ser revisto.'),
            ('O BPC do autista é vitalício?', 'Não existe prazo fixo, mas o INSS revisa o benefício periodicamente. É importante manter o CadÚnico atualizado e guardar laudos recentes.'),
            ('Quem recebe Bolsa Família pode pedir o BPC para o filho autista?', 'Pode. Desde 2025 o INSS soma o Bolsa Família na renda, regra que é questionada na Justiça. Vale fazer o pedido e analisar a resposta.'),
        ],
        cta=('Seu filho tem autismo e a família tem renda baixa?', 'A forma como o laudo descreve a rotina costuma ser decisiva na perícia.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre BPC para autismo e quero saber se meu filho tem direito.',
        rel=['como-pedir-bpc-loas', 'bpc-loas-renda', 'pensao-por-morte-filhos'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='bpc-loas-renda',
        hub='bpc-loas-natal',
        crumb='Renda no BPC',
        title='Renda por pessoa no BPC/LOAS: como o INSS calcula',
        seo='Renda do BPC/LOAS em 2026: Como o INSS Calcula',
        desc='Como o INSS calcula a renda por pessoa no BPC/LOAS em 2026: quem entra na família, o limite de R$ 405,25, o que não conta e quando a Justiça aceita renda maior.',
        lead='A renda é o motivo mais comum de negativa do BPC. Entender quem entra na conta e o que fica de fora ajuda a evitar erros no pedido e a saber se vale recorrer.',
        answer='O INSS soma a renda bruta de quem mora na casa e faz parte da família, e divide pelo número dessas pessoas. Em regra, o resultado precisa ser de até <strong>1/4 do salário mínimo por pessoa</strong>, ou seja, <strong>R$ 405,25 em 2026</strong>. Alguns valores ficam fora da conta, e a Justiça pode aceitar renda maior quando a família prova a necessidade.',
        secoes=[
            ('Quem entra na família', '''
<p>Para o BPC, a família é formada por quem <strong>mora na mesma casa</strong> e é:</p>
<ul>
<li>o próprio requerente e o cônjuge ou companheiro;</li>
<li>os pais e, na falta deles, madrasta ou padrasto;</li>
<li>irmãos solteiros;</li>
<li>filhos e enteados solteiros e menores sob tutela.</li>
</ul>
<p>Filhos casados, genros, noras, netos, avós e outros parentes <strong>não entram</strong>, mesmo morando juntos. Também não entra quem mora em outra casa, ainda que ajude com dinheiro.</p>'''),
            ('Como fazer a conta', '''
<p>Some a renda bruta mensal das pessoas da família e divida pelo número delas. Exemplo: casal de idosos em que o marido, de 67 anos, recebe aposentadoria de R$ 2.000. A renda por pessoa é de R$ 1.000, acima do limite, e a esposa não recebe o BPC pelo critério do INSS.</p>
<p>Agora, se a aposentadoria do marido fosse de <strong>um salário mínimo</strong>, ela ficaria fora da conta (veja abaixo), e a esposa poderia receber.</p>'''),
            ('O que não entra na renda', '''
<ul>
<li><strong>BPC ou aposentadoria de até um salário mínimo</strong> recebido por outro idoso de 65 anos ou mais ou por pessoa com deficiência da família;</li>
<li>a remuneração de estágio ou de aprendiz da pessoa com deficiência;</li>
<li>pensão especial de natureza indenizatória e alguns auxílios eventuais.</li>
</ul>
<p>Já o <strong>Bolsa Família</strong> passou a ser somado pelo INSS desde 2025 (Decreto 12.534/2025). A mudança é questionada na Justiça, e há decisões que afastam essa regra.</p>'''),
            ('Quando a Justiça aceita renda maior', '''
<p>O limite de 1/4 não é absoluto. O Supremo Tribunal Federal reconheceu que a miserabilidade pode ser provada por outros meios, e a lei passou a prever a ampliação do limite para até meio salário mínimo em situações regulamentadas. Na prática, a Justiça considera:</p>
<ul>
<li>gastos com remédios, fraldas, alimentação especial e tratamentos que o SUS não fornece;</li>
<li>o grau de dependência da pessoa e a necessidade de alguém deixar de trabalhar para cuidar dela;</li>
<li>as condições da moradia, verificadas na avaliação social ou por um perito.</li>
</ul>
<p>Guarde receitas, notas fiscais e comprovantes: eles são a prova desses gastos. O passo a passo do pedido está em <a href="/blog/como-pedir-bpc-loas/">como pedir o BPC/LOAS</a>.</p>'''),
        ],
        faq=[
            ('Qual o valor da renda por pessoa para receber o BPC em 2026?', 'Até R$ 405,25 por pessoa, que é 1/4 do salário mínimo de R$ 1.621,00. Na Justiça, famílias com renda um pouco maior podem receber se provarem a necessidade.'),
            ('A aposentadoria do meu marido conta na renda para o meu BPC?', 'Se ele tem 65 anos ou mais e a aposentadoria é de um salário mínimo, ela não entra na conta. Se for maior que o salário mínimo, entra inteira.'),
            ('Pensão alimentícia conta como renda?', 'Sim. A pensão alimentícia recebida pelo requerente ou por alguém da família entra no cálculo da renda.'),
            ('Filho que mora em outra casa e ajuda nas despesas conta?', 'Não. Só entra quem mora na mesma casa e faz parte do grupo familiar previsto na lei.'),
        ],
        cta=('O BPC foi negado por renda?', 'A conta do INSS nem sempre está certa, e a Justiça analisa a realidade da família.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre a renda do BPC e quero saber se tenho direito.',
        rel=['como-pedir-bpc-loas', 'bpc-loas-autismo', 'aposentadoria-quem-nunca-contribuiu'],
        publicado=D, atualizado=D, publicar=True,
    ),

    # ============================================================ Auxílio-doença
    dict(
        slug='auxilio-doenca-quem-tem-direito',
        hub='auxilio-doenca-negado',
        crumb='Auxílio-doença: quem tem direito',
        title='Auxílio-doença: quem tem direito e qual a carência',
        seo='Auxílio-Doença: Quem Tem Direito e Qual a Carência',
        desc='Quem tem direito ao auxílio-doença do INSS, a carência de 12 contribuições, as doenças que dispensam a carência, a qualidade de segurado e o auxílio do MEI.',
        lead='O auxílio-doença, hoje chamado de auxílio por incapacidade temporária, protege quem fica impedido de trabalhar por doença ou acidente. Veja os três requisitos e as exceções.',
        answer='Tem direito ao auxílio-doença quem: <strong>1)</strong> está <strong>incapaz para o trabalho</strong> por mais de 15 dias; <strong>2)</strong> tem <strong>qualidade de segurado</strong> (está contribuindo ou no período de graça); e <strong>3)</strong> cumpriu a <strong>carência de 12 contribuições</strong>. A carência é dispensada em acidentes, doenças do trabalho e em doenças graves listadas pelo governo.',
        secoes=[
            ('Requisito 1: incapacidade para o trabalho', '''
<p>Não basta estar doente: a doença precisa <strong>impedir o seu trabalho</strong> habitual por mais de 15 dias seguidos. Quem tem diabetes controlada e trabalha normalmente não tem direito; quem tem uma crise de coluna que impede o trabalho de pedreiro, sim. A incapacidade é verificada na <strong>perícia médica</strong> do INSS ou por análise de documentos (Atestmed).</p>
<p>Doença que começou antes da filiação ao INSS não dá direito, exceto se a incapacidade veio do agravamento depois de filiado.</p>'''),
            ('Requisito 2: qualidade de segurado', '''
<p>É estar coberto pelo INSS. Quem está trabalhando com carteira ou contribuindo tem. Quem parou de contribuir continua coberto no <strong>período de graça</strong>:</p>
<ul>
<li>12 meses após a última contribuição, em regra;</li>
<li>24 meses, para quem tem mais de 120 contribuições sem perder a qualidade de segurado;</li>
<li>mais 12 meses para o desempregado que comprova a situação, por exemplo com o seguro-desemprego.</li>
</ul>'''),
            ('Requisito 3: carência de 12 contribuições', '''
<p>A carência é de <strong>12 contribuições mensais</strong>. Ela é dispensada quando a incapacidade vem de:</p>
<ul>
<li><strong>acidente de qualquer natureza</strong>, no trabalho ou fora dele;</li>
<li><strong>doença profissional ou do trabalho</strong> (veja <a href="/acidente-de-trabalho/">acidente de trabalho</a>);</li>
<li>doenças da lista oficial, como tuberculose ativa, hanseníase, câncer, cardiopatia grave, doença de Parkinson, esclerose múltipla, nefropatia grave, hepatopatia grave, AIDS, alienação mental, cegueira, paralisia irreversível e AVC agudo.</li>
</ul>
<p>Quem perdeu a qualidade de segurado e voltou a contribuir precisa de metade da carência (6 contribuições) para recuperar o direito.</p>'''),
            ('Empregado, MEI e autônomo', '''
<p>O <strong>empregado com carteira</strong> recebe os primeiros 15 dias da empresa, e o INSS paga a partir do 16º dia. O <strong>MEI</strong>, o autônomo e o facultativo recebem do INSS desde o início da incapacidade, se pedirem em até 30 dias. O MEI tem direito ao auxílio-doença nas mesmas regras, com carência de 12 contribuições pagas em dia.</p>
<p>O valor é explicado em <a href="/blog/valor-auxilio-doenca/">como é calculado o auxílio-doença</a>.</p>'''),
        ],
        faq=[
            ('Quem está desempregado tem direito ao auxílio-doença?', 'Tem, se ainda estiver no período de graça: em regra, até 12 meses após o último emprego ou contribuição, prazo que pode chegar a 36 meses em alguns casos.'),
            ('Câncer precisa de carência para o auxílio-doença?', 'Não. Neoplasia maligna está na lista de doenças que dispensam a carência. A pessoa só precisa ter qualidade de segurado quando a incapacidade começou.'),
            ('Posso pedir auxílio-doença sem perícia?', 'Em muitos casos, sim: pelo Atestmed, o INSS analisa o atestado enviado pelo Meu INSS, sem perícia presencial, dentro de limites de prazo definidos pelo INSS.'),
            ('Doença psiquiátrica dá direito ao auxílio-doença?', 'Sim, se causar incapacidade para o trabalho. Depressão grave, transtorno bipolar e ansiedade incapacitante estão entre as causas mais comuns de afastamento.'),
        ],
        cta=('Está sem conseguir trabalhar?', 'O resultado depende muito dos documentos médicos e da forma como a incapacidade é descrita.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre auxílio-doença e quero saber se tenho direito.',
        rel=['valor-auxilio-doenca', 'prorrogacao-auxilio-doenca', 'inss-negou-quem-paga-salario'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='valor-auxilio-doenca',
        hub='auxilio-doenca-negado',
        crumb='Valor do auxílio-doença',
        title='Valor do auxílio-doença: como o INSS calcula em 2026',
        seo='Valor do Auxílio-Doença em 2026: Como o INSS Calcula',
        desc='Como o INSS calcula o valor do auxílio-doença em 2026: 91% da média, o limite da média dos últimos 12 salários, piso, teto, 13º e um exemplo de cálculo.',
        lead='O auxílio-doença quase nunca é igual ao salário. Veja de onde vem o número, por que ele costuma ser menor e quando vale conferir o cálculo.',
        answer=f'O auxílio-doença é de <strong>91% do salário de benefício</strong>, que é a média de todos os salários de contribuição desde julho de 1994. Mas ele <strong>não pode passar da média dos últimos 12 salários</strong>. Em 2026, o valor mínimo é {SM} e o máximo, {TETO}. Quem recebe tem direito a 13º proporcional.',
        secoes=[
            ('O cálculo em três passos', '''
<ol class="steps-l">
<li><strong>Média geral:</strong> o INSS soma todos os salários de contribuição desde julho de 1994, corrigidos, e divide pelo número de meses.</li>
<li><strong>91%:</strong> o benefício é de 91% dessa média.</li>
<li><strong>Limite:</strong> o resultado não pode ser maior que a média dos últimos 12 salários de contribuição. Se for, vale o menor.</li>
</ol>'''),
            ('Exemplo', '''
<div class="table-wrap"><table>
<tr><th></th><th>Valor</th></tr>
<tr><td>Média de todos os salários desde 1994</td><td>R$ 3.000,00</td></tr>
<tr><td>91% da média</td><td>R$ 2.730,00</td></tr>
<tr><td>Média dos últimos 12 salários</td><td>R$ 2.500,00</td></tr>
<tr><td><strong>Valor do auxílio-doença</strong></td><td><strong>R$ 2.500,00</strong> (o menor dos dois)</td></tr>
</table></div>
<p>Quem contribui sobre o salário mínimo, como o MEI, recebe um salário mínimo ({SM} em 2026).</p>'''.replace('{SM}', SM)),
            ('Auxílio-doença por acidente de trabalho', '''
<p>O valor do auxílio acidentário (código B91) é calculado da mesma forma. A diferença está nos direitos que ele traz: a empresa continua depositando o FGTS durante o afastamento, e o empregado tem <strong>estabilidade de 12 meses</strong> depois da alta. Veja <a href="/acidente-de-trabalho/">acidente de trabalho</a>.</p>'''),
            ('Quando conferir o cálculo', '''
<ul>
<li>salários que não aparecem no CNIS ou aparecem com valor menor;</li>
<li>períodos de trabalho com mais de um emprego, cujas contribuições devem ser somadas;</li>
<li>benefício dado como comum (B31) quando a doença tem relação com o trabalho.</li>
</ul>
<p>Erros como esses podem ser corrigidos com pedido de revisão ao INSS. Saiba mais em <a href="/revisao-beneficio-inss/">revisão de benefício do INSS</a>.</p>'''),
        ],
        faq=[
            ('Quem recebe auxílio-doença tem direito ao 13º?', 'Sim. O INSS paga o abono anual proporcional aos meses em que a pessoa recebeu o benefício no ano.'),
            ('O auxílio-doença pode ser menor que o salário mínimo?', 'Não. O valor mínimo é o salário mínimo, R$ 1.621,00 em 2026.'),
            ('Por que meu auxílio-doença é menor que o meu salário?', 'Porque o cálculo usa a média de todos os salários desde 1994, aplica 91% e ainda limita o resultado à média dos últimos 12 salários. Por isso o benefício quase sempre fica abaixo do salário atual.'),
            ('O valor do auxílio-doença do MEI é de quanto?', 'Quem contribui como MEI paga sobre o salário mínimo e, por isso, recebe um salário mínimo de auxílio-doença.'),
        ],
        cta=('Acha que o valor do seu benefício está errado?', 'Salários que faltam no CNIS ou um código de benefício errado mudam o valor.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre o valor do auxílio-doença e quero conferir o meu.',
        rel=['auxilio-doenca-quem-tem-direito', 'prorrogacao-auxilio-doenca'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='prorrogacao-auxilio-doenca',
        hub='auxilio-doenca-negado',
        crumb='Prorrogação do auxílio-doença',
        title='Prorrogação do auxílio-doença: prazo, documentos e negativa',
        seo='Prorrogação do Auxílio-Doença: Prazo e Documentos',
        desc='Como pedir a prorrogação do auxílio-doença no Meu INSS: prazo de 15 dias antes do fim, documentos médicos, se continua recebendo e o que fazer se for negada.',
        lead='O auxílio-doença tem data para acabar. Se você ainda não pode voltar ao trabalho, o pedido de prorrogação precisa ser feito no prazo certo para não ficar sem renda.',
        answer='O pedido de prorrogação deve ser feito nos <strong>15 dias antes da data de cessação</strong> do benefício (DCB), pelo Meu INSS ou pelo telefone 135. Feito no prazo, o benefício, em regra, continua sendo pago até a nova perícia. É preciso apresentar <strong>atestado ou relatório médico atualizado</strong>.',
        secoes=[
            ('Onde ver a data de fim do benefício', '''
<p>A <strong>data de cessação do benefício (DCB)</strong> aparece na carta de concessão e no Meu INSS, em "Extrato de benefício". Anote essa data: o prazo da prorrogação conta a partir dela.</p>'''),
            ('Como pedir', '''
<ol class="steps-l">
<li>Entre no <strong>Meu INSS</strong> e procure "Pedir prorrogação do benefício por incapacidade", ou ligue para o <strong>135</strong>.</li>
<li>Faça o pedido nos <strong>15 dias anteriores</strong> à data de cessação. Antes disso o sistema não aceita; depois, o benefício já terá sido encerrado.</li>
<li>Envie o atestado ou relatório médico atualizado e acompanhe o agendamento da perícia.</li>
</ol>'''),
            ('Documentos médicos', '''
<p>O atestado deve ser <strong>recente</strong> e trazer:</p>
<ul>
<li>o diagnóstico e o CID;</li>
<li>por que você ainda não pode trabalhar na sua função;</li>
<li>o tratamento em andamento e o tempo estimado de afastamento;</li>
<li>nome, CRM e assinatura do médico.</li>
</ul>
<p>Leve também exames e receitas recentes à perícia. Um atestado antigo ou genérico é a causa mais comum de prorrogação negada.</p>'''),
            ('Perdeu o prazo ou a prorrogação foi negada', '''
<p>Se o prazo passou, faça um <strong>novo pedido</strong> de auxílio-doença. Se a prorrogação foi negada, você pode recorrer em 30 dias, fazer novo pedido com documentos melhores ou entrar na Justiça Federal. Veja as opções em <a href="/auxilio-doenca-negado/">auxílio-doença negado</a>.</p>
<p>Se você é empregado e recebeu alta sem conseguir trabalhar, apresente-se à empresa: veja <a href="/blog/inss-negou-quem-paga-salario/">quem paga o salário quando o INSS dá alta</a>.</p>'''),
        ],
        faq=[
            ('Pedi a prorrogação. Continuo recebendo?', 'Em regra, sim: com o pedido feito no prazo, o benefício é mantido até a nova perícia. Acompanhe pelo Meu INSS.'),
            ('Precisa de novo atestado para pedir a prorrogação?', 'Sim. O atestado ou relatório deve ser atualizado e explicar por que a incapacidade continua.'),
            ('Quantas vezes posso pedir prorrogação?', 'Não há limite fixo. Enquanto a incapacidade continuar e for comprovada, a prorrogação pode ser pedida. Se ela for permanente, pode ser o caso de aposentadoria por incapacidade.'),
            ('Posso voltar a trabalhar antes do fim do benefício?', 'Pode, se você se sentir em condições e o médico liberar. O benefício termina quando você volta ao trabalho.'),
        ],
        cta=('A prorrogação foi negada?', 'Ainda há caminhos, com prazos curtos e documentos médicos que precisam ser bem preparados.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre prorrogação do auxílio-doença e preciso de orientação.',
        rel=['auxilio-doenca-quem-tem-direito', 'inss-negou-quem-paga-salario', 'valor-auxilio-doenca'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='inss-negou-quem-paga-salario',
        hub='auxilio-doenca-negado',
        crumb='INSS negou: quem paga?',
        title='INSS deu alta e a empresa não aceita a volta: quem paga o salário?',
        seo='INSS Negou e a Empresa Não Aceita: Quem Paga o Salário?',
        desc='O INSS negou ou cortou o auxílio-doença, mas o médico da empresa diz que você não pode voltar. Entenda o limbo previdenciário e quem paga o salário.',
        lead='É uma situação comum e angustiante: o INSS diz que você pode trabalhar, a empresa diz que não, e o salário não vem de lugar nenhum. Esse impasse tem nome e tem solução.',
        answer='Esse impasse é chamado de <strong>limbo previdenciário</strong>. A Justiça do Trabalho entende, em regra, que depois da alta do INSS o empregado volta a estar à disposição da empresa: se ela não aceita o retorno, <strong>deve pagar os salários</strong> ou colocá-lo numa função compatível. O empregado precisa se apresentar à empresa e, ao mesmo tempo, pode recorrer da decisão do INSS.',
        secoes=[
            ('Por que acontece', '''
<p>Quando o INSS nega ou encerra o auxílio-doença, considera que você pode trabalhar. Mas o <strong>médico do trabalho</strong> da empresa, no exame de retorno, pode considerar você inapto. O resultado é ficar sem benefício e sem salário.</p>'''),
            ('O que a Justiça do Trabalho decide', '''
<p>O entendimento predominante é que, com a alta do INSS, o contrato de trabalho volta a valer por inteiro. Se a empresa impede a volta, o risco é dela: precisa <strong>pagar os salários</strong> do período ou <strong>readaptar</strong> o empregado numa função que ele consiga exercer. Cada caso depende das provas, mas a empresa não pode simplesmente deixar o empregado em casa sem pagamento.</p>'''),
            ('O que fazer, passo a passo', '''
<ol class="steps-l">
<li><strong>Apresente-se à empresa</strong> logo após a alta, de preferência por escrito (e-mail, mensagem ou carta com protocolo), e peça o exame de retorno.</li>
<li><strong>Guarde provas</strong>: o ASO de retorno, mensagens e qualquer documento em que a empresa recuse o seu trabalho.</li>
<li><strong>Recorra da decisão do INSS</strong> em até 30 dias ou faça novo pedido, com laudos atualizados. Veja <a href="/auxilio-doenca-negado/">auxílio-doença negado</a>.</li>
<li><strong>Cobre os salários</strong>: se a empresa recusar o retorno e não pagar, os salários podem ser cobrados na Justiça do Trabalho, e a falta de pagamento pode justificar a <a href="/rescisao-indireta/">rescisão indireta</a>.</li>
</ol>'''),
            ('Cuidado com as faltas', '''
<p>Não deixe de se apresentar à empresa por achar que não está bem. Ficar mais de 30 dias sem comparecer nem justificar, depois da alta, pode ser tratado como <strong>abandono de emprego</strong>, que é motivo de justa causa. Se o seu médico diz que você não pode trabalhar, entregue o atestado à empresa e faça novo pedido ao INSS.</p>'''),
        ],
        faq=[
            ('O que é limbo previdenciário?', 'É a situação do empregado que recebeu alta do INSS, mas foi considerado inapto pelo médico da empresa, e fica sem benefício e sem salário.'),
            ('A empresa pode me mandar para casa sem salário depois da alta do INSS?', 'Em regra, não. Se a empresa não aceita o retorno, a Justiça do Trabalho costuma entender que ela deve pagar os salários ou oferecer uma função compatível.'),
            ('Recorri ao INSS. Preciso ir trabalhar enquanto isso?', 'Você deve se apresentar à empresa e se colocar à disposição. Se ela recusar, guarde a prova da recusa. O recurso ao INSS segue em paralelo.'),
            ('Posso pedir demissão nessa situação?', 'Pedir demissão faz você perder direitos como multa do FGTS e seguro-desemprego. Se a empresa não paga os salários, o caminho costuma ser a rescisão indireta, que garante as verbas de uma demissão sem justa causa.'),
        ],
        cta=('Está sem benefício e sem salário?', 'O caso envolve o INSS e a empresa ao mesmo tempo, e os prazos dos dois lados correm juntos.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre limbo previdenciário: o INSS me deu alta e a empresa não aceita minha volta.',
        rel=['prorrogacao-auxilio-doenca', 'auxilio-doenca-quem-tem-direito'],
        publicado=D, atualizado=D, publicar=True,
    ),

    # ============================================================ Pensão por morte
    dict(
        slug='pensao-por-morte-tabela-idade',
        hub='pensao-por-morte-natal',
        crumb='Tabela da pensão por morte',
        title='Tabela de idade da pensão por morte: quando ela é vitalícia',
        seo='Tabela de Idade da Pensão por Morte: Quando é Vitalícia',
        desc='Tabela de duração da pensão por morte para viúvo, viúva e companheiro: de 3 anos a vitalícia, conforme a idade. Veja a regra dos 4 meses e as exceções.',
        lead='A pensão por morte do cônjuge nem sempre é para a vida toda. A duração depende da idade do viúvo ou da viúva, do tempo de casamento e das contribuições de quem faleceu.',
        answer='A pensão do cônjuge ou companheiro é <strong>vitalícia quando ele tem 45 anos ou mais</strong> na data do óbito. Abaixo disso, dura de 3 a 20 anos, conforme a idade. Essa tabela só vale se o falecido tinha <strong>18 contribuições</strong> e o casamento ou a união tinha <strong>2 anos</strong>; sem isso, a pensão dura 4 meses, exceto em caso de acidente ou doença do trabalho.',
        secoes=[
            ('A tabela', '''
<div class="table-wrap"><table>
<tr><th>Idade do cônjuge na data do óbito</th><th>Duração da pensão</th></tr>
<tr><td>Menos de 22 anos</td><td>3 anos</td></tr>
<tr><td>22 a 27 anos</td><td>6 anos</td></tr>
<tr><td>28 a 30 anos</td><td>10 anos</td></tr>
<tr><td>31 a 41 anos</td><td>15 anos</td></tr>
<tr><td>42 a 44 anos</td><td>20 anos</td></tr>
<tr><td>45 anos ou mais</td><td>Vitalícia</td></tr>
</table></div>
<p>Idades da Portaria ME 424/2020, válidas para óbitos a partir de 1º de janeiro de 2021. Para óbitos entre 2015 e 2020, as idades eram um ano menores (vitalícia a partir de 44 anos). A idade que conta é a do cônjuge <strong>no dia do óbito</strong>, não no dia do pedido.</p>'''),
            ('Quando a pensão dura só 4 meses', '''
<p>A pensão do cônjuge dura apenas <strong>4 meses</strong> se, na data do óbito:</p>
<ul>
<li>o falecido tinha <strong>menos de 18 contribuições</strong> mensais; ou</li>
<li>o casamento ou a união estável tinha <strong>menos de 2 anos</strong>.</li>
</ul>
<p>Essas exigências não se aplicam quando a morte decorre de <strong>acidente de qualquer natureza</strong> ou de doença do trabalho: nesses casos, vale direto a tabela por idade.</p>'''),
            ('Exceções', '''
<ul>
<li><strong>Cônjuge inválido ou com deficiência:</strong> recebe enquanto durar a invalidez ou a deficiência, respeitados os prazos mínimos da tabela.</li>
<li><strong>Ex-cônjuge que recebia pensão alimentícia:</strong> recebe pelo tempo que restava da pensão alimentícia, se ela tinha prazo; se não tinha, segue a tabela.</li>
<li><strong>Casar de novo</strong> não faz perder a pensão do INSS.</li>
</ul>
<p>A pensão dos filhos segue outra regra: vai até os 21 anos. Veja <a href="/blog/pensao-por-morte-filhos/">pensão por morte para filhos</a>.</p>'''),
            ('E o valor?', '''
<p>A duração não muda o valor. Desde a Reforma da Previdência, a pensão é de 50% da aposentadoria do falecido mais 10% por dependente, até 100%. Os detalhes estão na página de <a href="/pensao-por-morte-natal/">pensão por morte</a>. Se você já é aposentada, veja <a href="/blog/acumular-pensao-e-aposentadoria/">como fica o acúmulo de pensão e aposentadoria</a>.</p>'''),
        ],
        faq=[
            ('Com quantos anos a pensão por morte é vitalícia?', 'Para óbitos a partir de 2021, quando o cônjuge ou companheiro tem 45 anos ou mais na data do óbito, desde que o falecido tivesse 18 contribuições e a união tivesse pelo menos 2 anos.'),
            ('Viúva de 40 anos recebe pensão por quanto tempo?', 'Por 15 anos, se cumpridos os requisitos de 18 contribuições e 2 anos de casamento ou união. Se não, por 4 meses.'),
            ('Se eu casar de novo, perco a pensão?', 'Não. No INSS, um novo casamento ou união não encerra a pensão por morte.'),
            ('A pensão de quem tem 45 anos é vitalícia mesmo com poucos anos de casamento?', 'Precisa de pelo menos 2 anos de casamento ou união e de 18 contribuições do falecido. Sem isso, dura 4 meses, a não ser que a morte tenha sido por acidente ou doença do trabalho.'),
        ],
        cta=('A duração da sua pensão está certa?', 'A data de início da união e as contribuições do falecido mudam o prazo, e o INSS às vezes erra nessa conta.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre a tabela da pensão por morte e quero tirar uma dúvida.',
        rel=['pensao-por-morte-filhos', 'acumular-pensao-e-aposentadoria'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='pensao-por-morte-filhos',
        hub='pensao-por-morte-natal',
        crumb='Pensão por morte para filhos',
        title='Pensão por morte para filhos: até que idade e qual o valor',
        seo='Pensão por Morte para Filhos: Até Que Idade e Valor',
        desc='Pensão por morte para filhos: vai até os 21 anos, regras para filho com deficiência, enteado, prazo de 180 dias para menores de 16 e o valor de cada cota.',
        lead='Quando um pai ou uma mãe que contribuía para o INSS falece, os filhos têm direito à pensão. Veja até quando ela é paga, como é dividida e o prazo para pedir sem perder valores.',
        answer='O filho recebe a pensão por morte <strong>até completar 21 anos</strong>. Se for inválido ou tiver deficiência intelectual, mental ou grave, recebe enquanto durar a condição, sem limite de idade. Cada dependente acrescenta 10% à pensão, e a cota do filho <strong>termina aos 21 anos sem passar para os outros</strong>. Para filhos menores de 16, o pedido feito em até 180 dias garante os valores desde o óbito.',
        secoes=[
            ('Quem são os filhos com direito', '''
<ul>
<li>filhos, inclusive adotivos e os nascidos fora do casamento, até 21 anos;</li>
<li>filhos de qualquer idade inválidos ou com deficiência intelectual, mental ou grave;</li>
<li><strong>enteados e menores sob tutela</strong>, se houver declaração do segurado e prova de dependência econômica.</li>
</ul>
<p>Estar na faculdade <strong>não prorroga</strong> a pensão depois dos 21 anos: o STJ já decidiu que não há essa extensão.</p>'''),
            ('Como fica o valor', '''
<p>A pensão é formada por uma cota familiar de <strong>50%</strong> da aposentadoria do falecido, mais <strong>10% por dependente</strong>, até 100%. O total é dividido em partes iguais entre os dependentes.</p>
<div class="table-wrap"><table>
<tr><th>Dependentes</th><th>Percentual</th></tr>
<tr><td>1 filho</td><td>60%</td></tr>
<tr><td>2 filhos</td><td>70%</td></tr>
<tr><td>Viúva e 2 filhos</td><td>80%</td></tr>
<tr><td>Viúva e 3 filhos</td><td>90%</td></tr>
</table></div>
<p>Quando um filho completa 21 anos, a cota de 10% dele <strong>deixa de existir</strong> e a pensão total diminui. Se houver dependente inválido ou com deficiência grave, a pensão é de 100%.</p>'''),
            ('Prazo para pedir', '''
<p>Para receber desde a data do óbito, o pedido deve ser feito em até <strong>180 dias</strong> para filhos menores de 16 anos e em até <strong>90 dias</strong> para os demais dependentes. Fora desse prazo, a pensão é paga a partir da data do pedido.</p>
<p>O pedido é feito pelo Meu INSS ou pelo 135, pelo responsável legal da criança, com a certidão de óbito, a certidão de nascimento e os documentos de quem faleceu.</p>'''),
            ('Filhos de pais separados', '''
<p>O filho de pai ou mãe separado tem direito à pensão da mesma forma, e ela é dividida com o novo cônjuge ou companheiro do falecido, se houver. Questões sobre bens e herança são tratadas no <a href="/inventario-natal/">inventário</a>.</p>'''),
        ],
        faq=[
            ('Até que idade o filho recebe pensão por morte?', 'Até completar 21 anos. Filho inválido ou com deficiência intelectual, mental ou grave recebe enquanto durar a condição.'),
            ('Filho na faculdade recebe pensão até os 24 anos?', 'Não no INSS. A pensão por morte termina aos 21 anos, mesmo que o filho esteja estudando.'),
            ('Qual o valor da pensão por morte para 2 filhos?', '70% da aposentadoria que o falecido recebia ou teria direito: 50% da cota familiar mais 10% para cada filho, divididos igualmente entre os dois.'),
            ('Neto pode receber pensão por morte do avô?', 'Só se estiver sob tutela do avô e for provada a dependência econômica. A simples guarda ou ajuda financeira, em regra, não basta para o INSS.'),
        ],
        cta=('Ficou com filhos menores depois de uma perda na família?', 'O prazo de 180 dias garante os valores desde o óbito, e os documentos certos evitam atraso.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre pensão por morte para filhos e preciso de orientação.',
        rel=['pensao-por-morte-tabela-idade', 'acumular-pensao-e-aposentadoria', 'bpc-loas-autismo'],
        publicado=D, atualizado=D, publicar=True,
    ),
    dict(
        slug='acumular-pensao-e-aposentadoria',
        hub='pensao-por-morte-natal',
        crumb='Pensão e aposentadoria juntas',
        title='Aposentada pode receber pensão por morte? As regras do acúmulo',
        seo='Pensão por Morte e Aposentadoria: Pode Acumular?',
        desc='Aposentada pode receber pensão por morte do marido? Pode, com redução por faixas. Veja a tabela da Reforma, um exemplo de cálculo e quando não há redução.',
        lead='Receber aposentadoria e pensão por morte ao mesmo tempo é permitido, mas desde a Reforma da Previdência um dos benefícios é pago com desconto. Veja como funciona a conta.',
        answer='Sim. A aposentada pode receber a pensão por morte do marido ou companheiro. Pela Reforma da Previdência, ela recebe <strong>o benefício maior por inteiro</strong> e <strong>parte do menor</strong>, calculada por faixas de salário mínimo. A redução não se aplica se os dois benefícios já existiam, ou se o direito a eles já estava garantido, antes de 13 de novembro de 2019.',
        secoes=[
            ('Como funciona a redução', '''
<p>O benefício de <strong>maior valor</strong> é pago integralmente. O de <strong>menor valor</strong> é pago por faixas, somadas:</p>
<div class="table-wrap"><table>
<tr><th>Faixa do benefício menor</th><th>Quanto recebe</th></tr>
<tr><td>Até 1 salário mínimo</td><td>100%</td></tr>
<tr><td>Entre 1 e 2 salários mínimos</td><td>60%</td></tr>
<tr><td>Entre 2 e 3 salários mínimos</td><td>40%</td></tr>
<tr><td>Entre 3 e 4 salários mínimos</td><td>20%</td></tr>
<tr><td>Acima de 4 salários mínimos</td><td>10%</td></tr>
</table></div>
<p>A regra está no artigo 24 da Emenda Constitucional 103/2019.</p>'''),
            ('Exemplo com valores de 2026', f'''
<p>Aposentadoria de R$ 3.000 e pensão de R$ 2.000. A aposentadoria, maior, é paga inteira. Na pensão:</p>
<ul>
<li>até 1 salário mínimo ({SM}): 100% = R$ 1.621,00;</li>
<li>o que passa disso (R$ 379,00) está na faixa de 1 a 2 salários: 60% = R$ 227,40.</li>
</ul>
<p>A pensão paga fica em <strong>R$ 1.848,40</strong>, e o total recebido, em R$ 4.848,40. Se um dos benefícios acabar ou mudar, o cálculo é refeito e o outro pode voltar a ser pago por inteiro.</p>'''),
            ('Quando não há redução', '''
<ul>
<li>quando os dois benefícios foram concedidos antes de 13 de novembro de 2019;</li>
<li>quando o direito aos dois já estava adquirido nessa data, mesmo que pedidos depois;</li>
</ul>'''),
            ('O que não pode acumular', '''
<ul>
<li><strong>duas pensões de cônjuge</strong> no INSS: fica a mais vantajosa;</li>
<li><strong>BPC/LOAS com pensão ou aposentadoria</strong>: o BPC não pode ser acumulado com outro benefício.</li>
</ul>
<p>A duração da pensão do cônjuge está na <a href="/blog/pensao-por-morte-tabela-idade/">tabela de idade da pensão por morte</a>. A aposentadoria da mulher é explicada em <a href="/blog/aposentadoria-por-idade-mulher/">aposentadoria por idade da mulher</a>.</p>'''),
        ],
        faq=[
            ('Sou aposentada. Posso receber a pensão do meu marido?', 'Pode. Você recebe o benefício de maior valor por inteiro e uma parte do menor, calculada por faixas de salário mínimo.'),
            ('Pensão e aposentadoria de um salário mínimo cada: tem desconto?', 'Não. A primeira faixa, de até um salário mínimo, é paga por inteiro. Quem tem os dois benefícios de um salário mínimo recebe os dois completos.'),
            ('Posso escolher qual benefício recebe por inteiro?', 'O INSS paga por inteiro o mais vantajoso, mas o segurado pode pedir a troca se a situação mudar, por exemplo se um dos benefícios for revisado.'),
            ('Quem recebe BPC pode receber pensão por morte?', 'Não ao mesmo tempo. Com direito à pensão, a pessoa deixa o BPC e passa a receber a pensão, que paga 13º.'),
        ],
        cta=('O INSS aplicou o desconto certo?', 'A data do óbito e a data em que você adquiriu o direito à aposentadoria mudam o cálculo.'),
        wa='Olá, Dra. Thayná! Li o artigo sobre acumular pensão e aposentadoria e quero conferir o meu caso.',
        rel=['pensao-por-morte-tabela-idade', 'aposentadoria-por-idade-mulher', 'pensao-por-morte-filhos'],
        publicado=D, atualizado=D, publicar=True,
    ),
]
