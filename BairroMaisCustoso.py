def bairro_mais_custoso(dicionario):
    maiorcusto = 0
    nomedomaiorcusto = ""
    for bairro in dicionario:
        custo = sum(dicionario[bairro][6:])
        if custo > maiorcusto:
            maiorcusto = custo
            nomedomaiorcusto = bairro
    return nomedomaiorcusto