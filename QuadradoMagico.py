def quadrado_magico(lista):
    soma = sum(lista[0])
    #Checar se as linhas dão a mesma soma
    for linha in lista[1:]:
        if sum(linha) != soma: 
            return False
    #Checar se as colunas dão a mesma soma
    colunas = [sum(linha[i] for linha in lista) for i in range(len(lista))]
    for coluna in colunas:
        if coluna != soma:
            return False
    #Checar se as diagonais dão a mesma soma
    diagonal_principal = sum(lista[i][i] for i in range(len(lista)))
    diagonal_secundaria = sum(lista[len(lista)-1-i][i] for i in range(len(lista)))
    if diagonal_principal != soma or diagonal_secundaria != soma:
        return False
    return True