---
name: humanize-br
description: |
  Reescreve textos em português com "sotaque de robô" para soarem como uma
  pessoa de verdade escreveu, sem mudar o que foi dito, ou aponta cada indício
  de IA sem reescrever nada. Use ao editar ou revisar textos em português com
  clichês de IA, discurso de vendas, fontes vagas, estrutura repetitiva,
  palavras batidas, voz passiva, preenchimento ou sobras de chatbot. Baseado
  nos padrões de "Signs of AI writing" da Wikipédia e nos do projeto No AI
  Slop, adaptados para o português do Brasil. Para texto em inglês, use
  humanize-ai-slop.
license: MIT
metadata:
  version: "1.2.0"
---

# Humanize BR: elimine o sotaque de robô do seu texto

Reescreva texto com cara de IA para soar como quem escreveu de verdade, não um chatbot. Não mude o que o texto diz nem invente detalhes.

Os padrões abaixo vêm de duas fontes em inglês, adaptadas para o português: a lista ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipédia, mantida pela WikiProject AI Cleanup, e os padrões do projeto [No AI Slop](https://github.com/petergyang/no-ai-slop), de Peter Yang. Nenhuma tradução literal resolve sozinha: um texto gerado por IA em português tem vícios próprios (calões, travessões, anglicismos, aspas), então cada padrão foi reescrito com exemplos e ressalvas para o nosso idioma. Revisões posteriores do Humanizer contribuíram os padrões 6 e 24 e as formas ampliadas dos padrões 32 e 40; esta skill mantém a numeração própria por tema.

## Os dois modos

**Editar (padrão).** A pessoa envia um texto para corrigir. Faça a menor edição eficaz seguindo as regras abaixo e devolva o texto editado mais uma seção **O que mudou**.

**Detectar.** A pessoa pergunta se um texto tem cara de IA, ou pede para auditar, escanear ou apontar problemas sem reescrever. Nomeie cada padrão desta skill que aparece, cite o trecho exato e sugira o ajuste em poucas palavras, um achado por linha na ordem do texto:

- **Padrão N (nome):** "trecho exato" → o ajuste em poucas palavras

Termine o relatório com uma linha de resumo: quantos achados, quantos padrões distintos e onde eles se concentram ("9 achados, 6 padrões, a maioria no primeiro e no último parágrafo"). Vários padrões num mesmo trecho são evidência mais forte que um padrão espalhado, então o resumo mostra por onde começar. Leia [`references/patterns.md`](references/patterns.md) antes de escrever o relatório, para que cada achado use o nome e o alcance do catálogo.

Não reescreva, não dê nota ao texto e não afirme quem o escreveu. Detectores de IA chutam; padrões nomeados são evidência que a pessoa pode conferir com os próprios olhos. Quando o texto estiver num arquivo e o scanner embutido estiver disponível, rode `python3 scripts/slop_scan.py <caminho>` primeiro: ele lista os achados mecânicos (palavras banidas, travessões, títulos decorados, emojis, aspas misturadas, listas com rótulo em negrito, anglicismos hifenizados) como `fix`, e as expressões vigiadas (sobras de chatbot, falso insight, preenchimento, contrastes binários, linhas horizontais) como `watch`, cada um com o número do padrão. Confirme ou descarte cada achado `watch` lendo o contexto, e acrescente os padrões retóricos que o scanner não enxerga. Sem o scanner instalado, faça essas checagens à mão. Ofereça a edição depois de mostrar os achados.

## O que fazer

Ao receber um texto para humanizar:

1. **Encontre os padrões de IA.** Compare o texto com o [índice de padrões](#índice-de-padrões).
2. **Preserve cada afirmação.** Você pode encurtar trechos fracos, expandir trechos úteis e juntar ou separar parágrafos. Mantenha a informação mesmo quando mudar a estrutura.
3. **Não invente fatos.** Não acrescente fato, nome, número, data, citação ou referência que não venha da fonte ou de quem pediu a edição. Se uma frase precisar de um detalhe que falta, pergunte por ele ou use uma frase mais simples. Você pode acrescentar uma opinião ou reação quando a voz de quem escreve pedir isso, mas não pode acrescentar uma alegação factual. Ficção é exceção, porque inventar detalhes faz parte da tarefa.
4. **Combine com a voz certa.** Use o tom adequado ao texto, seja formal, informal ou técnico. Só acrescente personalidade quando o texto e quem escreve pedirem por isso.

O tipo de entrada define o que você devolve. Veja [Como devolver o resultado](#como-devolver-o-resultado). Use o mesmo processo de reescrita em qualquer modo.

## O que perguntar

Se a pessoa não tiver enviado um rascunho, peça que cole o texto.

Se o público ou o formato estiver em dúvida e a resposta mudaria a edição, faça uma pergunta só: para quem é este texto e onde ele será publicado? Caso contrário, edite partindo da leitura mais provável e diga qual escolheu.

Se uma frase precisar de um fato que o rascunho não contém, pergunte por ele em vez de inventar.

## Combine com a voz de quem escreve

Se a pessoa enviar uma amostra da própria escrita, analise antes de reescrever:

1. Leia a amostra primeiro. Note o tamanho das frases, o vocabulário, o jeito de abrir parágrafos, a pontuação, as expressões repetidas e as transições.
2. Reproduza esses hábitos. Não troque palavras informais por formais nem apague cacoetes deliberados.
3. Sem amostra, use a orientação abaixo.

Uma amostra de escrita tem prioridade sobre estas regras de estilo. Se a amostra usa travessões com frequência, mantenha a mesma proporção. Não trate o padrão 15 como proibição automática.

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

## Índice de padrões

Cada linha nomeia um padrão e o ajuste habitual. Isso basta para a maioria das edições. Leia [`references/patterns.md`](references/patterns.md) para ver as expressões vigiadas e os exemplos de antes e depois: sempre num relatório de detecção, e sempre que o alcance de um padrão não estiver claro.

### Conteúdo

1. Importância inflada: tire "momento decisivo" e "é um testemunho de"; diga o fato e deixe quem lê julgar.
2. Citação de nomes: troque a lista de veículos ou especialistas pelo que uma fonte nomeada disse de fato.
3. Gerúndio raso: corte orações soltas como "destacando...", "garantindo..." ou transforme em afirmação com fonte.
4. Linguagem de vendas: troque "vibrante", "aninhado", "de tirar o fôlego" por descrição simples.
5. Fontes vagas: nomeie a fonte ou marque a afirmação como sem apoio; nunca invente citação.
6. Conexão vaga: troque "associado a" e "ligado a" pela relação real.
7. Seções formulaicas: corte "apesar dos desafios... segue prosperando"; mantenha só problemas concretos.

### Linguagem e gramática

8. Palavras superusadas: troque as palavras banidas e vigiadas por palavras simples.
9. Evitar ser, estar e ter: "serve como" e "conta com" viram "é" e "tem".
10. Contrastes binários: reescreva "não é X, é Y" e "não A, não B, mas C" como afirmação direta.
11. Grupos de três: mantenha os itens de que o texto precisa, sejam um, dois ou quatro.
12. Troca de nomes: repita o substantivo mais claro em vez de rodar sinônimos; varie o início das frases.
13. Falsos intervalos: tire "de X a Y" quando X e Y não forem pontas de uma escala real.
14. Voz passiva: diga quem agiu.

### Formatação

15. Travessões: troque travessões por vírgula, dois-pontos, parênteses ou frase nova, salvo diálogo ou amostra de quem escreve.
16. Negrito excessivo: tire o negrito que não marca nada que a pessoa precise encontrar.
17. Listas com rótulo em negrito: transforme itens "**Rótulo:** texto" em prosa ou itens simples.
18. Capitalização de títulos: use maiúscula só na primeira palavra e em nomes próprios.
19. Emojis decorativos: tire emojis de títulos e itens de lista.
20. Consistência de aspas: use um estilo de aspas no documento inteiro, de acordo com quem escreve ou o formato de destino.

### Chatbot

21. Sobras de chatbot: apague "espero que isso ajude", "quer que eu...?", "me avise se".
22. Chutes disfarçados: apague ressalvas de limite de treino e palpites apresentados como fato.
23. Tom condescendente: tire "ótima pergunta!" e "você está certíssimo!".
24. Re-explicar contexto: comece pela decisão ou resposta; não repita o que a pessoa já escreveu.

### Preenchimento e finais

25. Frases de preenchimento: corte "a fim de", "vale ressaltar que", "quando se trata de".
26. Qualificadores empilhados: mantenha no máximo uma ressalva honesta.
27. Finais genéricos: termine num ponto concreto ou próximo passo, não em "o futuro é promissor".

### Anglicismos

28. Jargão hifenizado: troque "data-driven", "hands-on" e afins por um equivalente natural quando houver.

### Retórica de falsa profundidade

29. Verdade mais profunda: corte "a questão real é" e "no fundo"; diga o ponto.
30. Anunciar o ponto: corte "vamos mergulhar" e perguntas respondidas pelo próprio texto; diga o ponto.
31. Título repetido: não repita o título na primeira frase.
32. Escrever sobre o documento: descreva o assunto, não o documento nem como ele foi feito.
33. Punchlines forçadas e ritmo robótico: junte fragmentos dramáticos empilhados; varie o tamanho das frases.
34. Ditados formulaicos: apague o fecho de falsa sabedoria em vez de trocar por uma metáfora melhor.
35. Falsa sinceridade: corte "sejamos sinceros" e "a verdade é que" quando servem de gancho.
36. Objeções fantasma: corte "para deixar claro" e "não estou dizendo que" quando ninguém levantou o ponto.
37. Alternativas falsas: corte opções que o texto só levanta para descartar.
38. Revelações com dois-pontos: reescreva "O melhor: ele aprende" como frase simples.
39. Metadiscurso: corte comentários que rotulam um ponto como importante, sutil ou surpreendente.
40. Slop de formatação: tire símbolos decorativos, linhas entre todas as seções e títulos sobre blocos minúsculos.
41. Falso insight: corte "o que ninguém te conta"; deixe a afirmação se sustentar sozinha.

## O que não sinalizar

### O que não marcar como problema

Uma pessoa de verdade pode usar alguns destes padrões. Não trate nenhum item abaixo como prova isolada:

- **Gramática impecável e estilo consistente.** Muita gente escreve profissionalmente ou já foi revisada por um editor. Polimento não é sinônimo de IA.
- **Mistura de registro formal e informal.** Isso pode refletir a área, a idade ou os hábitos pessoais de quem escreve.
- **Prosa "seca" ou "robótica".** Texto de IA tem sinais *específicos*. Aridez genérica sem esses sinais é só um texto seco.
- **Palavras formais ou acadêmicas.** O padrão 8 lista palavras específicas que a IA usa em excesso. Não simplifique toda palavra formal.
- **Saudação ou despedida de carta num comentário.** Isso é anterior ao ChatGPT em séculos.
- **Conectivos comuns isolados.** "Além disso", "outrossim", "por conseguinte" só denunciam IA quando empilhados. Um "porém" sozinho não é sinal de nada.
- **Aspas curvas sozinhas.** No português, aspas curvas são o padrão editorial correto, não um indício de IA (veja o padrão 20).
- **Travessão sozinho.** Muitos autores e jornalistas usam bastante. Travessão só é evidência quando combinado com o ritmo formulaico de linguagem de vendas.
- **Uma frase curta isolada para dar ênfase.** Só marque fragmentos dramáticos quando vários aparecem em sequência.
- **Repetição proposital de abertura.** Quem escreve pode repetir uma abertura para criar ritmo ou força, como em "Ela veio. Ela viu. Ela venceu." Mude só quando a repetição não acrescentar nada.
- **"Sinceramente" ou "olha" no meio da frase.** Isso é comum em texto informal. O sinal de alerta é a abertura teatral isolada, não a palavra em si.
- **Ressalvas e limites úteis.** Mantenha avisos de escopo, avisos legais e de segurança, correções reais, objeções nomeadas, respostas e perguntas de FAQ.
- **Alternativas reais.** Mantenha opções que uma leitora consideraria de verdade num documento técnico, tutorial ou argumento. Remova só uma opção improvável que o texto descarta e nunca mais usa.
- **Dois-pontos antes de uma lista, rótulo ou citação de verdade.** O padrão 38 mira revelações encenadas, não pontuação comum.
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

**Texto colado (padrão).** Devolva a reescrita final seguida de uma seção curta **O que mudou**. Não devolva rascunhos intermediários.

**Modo arquivo.** Quando a pessoa indicar um arquivo, rode o processo de reescrita completo, mas grave só o texto final no arquivo. Mude apenas a prosa. Preserve blocos de código, metadados YAML, dados e destinos de links sem alteração. Depois dê um resumo curto para quem pediu.

**Modo embutido.** Quando outra tarefa usar esta skill para um *pull request*, mensagem de commit ou documento, devolva só o texto final.

**Modo detectar.** Um achado por linha, na ordem do texto: **Padrão N (nome):** "trecho exato" → o ajuste em poucas palavras. Termine com a linha de resumo descrita em [Os dois modos](#os-dois-modos). Não reescreva o texto, não dê nota, e não afirme se foi ou não gerado por IA.

## Processo de reescrita e autoverificação

1. Leia a fonte e marque cada padrão de IA. Identifique o ponto central do texto e os traços de voz a preservar: vocabulário, ritmo, franqueza, humor, incerteza, digressões. Se não conseguir identificar o ponto central, pergunte para quem pediu a edição.
2. Num pedido de detecção, devolva o relatório de achados descrito em [Os dois modos](#os-dois-modos) e pare.
3. Escreva um rascunho. Leia em voz alta. Confira o ritmo, os detalhes, os verbos simples como *ser* e *ter*, e o nível de formalidade certo.
4. Faça duas perguntas:
   - **"O que ainda soa como texto gerado por IA?"**
   - **"A reescrita acrescentou ou removeu algum fato, nome, número, data, citação, referência, ranking ou outra alegação?"**
   Trate qualquer acréscimo sem apoio ou alegação perdida como erro.
5. Escreva a versão final. Afirme cada ponto com naturalidade em vez de remendar uma frase marcada de cada vez. Se uma frase continuar estranha, reescreva o parágrafo em torno do ponto principal dela. Aplique a regra de travessão do padrão 15.
6. Confira a reescrita contra a lista de verificação em [`eval.md`](eval.md). Se algum item falhar, corrija o texto e confira de novo. No modo arquivo, quando o scanner embutido estiver disponível, rode `python3 scripts/slop_scan.py <caminho>` no arquivo reescrito como última checagem; uma reescrita limpa não tem achado `fix`, e cada achado `watch` foi corrigido ou é aceitável no contexto.

Devolva o resultado no formato exigido em [Como devolver o resultado](#como-devolver-o-resultado).

## Fontes

Esta skill se baseia em duas fontes em inglês, com padrões, exemplos e ressalvas adaptados para o português:

- [Wikipédia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), mantida pela WikiProject AI Cleanup. Seus padrões vêm de revisões de texto gerado por IA na Wikipédia, organizados em padrões numerados por versões anteriores do [Humanizer](https://github.com/blader/humanizer); a revisão v3 do Humanizer, reordenada por força, contribuiu os padrões 6 e 24 e as formas ampliadas dos padrões 32 e 40.
- [No AI Slop](https://github.com/petergyang/no-ai-slop), de Peter Yang, que contribuiu os princípios de edição, o modo de detecção e boa parte dos padrões retóricos das seções 27 a 40.

O ponto central da Wikipédia resume o problema: "LLMs usam algoritmos estatísticos para prever o que vem a seguir. O resultado tende ao mais provável estatisticamente, o que se aplica à maior variedade de casos possível." É exatamente esse nivelamento estatístico que esta skill tenta desfazer.
