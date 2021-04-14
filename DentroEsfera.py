import math

#DADO UM RAIO DE ESFERA NA ORIGEM, E AS COORDENADAS DE UM OBJETO,
#INFORMA SE ESTE OBJETO ESTÁ DENTRO OU AO MENOS TANGENCIANDO A ESFERA
def alerta(lista, raio):
    dist = math.sqrt((lista[0]**2) + (lista[1]**2) + (lista[2]**2))
    if dist <= raio:
        return True
    else:
        return False