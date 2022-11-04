import random

def previsao(cidade):
    
    resultado = {
        'cidade': cidade,
        'clima': random.choice(climas),
        'temperatura' : random.randrange(1,40)
    }

    return resultado

cidades = [
    'lages', 
    'correia pinto',
]

climas = [
    'nublado',
    'céu limpo',
]
