import random

def previsao(cidade):
    cidades = open("app\process\cidades.txt", 'r').readlines()
    if (cidade+'\n') in cidades:
        resultado = {
            'cidade': cidade,
            'clima': random.choice(climas),
            'temperatura' : random.randrange(1,40),
            'umidade': random.randrange(1,100)
        }
        return resultado
    return None

climas = [
    'nublado',
    'céu limpo',
    'chuva',
    'tempestade',
]
