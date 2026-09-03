# Guia para agentes

Este arquivo explica como alterar o Humanize BR sem quebrar o pacote nem o prompt.

## O que este repositório contém

Humanize BR é uma skill de agente escrita em Markdown, em português do Brasil, que mescla e traduz duas skills em inglês: [Humanizer](https://github.com/blader/humanizer) e [No AI Slop](https://github.com/petergyang/no-ai-slop). Não há etapa de build para a skill em si.

Mantenha a skill portátil. Não escreva instruções que a limitem a uma ou duas ferramentas de agente específicas.

## Arquivos principais

- `SKILL.md` é a fonte da verdade e o único arquivo de skill do repositório. Contém metadados YAML portáveis, 38 padrões numerados, seus exemplos e o processo de reescrita.
- `eval.md` contém a lista de autoverificação que a skill roda sobre o próprio trabalho antes de devolver o resultado.
- `README.md` explica instalação, uso, padrões e histórico de versões.
- `.claude-plugin/plugin.json` descreve o plugin do Claude Code e aponta o carregador de skill para o `SKILL.md` na raiz.
- `.claude-plugin/marketplace.json` permite adicionar este repositório como marketplace do Claude.
- `.codex-plugin/plugin.json` descreve o plugin para ChatGPT e Codex.
- `agents/openai.yaml` traz metadados de interface para agentes compatíveis com o formato OpenAI.
- `scripts/validate-package.py` confere os arquivos do pacote e a consistência entre eles.
- `NOTICE.md` documenta a origem e a licença dos dois projetos em inglês usados como base.

## Regras para mudanças

Mantenha `SKILL.md`, `eval.md` e `README.md` sincronizados.

- **Padrões:** a skill tem 38 padrões numerados, organizados em oito categorias. Ao adicionar, remover ou renumerar um padrão, atualize a tabela do README, o título da seção, o validador e toda referência ao número do padrão.
- **Versão:** mantenha a mesma versão em `SKILL.md`, em `metadata.version`, na primeira entrada de versão do README, em `.claude-plugin/plugin.json` e em `.codex-plugin/plugin.json`. Não acrescente um campo `version` de nível superior na skill.
- **Compatibilidade:** mantenha as instruções de instalação e uso neutras entre agentes. Nomes como Claude Code, ChatGPT e Codex são exemplos, não limitações.
- **Histórico:** acrescente uma nota curta de versão no README para toda mudança de comportamento ou correção não óbvia.
- **Localização:** ao adaptar um padrão do inglês, não traduza ao pé da letra. Verifique se o fenômeno realmente ocorre em português (travessão, aspas e hifenização têm convenções diferentes do inglês) e ajuste o exemplo e a ressalva de acordo. Veja os padrões 14, 19 e 26 no `SKILL.md` como referência desse cuidado.
- **Verificações:** antes de publicar, rode `python3 scripts/validate-package.py`.

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
