# Guia para agentes

Este arquivo explica como alterar o Humanize BR sem quebrar o pacote nem o prompt.

## O que este repositório contém

Humanize BR é uma skill de agente escrita em Markdown, em português do Brasil, que mescla e traduz duas skills em inglês: [Humanizer](https://github.com/blader/humanizer) e [No AI Slop](https://github.com/petergyang/no-ai-slop). Não há etapa de build para a skill em si.

Mantenha a skill portátil. Não escreva instruções que a limitem a uma ou duas ferramentas de agente específicas.

## Arquivos principais

- `SKILL.md` é a fonte da verdade e o único arquivo de skill do repositório. Contém metadados YAML portáveis, os modos, os princípios de edição, as listas de palavras, um índice de uma linha dos 41 padrões e o processo de reescrita.
- `references/patterns.md` é o catálogo completo de padrões: expressões vigiadas, o problema e um exemplo de antes e depois de cada padrão. A skill lê esse arquivo sob demanda.
- `eval.md` contém a lista de autoverificação que a skill roda sobre o próprio trabalho antes de devolver o resultado.
- `scripts/slop_scan.py` escaneia texto atrás dos padrões que uma máquina consegue checar, como achados `fix` ou `watch`, e lê as listas de palavras do `SKILL.md` e do `references/patterns.md`.
- `scripts/check-sync.py` confere se este repositório e o [Humanize AI Slop](https://github.com/Esl1h/humanize-ai-slop) não se distanciaram.
- `tests/` traz os testes unitários do scanner.
- `evals/` traz textos de prova com padrões plantados e controles negativos, reescritas de referência, os achados esperados (`checks.json`), um avaliador (`run_evals.py`), prompts de avaliação para agentes (`evals.json`) e um executor de evals com agente (`run_agent_evals.py`).
- `README.md` explica instalação, uso, padrões e histórico de versões.
- `.claude-plugin/plugin.json` descreve o plugin do Claude Code e aponta o carregador de skill para o `SKILL.md` na raiz.
- `.claude-plugin/marketplace.json` permite adicionar este repositório como marketplace do Claude.
- `.codex-plugin/plugin.json` descreve o plugin para ChatGPT e Codex.
- `agents/openai.yaml` traz metadados de interface para agentes compatíveis com o formato OpenAI.
- `scripts/validate-package.py` confere os arquivos do pacote e a consistência entre eles.
- `NOTICE.md` documenta a origem e a licença dos dois projetos em inglês usados como base.

## Regras para mudanças

Mantenha `SKILL.md`, `eval.md` e `README.md` sincronizados.

- **Padrões:** a skill tem 41 padrões numerados, organizados em sete categorias. Ao adicionar, remover ou renumerar um padrão, atualize o catálogo em `references/patterns.md`, a tabela do README, o índice de padrões no `SKILL.md`, o validador, os números de padrão relatados por `scripts/slop_scan.py` e toda referência ao número do padrão.
- **Versão:** mantenha a mesma versão em `SKILL.md`, em `metadata.version`, na primeira entrada de versão do README, em `.claude-plugin/plugin.json` e em `.codex-plugin/plugin.json`. Não acrescente um campo `version` de nível superior na skill.
- **Compatibilidade:** mantenha as instruções de instalação e uso neutras entre agentes. Nomes como Claude Code, ChatGPT e Codex são exemplos, não limitações.
- **Histórico:** acrescente uma nota curta de versão no README para toda mudança de comportamento ou correção não óbvia.
- **Localização:** ao adaptar um padrão do inglês, não traduza ao pé da letra. Verifique se o fenômeno realmente ocorre em português (travessão, aspas e hifenização têm convenções diferentes do inglês) e ajuste o exemplo e a ressalva de acordo. Veja os padrões 14, 19 e 26 em `references/patterns.md` como referência desse cuidado.
- **Arquivos compartilhados:** `scripts/slop_scan.py`, `scripts/check-sync.py`, `evals/run_evals.py` e `evals/run_agent_evals.py` são idênticos no Humanize AI Slop. Mantenha o comportamento específico de idioma no `CONFIG` do scanner e no `evals/checks.json`, e copie qualquer mudança para os dois repositórios.
- **Paridade:** uma mudança estrutural aqui (uma seção, um passo numerado, um item de lista no SKILL.md ou no eval.md, um prompt de avaliação) pede a mesma mudança no Humanize AI Slop. O `scripts/check-sync.py` acusa a divergência.
- **Tamanho:** mantenha o SKILL.md curto. Detalhe de que a skill não precisa em toda execução vai para `references/`.
- **Verificações:** antes de publicar, rode `python3 scripts/validate-package.py`, `python3 evals/run_evals.py`, `python3 -m unittest discover -s tests` e `python3 scripts/check-sync.py`.

## Estilo de escrita

Use linguagem simples e direta em comentários de código, prompts, documentação, descrições, mensagens de validação e relatórios de progresso, tanto em português quanto em inglês.

- Vá direto ao ponto principal.
- Use palavras comuns e voz ativa.
- Mantenha frases e parágrafos curtos.
- Use um único termo para a mesma coisa.
- Use "deve" ou "precisa" para requisitos, não linguagem ambígua.
- Use títulos, listas e tabelas quando isso ajudar quem lê.
- Remova palavras repetidas ou desnecessárias.
- Escreva em português com acentuação e crase corretas; não deixe passar erros de diacríticos.
- Evite duplas negativas.
- Mantenha identificadores, comandos, caminhos, campos de esquema, citações, frases vigiadas e exemplos que carregam comportamento exatamente como estão.
- Preserve o sentido técnico completo.
- Código, comentários de código e scripts de automação (`scripts/`, `.github/workflows/`) permanecem em inglês, seguindo a convenção do restante do ecossistema de skills.

## Editando a skill

- Mantenha os metadados YAML válidos.
- Trate o prompt abaixo dos metadados como o produto em si.
- Prefira uma instrução curta e clara a mais uma exceção ou explicação repetida.
- Ao mesclar um padrão vindo do Humanizer com um padrão equivalente do No AI Slop, escolha o exemplo mais natural em português em vez de somar os dois exemplos originais traduzidos.
