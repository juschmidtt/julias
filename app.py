from flask import Flask, request, jsonify
from configuracoes import CHAVE, URLOMDB
import requests # type: ignore
import bd as db

app = Flask(__name__)


def busca_api(parametros):
    parametros['apikey'] = CHAVE
    resultado = requests.get(URLOMDB, params=parametros)
    if resultado.status_code == 200:
        dados = resultado.json()
        if dados.get("Response") == "True":
            return dados
    return None


@app.route("/filme", methods=["GET"])
def listafilmes():
    with db.conexao.cursor() as cur:
        cur.execute("SELECT titulo FROM filmes")
        filmes = cur.fetchall()
        return jsonify([f[0] for f in filmes])


@app.route("/pesquisar/titulos", methods=["GET"])
def encontrartitulo():
    titulo = request.args.get('titulo')
    if not titulo:
        return jsonify({'Erro': 'É necessário inserir um título'}), 400

    dadosint = db.encontrarfilme_titulo(titulo)
    if dadosint:
        return jsonify(dadosint[5])  # Retorna o JSON armazenado

    dadosext = busca_api({'t': titulo})
    if dadosext:
        db.salvarfilme(dadosext)
        return jsonify(dadosext)

    return jsonify({'Erro': 'Filme não localizado'})


@app.route('/pesquisar/id', methods=['GET'])
def encontrarid():
    imdb_id = request.args.get('id')
    if not imdb_id:
        return jsonify({'Erro': 'É necessário inserir um id'})

    dadosint = db.encontrarfilme_id(imdb_id)
    if dadosint:
        return jsonify(dadosint[5])

    dadosext = busca_api({'i': imdb_id})
    if dadosext:
        db.salvarfilme(dadosext)
        return jsonify(dadosext)

    return jsonify({'Erro': 'Filme não localizado'})


if __name__ == '__main__':
    app.run(debug=True)
