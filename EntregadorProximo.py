import math

def entregador_mais_proximo(restaurante, entregadores):
    menordistancia = math.inf
    entregadormaisproximo = 0
    restauranteX = restaurante[0]
    restauranteY = restaurante[1]
    #iterar para cada entregador
    for entregador in range(len(entregadores)):
        #checar a distancia e, se for menor que a menor distancia encontrada até então, atualizar essa distancia e o indice de quem está a ela
        distancia = math.sqrt(((restauranteX - entregadores[entregador][0])**2) + ((restauranteY - entregadores[entregador][1])**2))
        if distancia < menordistancia:
            menordistancia = distancia
            entregadormaisproximo = entregador
    return entregadormaisproximo