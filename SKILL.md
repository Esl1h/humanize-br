---
name: humanize-br
description: |
  Reescreve textos com "sotaque de robô" para soarem como uma pessoa de verdade
  escreveu, sem mudar o que foi dito, ou aponta cada indício de IA sem
  reescrever nada. Use ao editar ou revisar textos em português com clichês de
  IA, discurso de vendas, fontes vagas, estrutura repetitiva, palavras
  batidas, voz passiva, preenchimento ou sobras de chatbot. Baseado nos 35
  padrões de "Signs of AI writing" da Wikipédia e nos padrões do projeto No AI
  Slop, adaptados para o português do Brasil.
license: MIT
metadata:
  version: "1.0.0"
---

# Humanize BR: elimine o sotaque de robô do seu texto

Reescreva texto com cara de IA para soar como quem escreveu de verdade, não um chatbot. Não mude o que o texto diz nem invente detalhes.

Os padrões abaixo vêm de duas fontes em inglês, adaptadas para o português: a lista ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipédia, mantida pela WikiProject AI Cleanup, e os padrões do projeto [No AI Slop](https://github.com/petergyang/no-ai-slop), de Peter Yang. Nenhuma tradução literal resolve sozinha: um texto gerado por IA em português tem vícios próprios (calões, travessões, anglicismos, aspas), então cada padrão foi reescrito com exemplos e ressalvas para o nosso idioma.

## Os dois modos

**Editar (padrão).** A pessoa envia um texto para corrigir. Faça a menor edição eficaz seguindo as regras abaixo e devolva o texto editado mais uma seção **O que mudou**.

**Detectar.** A pessoa pergunta se um texto tem cara de IA, ou pede para auditar, escanear ou apontar problemas sem reescrever. Nomeie cada padrão desta skill que aparece, cite o trecho exato e sugira o ajuste em poucas palavras. Não reescreva, não dê nota ao texto e não afirme quem o escreveu. Detectores de IA chutam; padrões nomeados são evidência que a pessoa pode conferir com os próprios olhos. Ofereça a edição depois de mostrar os achados.

## O que fazer

Ao receber um texto para humanizar:

1. **Encontre os padrões de IA.** Compare o texto com os padrões listados abaixo.
2. **Preserve cada afirmação.** Você pode encurtar trechos fracos, expandir trechos úteis e juntar ou separar parágrafos. Mantenha a informação mesmo quando mudar a estrutura.
3. **Não invente fatos.** Não acrescente fato, nome, número, data, citação ou referência que não venha da fonte ou de quem pediu a edição. Se uma frase precisar de um detalhe que falta, pergunte por ele ou use uma frase mais simples. Você pode acrescentar uma opinião ou reação quando a voz de quem escreve pedir isso, mas não pode acrescentar uma alegação factual. Ficção é exceção, porque inventar detalhes faz parte da tarefa.
4. **Combine com a voz certa.** Use o tom adequado ao texto, seja formal, informal ou técnico. Só acrescente personalidade quando o texto e quem escreve pedirem por isso.

O tipo de entrada define o que você devolve. Veja [Como devolver o resultado](#como-devolver-o-resultado). Use o mesmo processo de reescrita em qualquer modo.

## Combine com a voz de quem escreve

Se a pessoa enviar uma amostra da própria escrita, analise antes de reescrever:

1. Leia a amostra primeiro. Note o tamanho das frases, o vocabulário, o jeito de abrir parágrafos, a pontuação, as expressões repetidas e as transições.
2. Reproduza esses hábitos. Não troque palavras informais por formais nem apague cacoetes deliberados.
3. Sem amostra, use a orientação abaixo.

Uma amostra de escrita tem prioridade sobre estas regras de estilo. Se a amostra usa travessões com frequência, mantenha a mesma proporção. Não trate o padrão 14 como proibição automática.

## Dê personalidade só quando fizer sentido

Tirar os padrões de IA é só metade do trabalho. O resultado ainda precisa soar como uma pessoa.

Use personalidade em posts de blog, ensaios, opiniões e textos pessoais quando isso combinar com quem escreveu. Mantenha textos de referência, técnicos, jurídicos e factuais neutros. Não acrescente opinião ou primeira pessoa onde isso não pertence.

Quando a personalidade fizer sentido, preserve as opiniões, incertezas, sentimentos contraditórios, humor, digressões e ritmo irregular de quem escreveu. Nunca invente fatos só para o texto parecer mais pessoal.

## Princípios de edição

- **Preserve a voz real de quem escreveu.** Primeiro observe o vocabulário, o ritmo, a franqueza, o humor, a incerteza, as digressões e o nível de polimento do rascunho. Mantenha os traços que soam pessoais. Não deixe todo parágrafo igualmente arrumado nem reescreva frases fortes só por uniformidade.
- **Faça a menor edição eficaz.** Corrija padrões de IA, erros, repetição e trechos confusos. Não mexa em frases humanas que já funcionam. Um rascunho torto com voz de verdade deve continuar soando como a mesma pessoa depois de editado.
- **Vá direto ao ponto quando a introdução não acrescenta nada.** Corte introduções genéricas. Mantenha um relato pessoal, uma história ou uma confissão quando isso cria contexto, tensão ou personagem.
- **Adiante a conclusão só quando isso ajuda a leitura.** Coloque a conclusão logo no início quando isso facilita o entendimento. Não force toda seção e todo parágrafo no mesmo molde de "conclusão, detalhe, contexto".
- **Preserve o sentido de quem escreveu.** Não invente alegações, exemplos, números ou opiniões. Se algo estiver pouco claro, pergunte.
- **Abra o texto, não o simplifique demais.** Mantenha a substância, a nuance e a precisão. Corte só o que dificulta a leitura: jargão, frases longas, substantivos abstratos e estrutura emaranhada.
- **Use voz ativa.** "O time lançou na terça" é melhor que "a decisão foi tomada". Não deixe coisas inanimadas fazerem verbos de gente.
- **Faça cada frase merecer seu lugar.** Corte qualificadores vazios e introduções que só atrasam o ponto. Mantenha expressões como "acho que", "talvez" ou "para ser sincero" quando exprimem incerteza real, autoconsciência ou o ritmo de fala de quem escreveu.
- **Desembarace frases sem achatar o ritmo.** Separe frases e parágrafos genuinamente difíceis de acompanhar. Mantenha frases longas de fala, fragmentos e mudanças de ritmo quando são claras e características de quem escreveu.
- **Seja concreto e específico.** Abstração é onde o texto vai morrer. "A integração melhorou a eficiência" vira "a integração cortou o tempo de deploy de 40 para 4 minutos." Nomes, números, datas, mecanismos e exemplos valem mais que abstrações.
- **Use o teste da portabilidade.** Se uma frase pudesse ser colada, sem mudar nada, no texto de outra pessoa, empresa, país ou produto, ela provavelmente é enchimento. Corte ou troque por um fato, exemplo, mecanismo, consequência ou julgamento específico deste assunto.
- **Mostre, não diga o que a pessoa deve pensar.** Deixe os fatos, as ações, os exemplos e as consequências carregarem a ênfase. Corte comentários que rotulam um ponto como importante, surpreendente, sutil ou óbvio em vez de demonstrar por quê. Se o texto ao redor já mostra o ponto, confie na leitora e apague o comentário.
- **Proteja o fato específico.** Não dissolva um detalhe útil numa importância genérica. "A ferramenta melhora bastante a produtividade da equipe" vira "a ferramenta cortou o tempo de revisão de 30 para 8 minutos".
- **Deixe os verbos trabalharem.** Troque locuções verbais fracas por verbos diretos. "Tomou a decisão de" vira "decidiu". "Tem a capacidade de" vira "pode".
- **Saiba qual é a tarefa do texto.** Antes de mexer em estrutura ou vocabulário, entenda o que o texto quer fazer e para quem é.
- **Preserve a aspereza e o caráter úteis.** Mantenha opiniões fortes, linguagem direta, humor, palavrão, autointerrupções e confissões honestas quando pertencem a quem escreveu. Não troque por uma versão mais segura ou mais "profissional".
- **Mantenha a estrutura, a não ser que ela atrapalhe.** Preserve a progressão e os desvios de quem escreveu quando carregam personalidade. Se reorganizar, explique o porquê na seção O que mudou.

## Palavras e expressões vigiadas

Banidas de cara: mergulhar (no sentido de "delve"), fomentar, alavancar, viabilizar, capacitar/empoderar, utilizar (quando "usar" já resolve), robusto, de ponta, cutting-edge, mudança de paradigma, divisor de águas, "isso muda tudo", "isso é gigante", tapeçaria (metafórico), no reino/âmbito de (metafórico), multifacetado, meticuloso, intrincado, primordial, transformador, elevar (metafórico), embarcar nessa jornada, turbinar, potencializar ao extremo, em constante evolução, disruptivo, sinergia, holístico.

Advérbios costumeiramente vazios: apenas, literalmente (fora do sentido literal), sinceramente, honestamente, simplesmente, verdadeiramente, fundamentalmente, importantemente, crucialmente, inerentemente, inevitavelmente. Corte quando não acrescentam nada. Mantenha quando carregam ênfase, incerteza, contraste ou o ritmo natural de fala de quem escreveu.

Frases costumeiramente vazias: vale ressaltar que, é importante notar que, cabe destacar que, no final das contas, quando se trata de, no fundo, no mundo de hoje, na era de, no universo de, a real é que, a verdade é que, em termos de, no que diz respeito a, a fim de, daqui para frente, neste artigo, vamos mergulhar nisso, vamos explorar. Corte quando atrasam o ponto. Mantenha uma frase ocasional quando fizer parte da voz reconhecível de quem escreveu e a frase ainda merecer seu lugar.

## Padrões de texto com cheiro de IA

### Padrões de conteúdo

#### 1. Importância inflada e falso legado

**Palavras vigiadas:** serve/atua como, é um testemunho/lembrete, papel vital/significativo/crucial/fundamental, sublinha/reforça sua importância, reflete uma tendência mais ampla, simbolizando seu caráter duradouro/perene, contribuindo para, preparando o terreno para, marcando/moldando, representa uma virada, momento decisivo, panorama em evolução, ponto focal, marca indelével, profundamente enraizado

**Problema:** texto gerado por IA costuma afirmar que um detalhe comum marca uma virada histórica, prova um legado ou reflete uma tendência ampla.

**Antes:**
> O Instituto Brasileiro de Geografia e Estatística foi criado em 1936, marcando um momento decisivo na evolução da estatística nacional e consolidando-se como um pilar fundamental da administração pública brasileira.

**Depois:**
> O IBGE foi criado em 1936, dentro de um movimento mais amplo de centralização das estatísticas públicas no Brasil.

#### 2. Citação de nomes para provar importância

**Palavras vigiadas:** cobertura independente, veículos de mídia local/regional/nacional, escrito por um especialista renomado, presença ativa nas redes sociais

**Problema:** texto gerado por IA costuma listar veículos famosos ou número de seguidores para provar que alguém é relevante. A lista geralmente não dá contexto útil.

**Antes:**
> Suas opiniões já foram citadas pela Folha de S.Paulo, O Globo, Estadão e BBC Brasil. Ela mantém um perfil ativo nas redes sociais, com mais de 500 mil seguidores.

**Depois:**
> Suas opiniões já foram citadas pela Folha de S.Paulo e pela BBC Brasil.

Se a fonte explicar o que a pessoa disse e onde, mantenha essa citação útil. Não invente contexto para uma versão mais curta.

#### 3. Análise rasa com gerúndio

**Palavras vigiadas:** destacando/reforçando/enfatizando..., garantindo..., refletindo/simbolizando..., contribuindo para..., cultivando/fomentando..., abrangendo..., evidenciando...

**Problema:** texto gerado por IA costuma grudar um gerúndio numa frase simples para fazer um fato parecer mais profundo do que é.

**Antes:**
> A paleta de cores do templo, em azul, verde e dourado, dialoga com a paisagem da região, simbolizando a conexão da comunidade com a terra e reforçando sua identidade cultural.

**Depois:**
> O templo é pintado em azul, verde e dourado, cores que remetem à paisagem local.

#### 4. Linguagem de vendas

**Palavras vigiadas:** conta com um(a), vibrante, rico (no sentido figurado), profundo, aninhado(a), no coração de, inovador (no sentido figurado), renomado, deslumbrante, imperdível, encantador, de tirar o fôlego

**Problema:** texto gerado por IA costuma soar como propaganda, principalmente ao descrever lugares, cultura, produtos ou organizações.

**Antes:**
> Aninhada no coração das montanhas, Monte Verde encanta os visitantes com sua atmosfera acolhedora, paisagens de tirar o fôlego e uma rica herança cultural que a torna um destino imperdível.

**Depois:**
> Monte Verde fica na Serra da Mantiqueira, a cerca de 1.500 metros de altitude.

#### 5. Fontes vagas e autoridade genérica

**Palavras vigiadas:** especialistas acreditam, segundo relatórios do setor, observadores apontam, alguns críticos argumentam, diversas fontes/publicações (quando poucas são citadas), estudos mostram, é amplamente reconhecido que

**Problema:** texto gerado por IA costuma atribuir uma afirmação a especialistas, relatórios ou observadores sem nome.

**Antes:**
> Devido às suas características únicas, o rio desperta o interesse de pesquisadores e ambientalistas. Especialistas acreditam que ele desempenha um papel crucial no ecossistema da região.

**Depois:**
> Pesquisadores da UFMG estudam o rio há oito anos por causa da fauna endêmica que ele abriga.

Cite uma fonte real quando o texto original tiver uma. Caso contrário, remova a alegação sem apoio. Nunca invente uma fonte.

#### 6. Seções formulaicas de "desafios e perspectivas"

**Palavras vigiadas:** apesar de seus desafios..., apesar de enfrentar dificuldades típicas de..., desafios e legado, perspectivas futuras, segue prosperando

**Problema:** textos de IA costumam acrescentar uma seção padrão sobre desafios, perspectivas futuras ou crescimento contínuo. Essas seções em geral repetem alegações vagas em vez de trazer fatos.

**Antes:**
> Apesar de sua prosperidade industrial, o bairro enfrenta desafios típicos de áreas urbanas, como trânsito intenso e escassez de água. Ainda assim, graças à sua localização estratégica e às iniciativas em andamento, segue prosperando como parte essencial do crescimento da cidade.

**Depois:**
> O bairro tem trânsito recorrente e falta de água em períodos de seca.

Acrescente detalhes como datas ou ações públicas só quando vierem da fonte ou de quem pediu a edição.

### Padrões de linguagem e gramática

#### 7. Palavras de IA superusadas

**Palavras de alta frequência em IA:** ademais, outrossim, no cenário atual, panorama (em sentido abstrato), mergulhar (delve), robusto, essencial, crucial, primordial, fundamental (empilhados na mesma frase), sinergia, holístico, tapeçaria (metafórico), testemunho, sublinha/reforça (verbo), intrincado, multifacetado, jornada (metafórico), protagonismo, empoderar, fomentar, viabilizar, alavancar, engajamento, expertise, insights, disruptivo, corroborar, concomitantemente

**Problema:** texto de IA usa essas palavras com frequência muito maior do que a maioria das pessoas, principalmente em grupo.

**Antes:**
> Ademais, um traço marcante da culinária baiana é o uso do azeite de dendê. É um testemunho duradouro da herança africana que essa iguaria permaneça tão presente no panorama gastronômico local.

**Depois:**
> A culinária baiana também usa muito azeite de dendê, herança da culinária africana que chegou com o povo escravizado trazido para a Bahia.

#### 8. Evitar "ser", "estar" e "ter"

**Palavras vigiadas:** serve como, atua como, funciona como, representa, conta com, ostenta, apresenta

**Problema:** texto de IA costuma trocar verbos simples como *ser*, *estar* e *ter* por locuções mais longas.

**Antes:**
> O espaço serve como área de exposições da galeria e conta com mais de 300 metros quadrados, além de ostentar pé-direito duplo.

**Depois:**
> O espaço é a área de exposições da galeria, tem 300 metros quadrados e pé-direito duplo.

#### 9. "Não é só X, é Y" e contrastes binários forçados

**Problema:** texto de IA abusa de formas como "não é só sobre X, é sobre Y" e "a questão não é X, é Y", dentro da frase ou como duas frases separadas.

**Antes:**
> Não é só sobre a batida por baixo do vocal, é sobre a atmosfera inteira da música. Não é apenas uma canção, é um manifesto.

**Depois:**
> A batida pesada reforça o clima agressivo da faixa.

**Antes (contraste em duas frases):**
> A pergunta não é se o modelo é bom. É se a avaliação é boa.

**Depois:**
> A avaliação importa mais do que o modelo.

#### 10. Grupos forçados de três

**Problema:** texto de IA costuma empurrar ideias para grupos de três só para parecer completo.

**Antes:**
> O evento reúne palestras, mesas redondas e momentos de networking. Os participantes podem esperar inovação, inspiração e insights valiosos.

**Depois:**
> O evento tem palestras e mesas redondas, além de um tempo livre para conversar entre uma sessão e outra.

#### 11. Trocar nomes e repetir o início das frases

**Problema:** texto de IA trata a repetição por regra, não por ouvido. Pode ficar renomeando a mesma pessoa ou coisa. Também pode começar várias frases pelo mesmo sujeito, quase sempre "ela" ou "ele".

Use um nome claro para o mesmo sujeito. Para aberturas repetidas, junte as frases, troque o sujeito quando ajudar, ou comece pela ação.

**Antes (troca de nomes):**
> O protagonista enfrenta diversos desafios. O personagem principal precisa superar obstáculos. A figura central finalmente triunfa. O herói volta para casa.

**Depois:**
> O protagonista enfrenta diversos desafios, mas no fim triunfa e volta para casa.

**Antes (aberturas repetidas):**
> Ela reparou na porta. Ela reparou na fechadura. Ela guardou os dois detalhes.

**Depois:**
> Ela reparou na porta e na fechadura, e guardou os dois detalhes.

Não proíba a palavra repetida. Corrija o padrão de frase repetida. A frase que sobrar ainda pode começar com "Ela".

#### 12. Falsos intervalos "de X a Y"

**Problema:** texto de IA costuma usar "de X a Y" quando X e Y não formam um intervalo de verdade.

**Antes:**
> Nossa jornada pelo universo nos levou da singularidade do Big Bang à intrincada teia cósmica, do nascimento e morte das estrelas à dança enigmática da matéria escura.

**Depois:**
> O livro aborda o Big Bang, a formação das estrelas e as teorias atuais sobre a matéria escura.

#### 13. Voz passiva e sujeito oculto

**Problema:** texto de IA costuma esconder quem age ou apagar o sujeito. Use a voz ativa quando isso deixar o agente e a ação mais claros.

**Antes:**
> Nenhum arquivo de configuração é necessário. Os resultados são preservados automaticamente.

**Depois:**
> Você não precisa de um arquivo de configuração. O sistema preserva os resultados automaticamente.

### Padrões visuais e de formatação

#### 14. Travessões em excesso

**Regra:** a versão final não deve usar travessão (—) como muleta de ritmo em prosa expositiva, a não ser que a amostra de quem escreve já use bastante. Troque por ponto, vírgula, dois-pontos ou parênteses, ou reescreva a frase. Vale também para travessão espaçado ( — ) e para hífen duplo (--) usado como travessão.

**Importante:** isso não vale para o travessão de fala em diálogos de ficção ("— Não vou, disse ela."), que é convenção legítima e comum no português. O alvo aqui é o travessão usado como pausa dramática ou aposto decorativo em texto corrido, não a marcação de fala.

**Antes:**
> O termo é usado principalmente por instituições holandesas — não pelo povo em si. Ninguém diz "Países Baixos, Europa" como endereço — mas esse erro persiste — até em documentos oficiais.

**Depois:**
> O termo é usado principalmente por instituições holandesas, não pelo povo em si. Ninguém diz "Países Baixos, Europa" como endereço, mas esse erro persiste, até em documentos oficiais.

Antes de devolver a reescrita, procure por "—" e "–". Remova cada um, a não ser que a amostra de quem escreve use essa marca. Nesse caso, mantenha a mesma proporção da amostra.

#### 15. Excesso de negrito

**Problema:** chatbots de IA costumam colocar palavras e frases em negrito sem motivo claro.

**Antes:**
> O modelo combina **OKRs (Objetivos e Resultados-Chave)**, **KPIs (Indicadores de Desempenho)** e ferramentas visuais como o **Business Model Canvas (BMC)**.

**Depois:**
> O modelo combina OKRs, KPIs e ferramentas visuais como o Business Model Canvas.

#### 16. Listas com mini-títulos em negrito

**Problema:** texto de IA costuma usar listas verticais em que todo item começa com um rótulo em negrito seguido de dois-pontos.

**Antes:**
> - **Experiência do usuário:** a experiência foi bastante melhorada com uma nova interface.
> - **Desempenho:** o desempenho foi otimizado com algoritmos mais eficientes.
> - **Segurança:** a segurança foi reforçada com criptografia de ponta a ponta.

**Depois:**
> A atualização melhora a interface, deixa o carregamento mais rápido graças a algoritmos mais eficientes, e acrescenta criptografia de ponta a ponta.

#### 17. Capitalização indevida em títulos

**Problema:** chatbots de IA às vezes capitalizam Toda Palavra Principal De Um Título, um hábito importado do inglês que não é a convenção do português.

**Antes:**
> ## Negociações Estratégicas E Parcerias Globais

**Depois:**
> ## Negociações estratégicas e parcerias globais

#### 18. Emojis decorativos

**Problema:** chatbots de IA costumam acrescentar emojis a títulos e itens de lista como decoração.

**Antes:**
> 🚀 **Fase de lançamento:** o produto estreia no terceiro trimestre
> 💡 **Insight principal:** os usuários preferem simplicidade
> ✅ **Próximos passos:** agendar reunião de acompanhamento

**Depois:**
> O produto estreia no terceiro trimestre. A pesquisa com usuários mostrou preferência por simplicidade. Próximo passo: agendar uma reunião de acompanhamento.

#### 19. Consistência de aspas

**Importante:** diferente do inglês, no português as aspas curvas (" ") são o padrão tipográfico correto em texto formal, não um indício de IA. Não troque aspas curvas por aspas retas só por costume herdado do inglês.

**Problema real:** o indício de IA aqui é misturar aspas retas (" ") e curvas (" ") no mesmo texto, ou aninhar aspas duplas dentro de aspas duplas quando o padrão editorial pede aspas simples (' ') para a citação interna.

**Antes:**
> Ela disse "que "tudo estava pronto"", mas depois voltou atrás.

**Depois:**
> Ela disse "que 'tudo estava pronto'", mas depois voltou atrás.

Escolha um padrão de aspas para o documento inteiro e mantenha-o.

### Padrões de chatbot

#### 20. Sobras de texto de chatbot na resposta

**Palavras vigiadas:** espero que isso ajude, claro!, com certeza!, você está certíssimo!, quer que eu..., posso continuar?, me avise se, aqui está um(a)...

**Problema:** às vezes a saudação, a oferta ou o encerramento de um chatbot fica no meio de um texto que deveria valer por si só.

**Antes:**
> Aqui está um resumo da Revolução Francesa. Espero que isso ajude! Me avise se quiser que eu aprofunde algum trecho.

**Depois:**
> A Revolução Francesa começou em 1789, quando a crise financeira e a escassez de alimentos provocaram uma onda de revoltas.

#### 21. Ressalvas de limite de conhecimento e chutes disfarçados

**Palavras vigiadas:** até [data], de acordo com as informações disponíveis, embora detalhes específicos sejam escassos..., não é de conhecimento público, prefere manter a vida pessoal em sigilo, provavelmente [cresceu/estudou/começou], acredita-se que

**Problema:** um modelo pode dizer que não achou uma fonte e, na sequência, preencher a lacuna com um palpite plausível. Diga o que a fonte não mostra, ou apague a frase. Nunca apresente um palpite como fato.

**Antes (ressalva de limite de conhecimento):**
> Embora detalhes específicos sobre a fundação da empresa não estejam amplamente documentados nas fontes disponíveis, tudo indica que ela tenha sido criada em algum momento da década de 1990.

**Depois:**
> A data de fundação da empresa não consta nas fontes disponíveis. (Ou corte a frase. Cite uma data só se houver fonte.)

**Antes (chute disfarçado):**
> Não há informações públicas sobre sua vida pregressa, o que sugere que ela prefere manter os detalhes pessoais em sigilo. Provavelmente cresceu em uma família de classe média, o que teria moldado seu interesse por educação.

**Depois:**
> A vida pregressa dela não está documentada nas fontes disponíveis. (Ou omita a seção.)

#### 22. Tom exageradamente condescendente

**Problema:** assistentes de IA costumam elogiar quem pergunta ou concordar antes de responder.

**Antes:**
> Ótima pergunta! Você está certíssimo ao dizer que esse é um tema complexo. Esse é um ponto excelente sobre os fatores econômicos.

**Depois:**
> Os fatores econômicos que você citou são relevantes aqui.

### Preenchimento, ressalvas e finais

#### 23. Frases de preenchimento

**Antes → Depois:**
- "a fim de atingir esse objetivo" → "para atingir esse objetivo"
- "devido ao fato de que estava chovendo" → "porque estava chovendo"
- "neste momento" → "agora"
- "no caso de você precisar de ajuda" → "se precisar de ajuda"
- "o sistema tem a capacidade de processar" → "o sistema pode processar"
- "é importante notar que os dados mostram" → "os dados mostram"

#### 24. Excesso de qualificadores

**Frases vigiadas:** para ser justo, também é possível, poderia potencialmente, talvez possa se argumentar, em alguns casos pode ser que, isso é uma inferência

**Problema:** edições sucessivas podem empilhar um qualificador atrás do outro até toda alegação soar incerta. Mantenha um qualificador só quando a fonte apoiar e o sentido pedir. Remova ressalvas que só consertam um exagero anterior.

**Antes:**
> Poderia potencialmente se argumentar que a política talvez tenha algum tipo de efeito possível sobre os resultados.

**Depois:**
> A política pode afetar os resultados.

#### 25. Finais genéricos e conclusões vazias

**Problema:** texto de IA costuma terminar com otimismo vago em vez do último fato útil, ou com um parágrafo de recapitulação que só repete o que já foi dito.

**Antes (final genérico):**
> O futuro é promissor para a empresa. Tempos empolgantes estão por vir, à medida que ela continua sua jornada rumo à excelência. Isso representa um passo importante na direção certa.

**Depois:**
> (Corte o parágrafo. Termine no último fato concreto, não numa despedida. Se a fonte tiver planos reais, use-os.)

**Antes (recapitulação):**
> Em suma, discutimos os principais pontos do projeto. Como vimos, a integração trouxe diversos benefícios para a equipe.

**Depois:**
> (Corte o parágrafo de recapitulação. Termine no ponto concreto mais recente ou numa próxima ação.)

### Anglicismos e hifenização

#### 26. Jargão em inglês hifenizado sem necessidade

**Palavras vigiadas:** data-driven, customer-centric, cutting-edge, state-of-the-art, hands-on, mindset, insights acionáveis

**Problema:** o português não forma pares de adjetivo com hífen do mesmo jeito que o inglês. Quando um texto em português importa esse hábito ao pé da letra, ou usa o termo em inglês sem necessidade quando existe equivalente natural, isso é tanto anglicismo quanto indício de texto gerado por IA (o modelo calca a estrutura do inglês, que é sua língua de treinamento dominante).

**Antes:**
> A equipe é data-driven e trouxe uma abordagem customer-centric para o problema, com uma solução cutting-edge e state-of-the-art.

**Depois:**
> A equipe toma decisões com base em dados e pensa a partir da experiência do cliente. A solução usa a tecnologia mais recente disponível.

Mantenha o termo em inglês quando ele for o nome próprio de uma tecnologia, ferramenta ou conceito técnico sem tradução consagrada (React, machine learning, deploy). O alvo é o jargão corporativo importado sem necessidade, não o vocabulário técnico legítimo.

### Retórica de falsa profundidade

#### 27. Fingir revelar uma verdade mais profunda

**Frases vigiadas:** a questão real é, no fundo, na realidade, o que realmente importa, fundamentalmente, a questão mais profunda, o cerne da questão

**Problema:** texto de IA usa essas frases para fazer um ponto comum soar como uma verdade escondida.

**Antes:**
> A questão real é se os times conseguem se adaptar. No fundo, o que realmente importa é a maturidade da organização.

**Depois:**
> A questão é se os times conseguem se adaptar, o que depende de a organização estar pronta para mudar seus hábitos.

#### 28. Anunciar o próximo ponto em vez de dizer o ponto

**Frases vigiadas:** vamos explorar, vamos mergulhar, vamos entender melhor, aqui está o que você precisa saber, sem mais delongas, e se eu te dissesse que, pense nisso:, pergunta retórica seguida de resposta própria

**Problema:** texto de IA costuma anunciar o próximo ponto em vez de simplesmente afirmá-lo. Remova o anúncio, não só o tom formal dele.

**Antes:**
> Vamos explorar como funciona o cache no Next.js. Aqui está o que você precisa saber.

**Depois:**
> O Next.js guarda dados em cache em várias camadas: memoização de requisição, cache de dados e cache de rota.

**Antes (registro casual):**
> Uma coisa que me pegou desprevenido, então presta atenção nessa parte: o servidor de desenvolvimento do webpack não manda o cabeçalho CORS por padrão.

**Depois:**
> O servidor de desenvolvimento do webpack não manda o cabeçalho CORS por padrão.

#### 29. Título repetido na frase seguinte

**Sinais para observar:** um título seguido de um parágrafo de uma linha que só repete o próprio título antes do conteúdo real começar.

**Antes:**
> ## Desempenho
>
> Velocidade importa.
>
> Quando o usuário encontra uma página lenta, ele sai do site.

**Depois:**
> ## Desempenho
>
> Quando o usuário encontra uma página lenta, ele sai do site.

#### 30. Escrever sobre a versão anterior

**Problema:** documentação e comentários devem descrever o comportamento atual. Mencione a versão anterior só em changelogs, notas de versão, guias de migração e outros documentos sobre mudança.

**Antes:**
> Essa função foi criada para substituir a abordagem antiga de percorrer todos os itens, que causava desempenho O(n²).

**Depois:**
> Essa função usa uma tabela hash para buscas O(1), evitando o custo O(n²) da iteração ingênua.

#### 31. Punchlines forçadas, fragmentos dramáticos e ritmo robótico

**Problema:** texto de IA costuma transformar toda frase numa frase de efeito. Uma frase curta pode reforçar um ponto. Uma fileira de fragmentos curtos geralmente soa forçada, assim como parágrafos com a mesma estrutura repetida sentença após sentença.

**Antes:**
> Então veio o AlphaEvolve. Sem preferência por simetria. Sem viés estético. Sem saudosismo do gosto humano. As regras antigas acabaram.

**Depois:**
> O AlphaEvolve mudou a busca porque não favorecia simetria nem formas parecidas com as humanas, o que tornou algumas suposições antigas menos úteis.

#### 32. Ditados formulaicos de falsa sabedoria

**Palavras vigiadas:** X é a linguagem de Y, X vira uma armadilha, X não é uma ferramenta, é um espelho, a moeda de, a arquitetura de

**Problema:** texto de IA costuma transformar uma alegação comum numa frase de efeito que soa profunda, mas não acrescenta nenhum detalhe. Troque o ditado pela alegação específica.

**Antes:**
> Simetria é a linguagem da confiança. Eficiência vira uma armadilha quando os times esquecem a camada humana.

**Depois:**
> Layouts simétricos costumam parecer mais previsíveis para quem usa o produto. Times podem otimizar demais o processo e perder de vista como as pessoas realmente o utilizam no dia a dia.

#### 33. Aberturas de falsa sinceridade

**Frases vigiadas:** sinceramente?, olha,, a verdade é que, vou ser honesto(a), sejamos sinceros, falando sério, usadas como gancho isolado ou pausa fingida antes de um ponto comum

**Problema:** texto de IA costuma abrir com uma pausa encenada ou uma alegação de honestidade antes de fazer um ponto rotineiro. Diga o ponto direto.

**Antes:**
> Vale o preço? Sinceramente? Depende de quanto você vai usar.

**Depois:**
> Se vale o preço depende de quanto você vai usar.

#### 34. Responder objeções que ninguém levantou

**Frases vigiadas:** isso não é (principalmente/exatamente) sobre, não estou dizendo/argumentando que, para deixar claro, não me leve a mal, isso não quer dizer que, você poderia enquadrar de outro jeito, mas, alguns diriam... mas

**Problema:** texto de IA às vezes responde a uma objeção que não aparece em nenhum outro lugar do texto. Fique atento a uma frase sem atribuição sobre o que quem escreveu não quis dizer, principalmente quando o assunto dela não aparece em mais nenhum lugar. Uma alegação direta como "essa API não é thread-safe" não é esse padrão.

**Antes:**
> Isso não é exatamente sobre o tamanho do prompt, e não estou dizendo que a documentação não importa. Dá para categorizar o problema de outro jeito, mas a questão é se o agente consegue usar a instrução na hora de agir.

**Depois:**
> A questão é se o agente consegue usar a instrução na hora de agir.

Remova só a defesa sem apoio. Se ela tiver uma alegação real, afirme essa alegação direto. Mantenha uma objeção quando o texto citar sua origem ou respondê-la por completo.

#### 35. Rejeitar alternativas falsas

**Frases vigiadas:** uma opção tentadora seria, alguém poderia ser tentado a, uma abordagem óbvia seria, você pode até pensar que... mas, seria fácil simplesmente, alguns sugeririam

**Problema:** texto de IA às vezes apresenta uma opção que nenhuma leitora consideraria, rejeita em uma oração e nunca mais fala nela. Isso costuma ser resto de uma ideia de rascunho esquecida no texto final. Remova a opção falsa e afirme a restrição real direto.

**Antes:**
> Os tokens de sessão são renovados a cada 24 horas. Seria tentador simplesmente reiniciar o serviço de autenticação via cron para renovar tudo de uma vez, mas isso derrubaria todas as sessões ativas. A renovação acontece no próprio lugar, e o cliente atualiza de forma transparente.

**Depois:**
> Os tokens de sessão são renovados a cada 24 horas, no próprio lugar, e o cliente atualiza de forma transparente.

Uma alternativa rejeitada pode ser válida. Várias rejeições curtas e desconexas são um sinal mais forte. Pergunte que informação nova cada frase acrescenta. Se ela só registra uma edição anterior, reescreva o parágrafo em torno do ponto principal.

#### 36. Revelações com dois-pontos

**Problema:** texto de IA gosta de armar uma frase nominal, um dois-pontos, e uma revelação dramática em letra minúscula: "o detalhe que faz tudo funcionar: um agente separado avalia o resultado." Reescreva como frase comum. Use dois-pontos para listas, rótulos e citações, não para drama fingido.

**Antes:**
> O detalhe que faz tudo funcionar: um agente separado avalia o resultado.

**Depois:**
> Um agente separado avalia o resultado, e é isso que faz o sistema funcionar.

#### 37. Metadiscurso interpretativo

**Problema:** texto de IA às vezes sai do assunto para dizer à leitora o que notar, quanto peso dar a algo, ou como interpretar o próprio texto: "isso importa mais do que parece", "o ponto principal é", "como você pode ver", ou um redundante "em outras palavras". Se o ponto já está claro, apague o comentário. Caso contrário, troque por um fato ou apoio que já esteja no conteúdo.

**Antes:**
> Isso importa mais do que parece. Como você pode ver, essa distinção é essencial. Em outras palavras, o processo ficou mais rápido.

**Depois:**
> O processo ficou mais rápido.

#### 38. Slop de formatação

**Problema:** vários padrões de formatação artificial costumam aparecer juntos: emoji em título (padrão 18), negrito espalhado no meio da frase por ênfase (padrão 15), listas de marcadores onde duas frases de prosa ficariam melhores (padrão 16), e cabeçalhos para blocos de duas frases (padrão 29). A formatação deve seguir o conteúdo, não decorá-lo. Ao revisar, pergunte se cada elemento visual carrega informação ou só imita a aparência de um documento organizado.

## O que não sinalizar

### O que não marcar como problema

Uma pessoa de verdade pode usar alguns destes padrões. Não trate nenhum item abaixo como prova isolada:

- **Gramática impecável e estilo consistente.** Muita gente escreve profissionalmente ou já foi revisada por um editor. Polimento não é sinônimo de IA.
- **Mistura de registro formal e informal.** Isso pode refletir a área, a idade ou os hábitos pessoais de quem escreve.
- **Prosa "seca" ou "robótica".** Texto de IA tem sinais *específicos*. Aridez genérica sem esses sinais é só um texto seco.
- **Palavras formais ou acadêmicas.** O padrão 7 lista palavras específicas que a IA usa em excesso. Não simplifique toda palavra formal.
- **Saudação ou despedida de carta num comentário.** Isso é anterior ao ChatGPT em séculos.
- **Conectivos comuns isolados.** "Além disso", "outrossim", "por conseguinte" só denunciam IA quando empilhados. Um "porém" sozinho não é sinal de nada.
- **Aspas curvas sozinhas.** No português, aspas curvas são o padrão editorial correto, não um indício de IA (veja o padrão 19).
- **Travessão sozinho.** Muitos autores e jornalistas usam bastante. Travessão só é evidência quando combinado com o ritmo formulaico de linguagem de vendas.
- **Uma frase curta isolada para dar ênfase.** Só marque fragmentos dramáticos quando vários aparecem em sequência.
- **Repetição proposital de abertura.** Quem escreve pode repetir uma abertura para criar ritmo ou força, como em "Ela veio. Ela viu. Ela venceu." Mude só quando a repetição não acrescentar nada.
- **"Sinceramente" ou "olha" no meio da frase.** Isso é comum em texto informal. O sinal de alerta é a abertura teatral isolada, não a palavra em si.
- **Ressalvas e limites úteis.** Mantenha avisos de escopo, avisos legais e de segurança, correções reais, objeções nomeadas, respostas e perguntas de FAQ.
- **Alternativas reais.** Mantenha opções que uma leitora consideraria de verdade num documento técnico, tutorial ou argumento. Remova só uma opção improvável que o texto descarta e nunca mais usa.
- **Alegações sem fonte.** A maior parte da internet não tem fonte citada. Falta de citação não prova nada sozinha.
- **Formatação correta e complexa.** Editores visuais e templates produzem saída limpa sem qualquer IA envolvida.
- **Texto de segunda mão.** Não reescreva frases vigiadas dentro de citações, títulos, nomes próprios ou exemplos em que a frase está sendo discutida, não usada de verdade.

Na dúvida, procure vários padrões juntos. Um travessão sozinho não prova nada. Vários padrões batidos na mesma passagem são evidência mais forte.

### Detalhes humanos para preservar

Estes detalhes costumam carregar a voz de quem escreveu. Preserve-os a não ser que atrapalhem o sentido:

- **Detalhes específicos e incomuns.** Mantenha um endereço real, uma citação estranha, ou uma frase como "o advogado que trabalhava lá em cima da clínica do meu dentista".
- **Sentimentos contraditórios e tensão não resolvida.** Mantenha frases como "acho que isso é bom na maior parte, mas me incomoda, e não sei explicar direito por quê".
- **Referências datadas, presas a uma época.** Gírias, memes ou piadas internas ligadas a um ano e a um grupo específico. Modelos de IA ficam defasados um ano ou mais.
- **Escolhas deliberadas em primeira pessoa.** Mantenha um corte ou uma escolha de palavra quando quem escreveu conseguir explicar por que ela pertence ao texto.
- **Variação no tamanho das frases.** Texto humano alterna frases curtas e longas. Texto de IA tende a um ritmo parelho, de comprimento médio.
- **Digressões, parênteses e autocorreções genuínas.** "(fico querendo dizer 'quase' aqui, mas era certeza mesmo)". Modelos de IA raramente se interrompem assim.
- **Edições anteriores a 30 de novembro de 2022.** Data do lançamento público do ChatGPT. Qualquer coisa mais antiga, com raras exceções, não foi escrita por IA.

## Como devolver o resultado

**Texto colado (padrão).** Devolva o rascunho, uma lista curta dos padrões de IA que ainda restam, e a reescrita final.

**Modo arquivo.** Quando a pessoa indicar um arquivo, rode o processo de reescrita completo, mas grave só o texto final no arquivo. Mude apenas a prosa. Preserve blocos de código, metadados YAML, dados e destinos de links sem alteração. Depois dê um resumo curto para quem pediu.

**Modo embutido.** Quando outra tarefa usar esta skill para um *pull request*, mensagem de commit ou documento, devolva só o texto final.

**Modo detectar.** Nomeie cada padrão encontrado, cite o trecho exato entre aspas, e sugira o ajuste em poucas palavras. Não reescreva o texto, não dê nota, e não afirme se foi ou não gerado por IA.

## Processo de reescrita e autoverificação

1. Leia a fonte e marque cada padrão de IA.
2. Escreva um rascunho. Leia em voz alta. Confira o ritmo, os detalhes, os verbos simples como *ser* e *ter*, e o nível de formalidade certo.
3. Faça duas perguntas:
   - **"O que ainda soa como texto gerado por IA?"**
   - **"A reescrita acrescentou ou removeu algum fato, nome, número, data, citação, referência, ranking ou outra alegação?"**
   Trate qualquer acréscimo sem apoio ou alegação perdida como erro.
4. Escreva a versão final. Afirme cada ponto com naturalidade em vez de remendar uma frase marcada de cada vez. Se uma frase continuar estranha, reescreva o parágrafo em torno do ponto principal dela. Aplique a regra de travessão do padrão 14.
5. Confira a reescrita contra a lista de verificação em [`eval.md`](eval.md). Se algum item falhar, corrija o texto e confira de novo.

Devolva o resultado no formato exigido em [Como devolver o resultado](#como-devolver-o-resultado).

## Fontes

Esta skill se baseia em duas fontes em inglês, com padrões, exemplos e ressalvas adaptados para o português:

- [Wikipédia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), mantida pela WikiProject AI Cleanup. Seus padrões vêm de revisões de texto gerado por IA na Wikipédia.
- [No AI Slop](https://github.com/petergyang/no-ai-slop), de Peter Yang, que contribuiu os princípios de edição, o modo de detecção e boa parte dos padrões retóricos das seções 26 a 38.

O ponto central da Wikipédia resume o problema: "LLMs usam algoritmos estatísticos para prever o que vem a seguir. O resultado tende ao mais provável estatisticamente, o que se aplica à maior variedade de casos possível." É exatamente esse nivelamento estatístico que esta skill tenta desfazer.
