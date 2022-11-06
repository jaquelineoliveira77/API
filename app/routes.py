from flask import jsonify, render_template

from app import app
from app.forms import EscolhaCidade
from app.process.ibge import ajusta_dados, busca
from app.process.tempo import previsao


@app.route('/')
@app.route('/index')
def index():                
    return render_template('index.html')

@app.route('/escolha')
def escolha():
    form = EscolhaCidade()
    return render_template('escolha.html', form=form)

@app.route('/previsao')
def previsao():
    cidade = 'lages'
    return render_template('previsao.html', cidade=cidade)

@app.route('/tempo/<cidade>', methods = ['GET'])
def tempo(cidade):                
    resultado = previsao(cidade)
    if resultado == None:
        return 'Cidade incorreta'
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
