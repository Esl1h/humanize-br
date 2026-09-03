<p align="center">
  <img src="assets/banner.svg" alt="Humanize BR: tire o sotaque de robô do seu texto" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/licença-MIT-2ee6a6.svg" alt="Licença MIT"></a>
  <a href="#os-38-padrões"><img src="https://img.shields.io/badge/padrões-38-2ee6a6.svg" alt="38 padrões"></a>
  <a href="https://github.com/Esl1h/humanize-br/stargazers"><img src="https://img.shields.io/github/stars/Esl1h/humanize-br?style=social" alt="Estrelas no GitHub"></a>
  <a href="https://github.com/Esl1h/humanize-br/network/members"><img src="https://img.shields.io/github/forks/Esl1h/humanize-br?style=social" alt="Forks no GitHub"></a>
</p>

# Humanize BR

Humanize BR reescreve texto com cara de IA para soar como uma pessoa de verdade escreveu, sem mudar o que foi dito. É a fusão, traduzida e adaptada para o português do Brasil, de duas das skills de escrita mais usadas para isso em inglês: [Humanizer](https://github.com/blader/humanizer) e [No AI Slop](https://github.com/petergyang/no-ai-slop). Por ser apenas Markdown, funciona em qualquer agente que suporte skills: Claude Code, ChatGPT, Codex, e outros.

## O problema

Modelo de linguagem em português tem vícios próprios, e tradução automática de guia em inglês não pega metade deles. "Ademais", "no cenário atual", "é importante ressaltar que", travessão em toda outra frase, aspas misturadas, "data-driven" solto no meio de uma frase em português: isso tudo denuncia texto passado por IA sem revisão tanto quanto qualquer clichê em inglês.

Esta skill nasceu porque as ferramentas boas para resolver isso existiam só em inglês. Ela junta os 35 padrões do Humanizer, baseados em ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipédia, com os padrões retóricos e os princípios de edição do No AI Slop, reorganiza tudo em **38 padrões**, e adapta cada um para como a IA realmente escreve errado em português, não em inglês traduzido.

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

A skill segue o ritmo, o vocabulário, a pontuação e os cacoetes deliberados da amostra, inclusive a frequência de travessão, e ignora o padrão 14 quando a amostra já usa travessão com frequência.

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

**Instalação manual:** copie `SKILL.md` para a pasta de skills do seu agente.

## Os 38 padrões

### Padrões de conteúdo

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 1 | **Importância inflada e falso legado** | "marcando um momento decisivo na evolução de..." | "foi criado em 1936, dentro de um movimento mais amplo de..." |
| 2 | **Citação de nomes para provar importância** | "citada pela Folha, O Globo, Estadão e BBC, com 500 mil seguidores" | Mantenha só a citação que dá contexto real |
| 3 | **Análise rasa com gerúndio** | "simbolizando... refletindo... reforçando..." | Mantenha só o que a fonte sustenta |
| 4 | **Linguagem de vendas** | "aninhada no coração das montanhas, deslumbrante e imperdível" | "fica na Serra da Mantiqueira, a 1.500 metros de altitude" |
| 5 | **Fontes vagas e autoridade genérica** | "especialistas acreditam que desempenha papel crucial" | Nomeie a fonte real, ou remova a alegação |
| 6 | **Seções formulaicas de desafios e futuro** | "apesar dos desafios, segue prosperando" | Mantenha só os fatos concretos |

### Padrões de linguagem e gramática

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 7 | **Palavras de IA superusadas** | "ademais... testemunho duradouro... panorama gastronômico" | "também... permanece comum" |
| 8 | **Evitar "ser", "estar" e "ter"** | "serve como... conta com... ostenta" | "é... tem" |
| 9 | **"Não é só X, é Y" e contrastes binários** | "não é apenas uma canção, é um manifesto" | Afirme o ponto direto |
| 10 | **Grupos forçados de três** | "inovação, inspiração e insights" | Use quantos itens o sentido pedir |
| 11 | **Trocar nomes e repetir aberturas** | "o protagonista... o personagem principal... o herói" | Use um nome só para o mesmo sujeito |
| 12 | **Falsos intervalos "de X a Y"** | "do Big Bang à dança da matéria escura" | Liste os temas direto |
| 13 | **Voz passiva e sujeito oculto** | "nenhum arquivo é necessário" | "você não precisa de um arquivo" |

### Padrões visuais e de formatação

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 14 | **Travessões em excesso** | "instituições — não pelo povo — e isso persiste —" | Troque por vírgula, ponto ou parênteses (mantém o travessão de fala) |
| 15 | **Excesso de negrito** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 16 | **Listas com mini-títulos em negrito** | "**Desempenho:** foi otimizado" | Use prosa quando a lista não ajuda |
| 17 | **Capitalização indevida em títulos** | "## Negociações Estratégicas E Parcerias" | "## Negociações estratégicas e parcerias" |
| 18 | **Emojis decorativos** | "🚀 Fase de Lançamento: 💡 Insight:" | Remova os emojis |
| 19 | **Consistência de aspas** | aspas retas e curvas misturadas no mesmo texto | Escolha um padrão e mantenha (aspas curvas não são sinal de IA em português) |

### Padrões de chatbot

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 20 | **Sobras de texto de chatbot** | "espero que isso ajude! me avise se..." | Remova |
| 21 | **Ressalvas de limite de conhecimento e chutes** | "detalhes limitados sugerem que provavelmente..." | Diga o que a fonte não mostra, ou remova |
| 22 | **Tom exageradamente condescendente** | "ótima pergunta! você está certíssimo!" | Responda direto |

### Preenchimento, ressalvas e finais

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 23 | **Frases de preenchimento** | "a fim de", "devido ao fato de que" | "para", "porque" |
| 24 | **Excesso de qualificadores** | "poderia potencialmente possivelmente" | "pode" |
| 25 | **Finais genéricos e conclusões vazias** | "o futuro é promissor... em suma..." | Termine no último fato concreto |

### Anglicismos e hifenização

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 26 | **Jargão em inglês hifenizado sem necessidade** | "data-driven, customer-centric, cutting-edge" | "com base em dados, focada no cliente, atual" |

### Retórica de falsa profundidade

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 27 | **Fingir revelar uma verdade mais profunda** | "no fundo, o que realmente importa é..." | Afirme o ponto direto |
| 28 | **Anunciar o próximo ponto** | "vamos explorar como funciona..." | Comece pelo conteúdo |
| 29 | **Título repetido na frase seguinte** | "## Desempenho\n\nVelocidade importa." | Deixe o título falar sozinho |
| 30 | **Escrever sobre a versão anterior** | "essa função foi criada para substituir..." | Descreva o comportamento atual |
| 31 | **Punchlines forçadas e fragmentos dramáticos** | "Sem preferência. Sem viés. Sem nostalgia." | Use frases naturais |
| 32 | **Ditados formulaicos de falsa sabedoria** | "simetria é a linguagem da confiança" | Afirme a alegação específica |
| 33 | **Aberturas de falsa sinceridade** | "sinceramente? depende..." | Afirme a resposta direto |
| 34 | **Responder objeções que ninguém levantou** | "não estou dizendo que... mas..." | Remova a defesa sem apoio |
| 35 | **Rejeitar alternativas falsas** | "seria tentador simplesmente... mas" | Afirme a restrição real |
| 36 | **Revelações com dois-pontos** | "o detalhe que faz funcionar: um agente avalia" | Reescreva como frase comum |
| 37 | **Metadiscurso interpretativo** | "isso importa mais do que parece" | Apague o comentário |
| 38 | **Slop de formatação** | emoji em título, negrito decorativo, bullets e headers minúsculos | Formatação deve seguir o conteúdo |

Cada padrão tem exemplo completo, ressalva e explicação em [`SKILL.md`](SKILL.md). A lista de autoverificação que a skill roda sobre o próprio trabalho está em [`eval.md`](eval.md).

## Exemplo completo

*Detalhes como o mês e o bairro precisam vir de quem escreveu. Se estiverem faltando, a skill deve perguntar em vez de inventar.*

**Antes (com cara de IA):**
> Passei um fim de semana inesquecível em Paraty, e deixa eu te contar — essa cidade literalmente roubou meu coração. Desde o momento em que cheguei, eu soube que estava em um lugar verdadeiramente especial.
>
> Aninhada entre a Serra do Mar e o litoral sul fluminense, Paraty é um vibrante testemunho da herança colonial brasileira, onde história e natureza se entrelaçam a cada esquina. Sim, as pedras irregulares do calçamento são desafiadoras — meus tornozelos sentiram isso! — mas cada passo revela um cenário de tirar o fôlego que torna tudo válido.
>
> Nenhuma viagem estaria completa sem passear de barco pela Baía de Paraty, navegando entre as ilhas mais icônicas da região. E a comida? Simplesmente divina. A cachaça artesanal local é um tesouro nacional querido, e provar uma dose ainda fresca da destilaria foi um momento que nunca vou esquecer.
>
> Mas o que realmente torna Paraty especial não é só a paisagem — é o sentimento. Ande alguns passos para fora do centro histórico e você vai descobrir um lado mais quieto e autêntico: becos ensolarados, fachadas coloniais charmosas e moradores simpáticos levando a vida no seu ritmo, convidando você a desacelerar e aproveitar cada momento.
>
> É claro, a imperdível Igreja de Santa Rita oferece vistas deslumbrantes sobre os telhados coloniais. As filas podem ser longas, mas a experiência vale cada minuto para qualquer amante de história.
>
> Eu voltaria? Com certeza. Paraty não é só um lugar para visitar — é um lugar para se apaixonar, de novo e de novo. Se você está sonhando com sua próxima escapada, esse é um destino que promete memórias para durar a vida toda. ✨

**Depois:**
> Passei um fim de semana em Paraty em outubro passado e ainda tenho sentimentos meio contraditórios sobre a viagem. Bonita, sim. Também mais dura para os tornozelos do que qualquer guia avisa.
>
> O calçamento de pedra é praticamente o assunto principal da cidade e nunca aparece nos folhetos. Fiquei hospedado perto do centro histórico, que fica lindo nas fotos e, na prática, significa andar sobre pedras irregulares toda vez que eu queria um café. No segundo dia meus tornozelos já tinham opinião formada. Comecei a planejar cada caminhada em volta de qual trecho tinha o calçamento mais liso, o que é um jeito estranho de conhecer uma cidade, mas provavelmente o mais honesto.
>
> Todo mundo recomenda o passeio de barco pela baía, então fui, espremido entre o motor e um grupo de turistas filmando a mesma ilha havia uns vinte minutos. Da próxima vez eu alugaria uma canoa sozinho, ou iria antes das nove da manhã. A cachaça, porém, merece o alarde. Provei uma na própria destilaria, ainda quente do alambique, e por uns trinta segundos entendi por que gente monta viagem inteira em torno de uma garrafa.
>
> O que eu não esperava era como a cidade fica quieta longe do calçamento principal. Duas ruas para dentro de qualquer praça vira varal de roupa, janela aberta, gente de cadeira na porta vendo o movimento passar. É essa Paraty que eu ainda penso, não a igreja do cartão-postal.
>
> A igreja é boa. A vista é ótima, a fila é longa, e passei mais tempo esperando para entrar do que olhando alguma coisa lá dentro. Se eu tivesse só dois dias, trocaria por uma tarde de me perder pelas ruas de trás.
>
> Eu voltaria, mas em maio e com um calçado melhor. Paraty não facilita nada para quem visita. Acho que gostei disso, mesmo com meus tornozelos discordando.

## De onde isso vem

Humanize BR não parte do zero. Ele é a fusão de duas skills MIT em inglês, com tradução, adaptação e reorganização completas para o português. Veja [`NOTICE.md`](NOTICE.md) para os avisos de direitos autorais originais.

| | Humanizer | No AI Slop | Humanize BR |
|---|---|---|---|
| Idioma | Inglês | Inglês | Português do Brasil |
| Padrões | 35 | 20+ | 38 |
| Modo detectar (sem reescrever) | Não | Sim | Sim |
| Princípios de edição explícitos | Parcial | Sim | Sim |
| Ajuste para travessão e aspas em português | Não | Não | Sim |
| Ajuste para anglicismos corporativos | Não | Parcial | Sim (padrão 26) |
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

- **1.0.0** - Primeiro lançamento. Traduz, mescla e adapta o Humanizer (35 padrões) e o No AI Slop (20+ padrões) em uma única skill de 38 padrões para o português do Brasil, com ressalvas próprias para travessão, aspas e anglicismos corporativos, modo de detecção sem reescrita, e plugins para Claude Code e ChatGPT/Codex.

</details>

## Licença

MIT. Veja [`LICENSE`](LICENSE) e [`NOTICE.md`](NOTICE.md) para os avisos de direitos autorais dos projetos originais.
