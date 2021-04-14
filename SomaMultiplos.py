#RETORNA A SOMA DOS MULTIPLOS DE DOIS NÚMEROS, ENTRE 0 E 10 VEZES O MAIOR DOS DOIS
def soma_multiplos(a, b):
    lista_de_multiplos = []
    limite = 10*max(a, b)
    #Fazer append dos múltiplos válidos do primeiro argumento
    i = 0
    while a*i <= limite:
        lista_de_multiplos.append(a*i)
        i += 1
    #Fazer append dos múltiplos válidos do primeiro argumento
    i = 0
    while b*i <= limite:
        if b*i not in lista_de_multiplos:
            lista_de_multiplos.append(b*i)
        i += 1
    #Devolver a soma da lista de múltiplos obtidos no processo
    return sum(lista_de_multiplos)