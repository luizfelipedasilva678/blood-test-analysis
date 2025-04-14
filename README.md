# Analisador de hemograma

Aplicação que recebe uma imagem de um hemograma e retorna
uma análise utilizando o Gemini.

## Tecnologias utilizadas

- Python (3.13)
- Docker
- Pnpm
- Flask
- Tailwind

## Como rodar

Primeiro, é necessário definir algumas variáveis de ambiente:

```
DB_PASSWORD=
DB_USER=
DB_HOST=
DB_DATABASE_NAME=
SECRET_KEY=
GEMINI_API_KEY=
```

Depois, execute o comando `docker compose up -d` para subir o banco de dados.

Por fim, basta executar `pnpm run dev`.
