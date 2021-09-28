def verifica_lista(lista):
    if lista == []:
        return 'misturado'
    comparador_inicial = lista[0] % 2
    for numero in lista[1:]:
        if numero % 2 != comparador_inicial:
            return 'misturado'
    if comparador_inicial == 0:
        return 'par'
    else:
        return 'ímpar'