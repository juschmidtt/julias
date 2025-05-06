from flask import Flask, request, jsonify
import requests
import bd as banco
from configuracoes import CHAVE, URLOMDB

app = Flask(__name__)

def consultar_api(params):
    params["apikey"] = CHAVE
    resposta = requests.get(URLOMDB, params=params)
    if resposta.status_code == 200:
        conteudo = resposta.json()
        if conteudo.get("Response") == "True":
            return conteudo
    return None

@app.route("/filme", methods=["GET"])
def listar_filmes():
    with banco.conexao.cursor() as cursor:
        cursor.execute("SELECT titulo FROM filmes")
        resultado = cursor.fetchall()
        return jsonify([linha[0] for linha in resultado])

@app.route("/pesquisar/titulos", methods=["GET"])
def buscar_por_titulo():
    titulo_req = request.args.get('titulo')
    if not titulo_req:
        return jsonify({'Informe um título'}), 400

    titulo_formatado = titulo_req.strip().lower()

    dados_local = banco.encontrarfilme_titulo(titulo_formatado)
    if dados_local:
        return jsonify(dados_local[5])

    dados_api = consultar_api({'t': titulo_formatado})
    if dados_api:
        banco.salvarfilme(dados_api)
        return jsonify(dados_api)

    return jsonify({'Filme não encontrado'})

@app.route('/pesquisar/id', methods=['GET'])
def buscar_por_id():
    imdb_id = request.args.get('id')
    if not imdb_id:
        return jsonify({'Informe um ID'})

    dados_local = banco.encontrarfilme_id(imdb_id)
    if dados_local:
        return jsonify(dados_local[5])

    dados_api = consultar_api({'i': imdb_id})
    if dados_api:
        banco.salvarfilme(dados_api)
        return jsonify(dados_api)

    return jsonify({'Filme não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)

