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

@app.route("/titulo", methods=["GET"])
def titulo():
    dados = request.json()
    titulo2 = dados["titulo"]
    requests.get(url + "t=" + titulo2)



@app.route("/id", methods=["GET"])
def id1():
    dados = request.json()
    id2 = dados["id"]
    requests.get(url + "i=" + id2)