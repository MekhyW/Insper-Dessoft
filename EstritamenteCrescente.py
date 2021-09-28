def estritamente_crescente(lista):
    resultado = [lista[0]]
    for numero in lista[1:]:
        if numero > resultado[len(resultado)-1]:
            resultado.append(numero)
    return resultado