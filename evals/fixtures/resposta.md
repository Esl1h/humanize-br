Ótima pergunta! Olhando de novo, você tem razão de que o laço de retry sai cedo demais. O laço começa na linha 40, confere o contador de backoff e sai quando as tentativas passam de 3. Você perguntou por que ele sai cedo: ele sai cedo porque o contador é incrementado antes da checagem. O ajuste é incrementar depois da checagem.

Quer que eu abra um PR com o ajuste? Me avise!
