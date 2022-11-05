from flask import jsonify, render_template

from app import app
from app.process.ibge import ajusta_dados, busca
from app.process.tempo import previsao


@app.route('/')
@app.route('/index')
def index():                
    return render_template('index.html')

@app.route('/tempo/<cidade>', methods = ['GET'])
def tempo(cidade):                
    resultado = previsao(cidade)
    return jsonify({
        'cidade': resultado['cidade'],
        'clima': resultado['clima'],
        'temperatura' : resultado['temperatura'],
        'umidade' : resultado['umidade']
        })

@app.route('/nomes')
def nomes():              
    dados = busca()
    filtrar_nome = ajusta_dados(dados)

    return jsonify({
        'resultado': filtrar_nome
    })
