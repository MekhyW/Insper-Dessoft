#["João", "Marcos", "Felipe"]
# + ["Cléber", "Lisboa", "Catapano"]
# = ["João Cléber", "Marcos Lisboa", "Felipe Catapano"]

def junta_nome_sobrenome(nomes, sobrenomes):
    resultado = []
    for indice in range(0, len(nomes)):
        resultado.append(nomes[indice] + " " + sobrenomes[indice])
    return resultado