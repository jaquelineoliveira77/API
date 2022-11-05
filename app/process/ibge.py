import json

import httpx


def busca():
    request = httpx.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes")
    todos = json.loads(request.text)
    return todos

def ajusta_dados(dados):
    nomes = []
    for pessoa in dados:
        nomes.append(pessoa['nome'])
    return nomes