import json
import random

import httpx
from flask import Flask, jsonify

from app.process.tempo import previsao

app = Flask(__name__)


@app.route('/')
def index():                
    return 'pagina inicial'

@app.route('/tempo/<cidade>', methods = ['GET'])
def tempo(cidade):                
    resultado = previsao(cidade)
    return  resultado











def busca():
    request = httpx.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes")
    todos = json.loads(request.text)
    print(type(todos))
    return todos

def ajusta_dados(dados):
    nomes = []
    for pessoa in dados:
        nomes.append(pessoa['nome'])
    return nomes

@app.route('/convert/<tempC>', methods = ['GET'])
def CF2(tempC):
    tempF = float(tempC) * (9/5) + 32
    return jsonify({'Fahrenheint': tempF})


@app.route('/dados', methods = ['GET'])
def dados():              
    dados = busca()
    filtrar_nome = ajusta_dados(dados)

    return jsonify({
        'resultado': filtrar_nome
    })



if __name__ == '__main__':
    app.run()
