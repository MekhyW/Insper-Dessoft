import math

#DADO UMA LISTA COM N PESOS DE MASSA, DE RECHEIO E RAIOS DE PIZZAS,
#RETORNAR A QUALIDADE PARA CADA UMA A PARTIR DE DOIS CRITÉRIOS DE DENSIDADE
def classifica_pizza(lista):
    resultado = []
    for pizza in lista:
        area = math.pi*(pizza[2]**2)
        pass_criterios = 0
        if 0.07 < pizza[1]/area < 0.09:
            pass_criterios += 1
        if  0.18 < (pizza[0] + pizza[1])/area < 0.25:
            pass_criterios += 1
        if pass_criterios == 0:
            resultado.append('baixa qualidade')
        elif pass_criterios == 1:
            resultado.append('media qualidade')
        elif pass_criterios == 2:
            resultado.append('alta qualidade')
    return resultado