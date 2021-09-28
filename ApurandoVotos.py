# SOLUÇÃO USANDO DICIONÁRIO

def apurando_votos(nomes, votos):
    contagem = {}
    votosinvalidos = 0
    for voto in votos:
        if voto in nomes:
            if voto not in contagem:
                contagem[voto] = 1
            else:
                contagem[voto] += 1
        else:
            votosinvalidos += 1
    if votosinvalidos >= max(contagem.values()):
        return 'CANCELADA'
    else:
        return max(contagem, key=contagem.get)


# SOLUÇÃO USANDO APENAS LISTAS

def apurando_votos(nomes, votos):
    contagem = [0]*len(nomes)
    votosinvalidos = 0
    for voto in votos:
        if voto in nomes:
            contagem[nomes.index(voto)] += 1
        else:
            votosinvalidos += 1
    if votosinvalidos >= max(contagem):
        return 'CANCELADA'
    else:
        return nomes[contagem.index(max(contagem))]