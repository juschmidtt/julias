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
