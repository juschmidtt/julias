from flask import Flask, request, jsonify
import requests
import banco_dados as db

url = "https://www.omdbapi.com/?apikey=c45ea72&"


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
        return jsonify({'error': 'É necessário inserir um título'}), 400