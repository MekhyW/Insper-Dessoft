def calcula_escola(lista):
    soma = 0
    for quesito in lista:
        quesito.remove(min(quesito))
        soma += sum(quesito)
    return soma