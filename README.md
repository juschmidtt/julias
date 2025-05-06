# API de Busca de Filmes
Uma API feita com Flask que permite buscar informações sobre filmes e armazená-las em um banco de dados PostgreSQL.

## Como Funciona

Primeiro, a API procura no banco de dados se o filme já foi cadastrado.

Se não encontrar, ela busca na OMDb API (um serviço externo) e salva as informações no banco para consultas futuras.

## Estrutura do Código

app.py: Arquivo principal da API. Contém as rotas e a lógica de busca.

bd.py: Cuida da conexão com o banco de dados e das operações SQL.

configuracoes.py: Guarda a URL do banco e a chave da OMDb API.

requisicoes.http: Permitem que você veja se a api encontra o filme/série 

## Endpoints

### Listar filmes salvos 

```bash
GET /filme
```
Retorna uma lista com todos os títulos armazenados no banco.


### Pesquisar filme pelo título 

```bash
GET /pesquisar/titulos?titulo={bridgerton}
```

Primeiro procura no banco.

Se não encontrar, busca na OMDb API e salva o filme no banco.

### Pesquisar filme pelo ID IMDb
```bash
GET /pesquisar/id?id={id_imdb}
```
Busca pelo ID único do IMDb.

Também salva no banco se for a primeira vez que é buscado.

## Como Rodar Localmente

### Clone o repositório:
```bash
git clone https://github.com/juschmidtt/julias.git
cd julias-main
```

### Ações necessárias para rodar o código (cmd):
```bash
python -m venv .venv
.venv\Scripts\activate
pip install flask psycopg[binary] requests
```

### Rode a aplicação:
```bash
python app.py
```





