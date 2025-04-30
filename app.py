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
        return jsonify({'Erro': 'É necessário inserir um título'}), 400
    

    dadosint = db.pesquiar_f_t(titulo)
    if dadosint:
        return jsonify(dadosint[5]) 
    
    dadosext = buscasapi({'t': titulo})
    if dadosext: 
        db.salvarfilme(dadosext)
        return jsonify(dadosext)
    

    return jsonify({'Erro': 'Filme não localizado'})

@app.route('/pesquisar/id', methods=['GET'])
def encontrarid():
    imdb_id = request.args.get('id')
    if not imdb_id:
        return jsonify({'Erro': 'É necessário inserir um id'})