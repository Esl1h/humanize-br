# Contribuindo com o Humanize BR

Obrigado pelo interesse em melhorar a skill.

## Antes de abrir um pull request

1. Leia [`AGENTS.md`](AGENTS.md). Ele explica a estrutura do pacote e as regras para mudar `SKILL.md` sem quebrar a numeração dos padrões ou a sincronia entre os arquivos.
2. Rode a validação local:

   ```bash
   python3 scripts/validate-package.py
   python3 evals/run_evals.py
   ```

3. Se você mudou algo em `SKILL.md`, atualize também a tabela correspondente em `README.md` e, se for uma mudança de comportamento, acrescente uma nota em **Histórico de versões**.

## Tipos de contribuição bem-vindos

- **Novo padrão de texto com cara de IA** que você percebeu em português e ainda não está coberto.
- **Exemplo mais natural** para um padrão existente, especialmente se o atual ainda soa como tradução.
- **Correção de tradução ou de acentuação.**
- **Casos de falso positivo**: um padrão sinalizando algo que não deveria.

Para sugerir um padrão novo, abra uma issue com um trecho real (anonimizado, se necessário) que mostre o problema antes de mandar o pull request. Isso evita retrabalho caso o padrão já esteja coberto de outro jeito.

## O que evitar

- Não traduza um exemplo do Humanizer ou do No AI Slop ao pé da letra. Verifique se o fenômeno ocorre em português do jeito descrito (veja os padrões 14, 19 e 26 no `SKILL.md` como referência de adaptação, não de tradução).
- Não abra pull requests que misturem mudança de comportamento com reformatação. Um assunto por vez.
