---
title: Crônica do plantão
tags: [crônica, ops]
---

# Crônica do plantão

Eu achava que o pior do plantão era o bip. Não é. O pior é a hora depois, quando a correção já entrou e o sono não vem, e você fica relendo o canal do incidente como se ele te devesse um pedido de desculpas.

Na terça passada o bip tocou às 3h12. A fila de retentativas tinha chegado a 41.000 tarefas, e o painel dizia "saudável", piada que só painel sabe contar. Meu gerente gosta de dizer que a gente precisa "alavancar os runbooks". Eu gosto de dizer que o runbook é um arquivo de texto que ninguém abre desde 2023.

— Você reiniciou os workers? — perguntou a Bia no chat.

— Reiniciei, e subi para seis réplicas.

A correção foram dois comandos:

```sh
./bin/worker restart --all   # alavancar o caminho robusto
./bin/worker scale --replicas=6
```

Depois escrevi uma nota no [documento do incidente](https://wiki.example.com/ops/plantao--noturno) e mandei um e-mail para o time. O GPT-4 resumiu os logs para mim, mal. Corrigi o resumo à mão.

Talvez a lição seja confiar mais no tamanho da fila do que na luz verde do painel. Talvez seja ir dormir. Descubro no próximo bip, lá pelas 3 da manhã, provavelmente numa terça.
