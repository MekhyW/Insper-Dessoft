import math
def calcula_norma(vetor):
    valor = 0
    for coordenada in vetor:
        valor += coordenada**2
    return math.sqrt(valor)