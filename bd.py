import psycopg
import json
from configuracoes import URLBD  # Corrigido o import

conexao = psycopg.connect(URLBD)
conexao.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id SERIAL PRIMARY KEY,
        imdb_id TEXT UNIQUE,
        titulo TEXT,
        ano TEXT,
        tipo TEXT,
        data JSONB
    );
""")
conexao.commit()


def encontrarfilme_titulo(titulo):
    with conexao.cursor() as cur:
        cur.execute("SELECT * FROM filmes WHERE titulo = %s", (titulo,))
        return cur.fetchone()


def encontrarfilme_id(imdb_id):
    with conexao.cursor() as cur:
        cur.execute("SELECT * FROM filmes WHERE imdb_id = %s", (imdb_id,))
        return cur.fetchone()


def salvarfilme(filme):
    with conexao.cursor() as cur:
        cur.execute("""
            INSERT INTO filmes (imdb_id, titulo, ano, tipo, data)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (imdb_id) DO NOTHING
        """, (
            filme.get("imdbID"),
            filme.get("Title"),
            filme.get("Year"),
            filme.get("Type"),
            json.dumps(filme)
        ))
    conexao.commit()
