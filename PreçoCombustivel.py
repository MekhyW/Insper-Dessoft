def contabiliza_combustivel(dicionario):
    gasolina_litros = 0
    etanol_litros = 0
    gasolina_preço = 0
    etanol_preço = 0
    tipos = []
    for item in dicionario:
        if dicionario[item]['tipo'] not in tipos:
            tipos.append(dicionario[item]['tipo'])
    resposta = dict.fromkeys(tipos)
    informacoes_relevantes = ['total litros', 'custo por litro']
    for item in resposta:
        resposta[item] = dict.fromkeys(informacoes_relevantes)
    for item in dicionario:
        if resposta[dicionario[item]['tipo']]['total litros'] == None:
            resposta[dicionario[item]['tipo']]['total litros'] = 0
            resposta[dicionario[item]['tipo']]['custo por litro'] = 0
        resposta[dicionario[item]['tipo']]['total litros'] += dicionario[item]['litros']
        resposta[dicionario[item]['tipo']]['custo por litro'] += dicionario[item]['custo']
    for item in resposta:
        resposta[item]['custo por litro'] /= resposta[item]['total litros']
    return resposta

print(contabiliza_combustivel({
    'dia 3': {
        'tipo': 'Ar',
        'litros': 100,
        'custo': 20.0
    },
    'dia 5': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 175.0
    },
    'dia 20': {
        'tipo': 'Ar',
        'litros': 50,
        'custo': 10.0
    }
}))