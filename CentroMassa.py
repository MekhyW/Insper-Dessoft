#DADA UMA LISTA DE ABSISSAS E ORDENADAS DE UM OBJETO FÍSICO NO PLANO CARTESIANO, 
#RETORNA AS COORDENADAS DO CENTRO DE MASSA DO OBJETO

def calcula_cm(lista_x, lista_y):
    xcm = sum(lista_x)/len(lista_x)
    ycm = sum(lista_y)/len(lista_y)
    return [xcm, ycm]