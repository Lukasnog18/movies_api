# Movie Rental API

## Descrição
Esta API permite gerenciar o aluguel e avaliação de filmes.

## Estrutura do Projeto
- `routes.py`: Define os endpoints da API.
- `__init__.py`: Configura o Flask, a conexão com o banco de dados e o Swagger UI.
- `static/swagger.json`: Arquivo de especificação do Swagger.

## Instalação

1. **Criar e Ativar o Ambiente Virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Instalar Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

- **Banco de Dados:**
  Por padrão, o projeto usa um banco de dados mockado. Para inicializar o banco de dados e adicionar dados mock, execute o script create_db.py: python create_db.py

## Execução

1. **Executar o Servidor:**

    ```bash
    flask run
    ```

2. **Acessar a Documentação do Swagger:**

    Navegue até `http://localhost:5000/swagger` para visualizar e testar a API.

## Endpoints

### Obter Filmes por Gênero

- **Endpoint:** `/movies/<genre_name>`
- **Método:** GET
- **Parâmetros:**
  - `genre_name` (path parameter): Nome do gênero dos filmes a serem retornados.
- **Resposta:** Lista de filmes no formato JSON.

### Obter Detalhes de um Filme

- **Endpoint:** `/movies/<int:movie_id>`
- **Método:** GET
- **Parâmetros:**
  - `movie_id` (path parameter): ID do filme a ser listado.
- **Resposta:** Filme no formato JSON.

### Alugar um Filme

- **Endpoint:** `/rent/<int:user_id>/<int:movie_id>`
- **Método:** POST
- **Parâmetros:**
  - `user_id` (path parameter): ID do usuário que está alugando o filme.
  - `movie_id` (path parameter): ID do filme a ser alugado.
- **Resposta:** Lista de todos os aluguéis no formato JSON.

### Avaliar um Filme

- **Endpoint:** `/movies/<int:movie_id>/rate`
- **Método:** POST
- **Parâmetros:**
  - `user_id` (body parameter): ID do usuário.
  - `rating` (body parameter): Nota dada ao filme.
- **Resposta:** Mensagem de sucesso.

### Obter Aluguéis do Usuário

- **Endpoint:** `/user/<int:user_id>/rents`
- **Método:** GET
- **Parâmetros:**
  - `user_id` (path parameter): ID do usuário para obter o histórico de aluguéis.
- **Resposta:** Lista de aluguéis do usuário no formato JSON.

## Contribuição

Se você deseja contribuir para este projeto, siga estas etapas:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção.
3. Envie um pull request com uma descrição clara das suas alterações.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
