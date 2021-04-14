#QUANTOS CAMINHÕES SÃO NECESSÁRIOS PARA TRANSPORTAR BAGAGENS COM SOMA DE ATÉ 2000u?
def quantos_caminhoes(pesos):
    caminhões = 1
    balança = 0
    #Para cada mala, checar a próxima mala da lista; adicionar mais um caminhão e zerar a balança se for ultrapassar o limite
    #Não checar se for a última bagagem da lista
    for index in range(len(pesos)):
        balança += pesos[index]
        if index+1 <= len(pesos)-1:
            if balança + pesos[index+1] > 2000:
                balança = 0
                caminhões += 1
    return caminhões