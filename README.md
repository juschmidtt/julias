# API de Busca de Filmes
## Endpoints
### 1. Listar Filmes
Rota: GET /filme

Descrição: Retorna todos os títulos de filmes armazenados no banco de dados.

### 2. Pesquisar Filme por Título
Rota: GET /pesquisar/titulos?titulo={titulo}

Descrição: Busca um filme pelo título. Se não encontrado no banco, consulta a OMDb API e salva os dados.

### 3. Pesquisar Filme por ID
Rota: GET /pesquisar/id?id={imdb_id}

Descrição: Busca um filme pelo ID IMDb. Se não encontrado no banco, consulta a OMDb API e salva os dados.
## Como Rodar
### Pré-requisitos
Python 3.8+
Flask
psycopg2
Requests

## Instalação
### Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/juschmidtt/julias.git
cd julias

### Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure a conexão com o banco no arquivo configuracoes.py:

python
Copiar
Editar
URLBD = "postgresql://postgres:3f%40db@164.90.152.205:80/julias"
CHAVE = "c45ea72"
URLOMDB = "http://www.omdbapi.com/"

### Rode o servidor Flask:

bash
Copiar
Editar
python app.py
A API estará disponível em http://127.0.0.1:5000/.

Licença
MIT License
