# Analisador de hemograma

Aplicação desenvolvida durante a disciplina de Sistemas Computacionais Inteligentes
cujo objetivo é realizar uma análise de um hemograma enviado pelo usuário.

## Tecnologias utilizadas

- Python (3.13)
- Docker
- Pnpm (necessário ter o NodeJS instalado)
- Flask
- Tailwind

## Como executar

### Banco de dados

Execute o comando `docker compose up -d` para subir o banco de dados.

### Variáveis de ambiente

Crie um arquivo ```.env``` na raiz do projeto copie e cole as variáveis abaixo e preencha com seus valores.

```
DB_PASSWORD=
DB_USER=
DB_HOST=
DB_DATABASE_NAME=
SECRET_KEY=
GEMINI_API_KEY=
```

### Executando o projeto

1. Execute ```pnpm i```
2. Execute ```pip install -r requirements.txt```
3. Execute ```pnpm run generate-css```
4. Por fim, execute ```pnpm run dev``` 
