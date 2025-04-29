from flask import Flask, request
import requests

url = "https://www.omdbapi.com/?apikey=c45ea72&"


app = Flask(__name__)

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