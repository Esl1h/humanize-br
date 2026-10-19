<p align="center">
  <img src="assets/banner.svg" alt="Humanize BR: tire o sotaque de robô do seu texto" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/licença-MIT-2ee6a6.svg" alt="Licença MIT"></a>
  <a href="#os-41-padrões"><img src="https://img.shields.io/badge/padrões-41-2ee6a6.svg" alt="41 padrões"></a>
  <a href="https://github.com/Esl1h/humanize-br/stargazers"><img src="https://img.shields.io/github/stars/Esl1h/humanize-br?style=social" alt="Estrelas no GitHub"></a>
  <a href="https://github.com/Esl1h/humanize-br/network/members"><img src="https://img.shields.io/github/forks/Esl1h/humanize-br?style=social" alt="Forks no GitHub"></a>
</p>

# Humanize BR

Humanize BR reescreve texto com cara de IA para soar como uma pessoa de verdade escreveu, sem mudar o que foi dito. É a fusão, traduzida e adaptada para o português do Brasil, de duas das skills de escrita mais usadas para isso em inglês: [Humanizer](https://github.com/blader/humanizer) e [No AI Slop](https://github.com/petergyang/no-ai-slop). Por ser apenas Markdown, funciona em qualquer agente que suporte skills: Claude Code, ChatGPT, Codex, e outros.

## O problema

Modelo de linguagem em português tem vícios próprios, e tradução automática de guia em inglês não pega metade deles. "Ademais", "no cenário atual", "é importante ressaltar que", travessão em toda outra frase, aspas misturadas, "data-driven" solto no meio de uma frase em português: isso tudo denuncia texto passado por IA sem revisão tanto quanto qualquer clichê em inglês.

Esta skill nasceu porque as ferramentas boas para resolver isso existiam só em inglês. Ela junta os padrões do Humanizer (35 na versão original, mais tells das revisões v3 posteriores), baseados em ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipédia, com os padrões retóricos e os princípios de edição do No AI Slop, reorganiza tudo em **41 padrões**, e adapta cada um para como a IA realmente escreve errado em português, não em inglês traduzido.

## Os dois modos

**Editar (padrão).** Você manda um texto, a skill devolve a versão editada mais uma seção **O que mudou**.

```
/humanize-br

Passei um fim de semana inesquecível em Paraty, e deixa eu te contar —
essa cidade literalmente roubou meu coração...
```

**Detectar.** Você pergunta se um texto tem cara de IA. A skill aponta cada padrão encontrado, cita o trecho e sugere o ajuste, sem reescrever nada e sem dar nota de "% de IA" (isso não existe de verdade).

```
/humanize-br é isso IA? [cole o texto aqui]
```

Ou peça em linguagem natural:

```
Humaniza esse texto para mim: [seu texto]
```

```
Isso parece que foi escrito por ChatGPT?
```

Para editar um arquivo inteiro, indique o caminho:

```
Tira o sotaque de robô do texto em docs/post-lancamento.md
```

### Combine com sua voz

Para a reescrita soar mais como você, inclua uma amostra:

```
/humanize-br

Aqui está uma amostra do meu jeito de escrever:
[cole 2 ou 3 parágrafos seus]

Agora humaniza este texto:
[cole o texto de IA aqui]
```

A skill segue o ritmo, o vocabulário, a pontuação e os cacoetes deliberados da amostra, inclusive a frequência de travessão, e ignora o padrão 15 quando a amostra já usa travessão com frequência.

## Instalação

**Com o Skills CLI**, no Claude Code, ChatGPT, Codex ou qualquer agente compatível:

```bash
npx skills add Esl1h/humanize-br --global
```

Tire o `--global` para instalar só no projeto atual. Use `--agent <nome>` ou `--agent '*'` para escolher quem recebe a skill.

**Como plugin do Claude Code:**

```text
/plugin marketplace add Esl1h/humanize-br
/plugin install humanize-br@humanize-br
```

O comando do plugin é `/humanize-br:humanize-br`.

**No ChatGPT ou Codex**, cole isto na conversa:

```text
Instale a skill /humanize-br globalmente a partir de
https://github.com/Esl1h/humanize-br
```

**No Claude Desktop**, baixe este repositório como ZIP e envie como skill.

**Instalação manual:** copie `SKILL.md`, `eval.md` e `references/` para a pasta de skills do seu agente, e `scripts/` se quiser o scanner mecânico.

## O scanner mecânico

O repo traz `scripts/slop_scan.py`, um scanner sem dependências para as checagens que uma máquina faz bem. Ele separa os achados em duas severidades:

- `fix`: palavras banidas (com conjugações e flexões), travessões, listas com rótulo em negrito, títulos em *title case*, emojis em títulos e itens de lista, aspas misturadas e anglicismos hifenizados. A skill sempre remove esses.
- `watch`: contrastes binários, emojis no corpo do texto, linhas horizontais e as expressões vigiadas do catálogo (sobras de chatbot, falso insight, preenchimento, fontes vagas e outras). Costumam ser slop, mas pedem uma olhada no contexto.

Ele lê as listas de palavras do `SKILL.md` e do `references/patterns.md`, então nunca dessincroniza da skill. Ignora código, metadados YAML, destinos de links, URLs, texto entre aspas e travessão de diálogo. Os padrões retóricos continuam com o modelo. O mesmo scanner vem no [Humanize AI Slop](https://github.com/Esl1h/humanize-ai-slop) e escolhe o idioma pelo `SKILL.md`.

```bash
python3 scripts/slop_scan.py docs/post-lancamento.md   # lista achados com o número do padrão
python3 scripts/slop_scan.py - < rascunho.txt          # lê da entrada padrão
python3 scripts/slop_scan.py rascunho.md --json        # achados em JSON
python3 scripts/slop_scan.py limpo.md --strict         # sai com código 1 se achar algo de nível fix
```

A skill roda o scanner no modo detectar e depois de edições em arquivo sempre que instalada junto com o repo.

## Testes

`evals/` traz textos de prova com padrões plantados, controles negativos de prosa humana, reescritas de referência e um avaliador. O `evals/checks.json` define o que cada texto de prova deve produzir. `tests/` traz os testes unitários do scanner:

```bash
python3 evals/run_evals.py                                          # autoverificações (CI)
python3 evals/run_evals.py --grade evals/fixtures/sao-paulo.md saida.md
python3 -m unittest discover -s tests                               # testes do scanner (CI)
```

`evals/evals.json` lista prompts e asserções para rodar a skill completa com um agente. O `evals/run_agent_evals.py` roda esses prompts em qualquer CLI de agente que leia o prompt da entrada padrão, avalia as edições mecanicamente e, com `--judge`, pede a um segundo comando que confira cada asserção:

```bash
python3 evals/run_agent_evals.py --agent "claude -p" --judge "claude -p"
```

O CI roda as autoverificações e os testes a cada push, e confere se os arquivos compartilhados continuam iguais aos do Humanize AI Slop.

## Os 41 padrões

### Padrões de conteúdo

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 1 | **Importância inflada e falso legado** | "marcando um momento decisivo na evolução de..." | "foi criado em 1936, dentro de um movimento mais amplo de..." |
| 2 | **Citação de nomes para provar importância** | "citada pela Folha, O Globo, Estadão e BBC, com 500 mil seguidores" | Mantenha só a citação que dá contexto real |
| 3 | **Análise rasa com gerúndio** | "simbolizando... refletindo... reforçando..." | Mantenha só o que a fonte sustenta |
| 4 | **Linguagem de vendas** | "aninhada no coração das montanhas, deslumbrante e imperdível" | "fica na Serra da Mantiqueira, a 1.500 metros de altitude" |
| 5 | **Fontes vagas e autoridade genérica** | "especialistas acreditam que desempenha papel crucial" | Nomeie a fonte real, ou remova a alegação |
| 6 | **Conexão vaga ou associação imprecisa** | "é associada a", "em conexão com" | Nomeie a relação que a fonte informa |
| 7 | **Seções formulaicas de desafios e futuro** | "apesar dos desafios, segue prosperando" | Mantenha só os fatos concretos |

### Padrões de linguagem e gramática

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 8 | **Palavras de IA superusadas** | "ademais... testemunho duradouro... panorama gastronômico" | "também... permanece comum" |
| 9 | **Evitar "ser", "estar" e "ter"** | "serve como... conta com... ostenta" | "é... tem" |
| 10 | **"Não é só X, é Y" e contrastes binários** | "não é apenas uma canção, é um manifesto" | Afirme o ponto direto |
| 11 | **Grupos forçados de três** | "inovação, inspiração e insights" | Use quantos itens o sentido pedir |
| 12 | **Trocar nomes e repetir aberturas** | "o protagonista... o personagem principal... o herói" | Use um nome só para o mesmo sujeito |
| 13 | **Falsos intervalos "de X a Y"** | "do Big Bang à dança da matéria escura" | Liste os temas direto |
| 14 | **Voz passiva e sujeito oculto** | "nenhum arquivo é necessário" | "você não precisa de um arquivo" |

### Padrões visuais e de formatação

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 15 | **Travessões em excesso** | "instituições — não pelo povo — e isso persiste —" | Troque por vírgula, ponto ou parênteses (mantém o travessão de fala) |
| 16 | **Excesso de negrito** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 17 | **Listas com mini-títulos em negrito** | "**Desempenho:** foi otimizado" | Use prosa quando a lista não ajuda |
| 18 | **Capitalização indevida em títulos** | "## Negociações Estratégicas E Parcerias" | "## Negociações estratégicas e parcerias" |
| 19 | **Emojis decorativos** | "🚀 Fase de Lançamento: 💡 Insight:" | Remova os emojis |
| 20 | **Consistência de aspas** | aspas retas e curvas misturadas no mesmo texto | Escolha um padrão e mantenha (aspas curvas não são sinal de IA em português) |

### Padrões de chatbot

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 21 | **Sobras de texto de chatbot** | "espero que isso ajude! me avise se..." | Remova |
| 22 | **Ressalvas de limite de conhecimento e chutes** | "detalhes limitados sugerem que provavelmente..." | Diga o que a fonte não mostra, ou remova |
| 23 | **Tom exageradamente condescendente** | "ótima pergunta! você está certíssimo!" | Responda direto |
| 24 | **Re-explicar o que a leitora já sabe** | resposta que reconstrói o contexto da conversa antes da decisão | Comece pela decisão |

### Preenchimento, ressalvas e finais

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 25 | **Frases de preenchimento** | "a fim de", "devido ao fato de que" | "para", "porque" |
| 26 | **Excesso de qualificadores** | "poderia potencialmente possivelmente" | "pode" |
| 27 | **Finais genéricos e conclusões vazias** | "o futuro é promissor... em suma..." | Termine no último fato concreto |

### Anglicismos e hifenização

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 28 | **Jargão em inglês hifenizado sem necessidade** | "data-driven, customer-centric, cutting-edge" | "com base em dados, focada no cliente, atual" |

### Retórica de falsa profundidade

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 29 | **Fingir revelar uma verdade mais profunda** | "no fundo, o que realmente importa é..." | Afirme o ponto direto |
| 30 | **Anunciar o próximo ponto** | "vamos explorar como funciona..." | Comece pelo conteúdo |
| 31 | **Título repetido na frase seguinte** | "## Desempenho\n\nVelocidade importa." | Deixe o título falar sozinho |
| 32 | **Escrever sobre o documento em vez do assunto** | "foi criado para substituir", "a tabela abaixo compara" | Descreva o assunto, não o documento |
| 33 | **Punchlines forçadas e fragmentos dramáticos** | "Sem preferência. Sem viés. Sem nostalgia." | Use frases naturais |
| 34 | **Ditados formulaicos de falsa sabedoria** | "simetria é a linguagem da confiança" | Afirme a alegação específica |
| 35 | **Aberturas de falsa sinceridade** | "sinceramente? depende..." | Afirme a resposta direto |
| 36 | **Responder objeções que ninguém levantou** | "não estou dizendo que... mas..." | Remova a defesa sem apoio |
| 37 | **Rejeitar alternativas falsas** | "seria tentador simplesmente... mas" | Afirme a restrição real |
| 38 | **Revelações com dois-pontos** | "o detalhe que faz funcionar: um agente avalia" | Reescreva como frase comum |
| 39 | **Metadiscurso interpretativo** | "isso importa mais do que parece" | Apague o comentário |
| 40 | **Slop de formatação** | emoji em título, negrito decorativo, bullets e headers minúsculos | Formatação deve seguir o conteúdo |
| 41 | **Encenação de falso insight** | "o que ninguém te conta sobre contratação:" | Corte a encenação, deixe a alegação |

Cada padrão tem exemplo completo, ressalva e explicação em [`references/patterns.md`](references/patterns.md). O [`SKILL.md`](SKILL.md) guarda um resumo de uma linha de cada um, e a skill só carrega o catálogo completo quando precisa. A lista de autoverificação que a skill roda sobre o próprio trabalho está em [`eval.md`](eval.md).

## Exemplo completo

*Alegações sem apoio, como um superlativo continental atribuído a "especialistas", devem ser removidas, não substituídas por uma fonte inventada.*

**Antes (com cara de IA):**
> Se você é apaixonado por comida, São Paulo vai literalmente roubar seu coração — e deixa eu te contar, não existe outra cidade no Brasil que ofereça uma experiência gastronômica tão rica e multifacetada quanto a capital paulista.
>
> A cena gastronômica paulistana é um vibrante testemunho da diversidade cultural do Brasil, refletindo décadas de imigração italiana, japonesa, árabe e nordestina que moldaram um panorama culinário único. Não é só uma questão de comer bem, é uma verdadeira imersão cultural que simboliza a alma cosmopolita da cidade.
>
> Bairros como a Liberdade, a Mooca e o Bixiga oferecem experiências autênticas, imperdíveis e inesquecíveis. Segundo especialistas em gastronomia, São Paulo concentra a maior diversidade de restaurantes étnicos da América Latina, com opções que vão desde o tradicional pastel de feira até o requintado kaiseki japonês.
>
> Vale destacar que não é apenas sobre comer, é sobre viver uma experiência sensorial completa. 🍜 O detalhe que faz São Paulo ser especial: a cidade nunca dorme, e a comida de rua a qualquer hora do dia é prova viva disso.
>
> Aqui estão alguns destaques que você não pode perder:
> - **Mercadão:** um templo gastronômico com o icônico sanduíche de mortadela
> - **Feira da Liberdade:** um mergulho na cultura oriental aos finais de semana
> - **Vila Madalena:** boteco descontraído, cerveja artesanal e petiscos
>
> Apesar dos desafios típicos de uma metrópole, como o trânsito caótico e os preços elevados, São Paulo continua a prosperar como a capital gastronômica inquestionável do Brasil. Se você está planejando sua próxima viagem, esse é um destino que promete memórias inesquecíveis e sabores para durar a vida toda. Espero que esse guia ajude na sua jornada gastronômica! ✨

**Padrões identificados:** 4 (linguagem de vendas: "vibrante", "imperdíveis, inesquecíveis", "alma cosmopolita"), 1 (importância inflada: "testemunho da diversidade cultural", "moldaram um panorama culinário único"), 3 (gerúndio raso: "refletindo décadas de imigração..."), 5 (fonte vaga: "segundo especialistas... maior diversidade... da América Latina"), 10 (não é só X, é Y, duas vezes), 11 (grupo forçado de três: "autênticas, imperdíveis e inesquecíveis"), 17 (lista com mini-título em negrito), 19 (emojis 🍜 e ✨), 30 (anunciar o próximo ponto: "aqui estão alguns destaques..."), 38 (revelação com dois-pontos: "o detalhe que faz São Paulo ser especial: a cidade nunca dorme"), 7 (desafios formulaicos: "apesar dos desafios típicos..., continua a prosperar"), 21 (sobra de chatbot: "Espero que esse guia ajude..."), 27 (final genérico: "memórias inesquecíveis... para durar a vida toda"), e a expressão vigiada "vale destacar que".

**Depois:**
> São Paulo tem uma das cenas gastronômicas mais diversas do Brasil, moldada por mais de um século de imigração italiana, japonesa, árabe e nordestina. Isso aparece tanto na comida de rua quanto no cardápio dos restaurantes mais concorridos.
>
> Essa mistura fica mais visível em três bairros. A Liberdade abriga a maior comunidade japonesa fora do Japão e concentra lojas de doces, casas de lámen e a feira de fim de semana. A Mooca e o Bixiga guardam a herança italiana em restaurantes de família que ainda seguem receitas antigas. Cada bairro tem um sotaque próprio, do pastel de feira ao kaiseki.
>
> O Mercadão Municipal é onde boa parte dos visitantes começa, por causa do sanduíche de mortadela, generoso e simples, que virou tão símbolo da cidade quanto qualquer prato mais elaborado. Na Feira da Liberdade, o destaque de fim de semana é a comida de rua japonesa. Na Vila Madalena, os botecos ficam abertos até tarde, com petisco e cerveja artesanal para quem prefere passar a noite ali em vez de num museu.
>
> O trânsito é ruim e os preços em bairros badalados não são baixos, mas isso não costuma afastar quem já decidiu vir para comer.

**O que mudou:** cortamos toda alegação sem apoio ("maior diversidade da América Latina", "especialistas em gastronomia") em vez de inventar uma fonte para ela. Trocamos a lista de marcadores em negrito por prosa, tiramos os emojis, o "aqui estão os destaques" e a despedida de chatbot, e terminamos no fato concreto (trânsito e preço) em vez do final genérico de "memórias para durar a vida toda". Todo bairro, prato e fato original foi mantido: nada foi inventado, só reduzido ao que é verificável ou de conhecimento comum (Mercadão, Liberdade como maior comunidade japonesa fora do Japão, Mooca e Bixiga como bairros italianos, Vila Madalena como polo de bar).

## De onde isso vem

Humanize BR não parte do zero. Ele é a fusão de duas skills MIT em inglês, com tradução, adaptação e reorganização completas para o português, e incorpora tells das revisões v3 do Humanizer (conexão vaga e leitora errada). Veja [`NOTICE.md`](NOTICE.md) para os avisos de direitos autorais originais.

| | Humanizer | No AI Slop | Humanize BR |
|---|---|---|---|
| Idioma | Inglês | Inglês | Português do Brasil |
| Padrões | 35 | 20+ | 41 |
| Modo detectar (sem reescrever) | Não | Sim | Sim |
| Princípios de edição explícitos | Parcial | Sim | Sim |
| Ajuste para travessão e aspas em português | Não | Não | Sim |
| Ajuste para anglicismos corporativos | Não | Parcial | Sim (padrão 28) |
| Plugin Claude Code | Sim | Não | Sim |
| Plugin ChatGPT / Codex | Não | Sim | Sim |

## Contribuindo

Sugestões de novos padrões, correções de tradução e exemplos mais naturais em português são bem-vindos. Leia [`AGENTS.md`](AGENTS.md) antes de editar `SKILL.md`, e rode `python3 scripts/validate-package.py` antes de abrir um *pull request*. Veja também [`CONTRIBUTING.md`](CONTRIBUTING.md).

Se esta skill te poupou trabalho, deixe uma estrela. Isso ajuda outras pessoas que escrevem em português a encontrar a ferramenta.

## Histórico de estrelas

<a href="https://star-history.com/#Esl1h/humanize-br&Date">
  <img src="https://api.star-history.com/svg?repos=Esl1h/humanize-br&type=Date" alt="Gráfico de histórico de estrelas do Humanize BR" width="100%">
</a>

## Histórico de versões

<details>
<summary>Ver notas de lançamento</summary>

- **1.1.0** - Sincroniza com o humanize-ai-slop e com revisões posteriores do Humanizer: ganha os padrões de conexão vaga (6), de re-explicar o que a leitora já sabe (24) e de encenação de falso insight (41), amplia o padrão de escrever sobre o documento (32), e chega a 41 padrões. Ganhou também a seção "O que perguntar", formato definido para o relatório de detecção, índice de padrões no SKILL.md, scanner mecânico (`scripts/slop_scan.py`), suíte de testes (`evals/`) e a autoverificação alinhada com a versão em inglês.
- **1.0.0** - Primeiro lançamento. Traduz, mescla e adapta o Humanizer (35 padrões) e o No AI Slop (20+ padrões) em uma única skill de 38 padrões para o português do Brasil, com ressalvas próprias para travessão, aspas e anglicismos corporativos, modo de detecção sem reescrita, e plugins para Claude Code e ChatGPT/Codex.

</details>

## Licença

MIT. Veja [`LICENSE`](LICENSE) e [`NOTICE.md`](NOTICE.md) para os avisos de direitos autorais dos projetos originais.
