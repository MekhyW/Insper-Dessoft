def verifica_primos(lista):
    resultado = {}
    for numero in lista:
        if numero == -1 or numero == 1 or numero == 0:
            resultado[numero] = False
        for i in range(2, numero+1):
            if i == numero:
                resultado[numero] = True
            elif numero%i == 0:
                resultado[numero] = False
                break
    return resultado