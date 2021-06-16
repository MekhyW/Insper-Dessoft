def decodifica(codigo, dicionario):
    novocodigo = ""
    #iterar por todos os caracteres na senha/código
    for caractere in codigo:
        #se não há substituição a ser feita, considerar o próprio caracter
        if caractere not in dicionario.values():
            novocodigo += caractere
        #se há uma chave para ele, percorrer o dicionario para achar a substiuição e considerar a chave
        else:
            for chave in dicionario:
                if caractere == dicionario[chave]:
                    novocodigo += chave
    return novocodigo