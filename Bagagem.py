def filtra_bagagens(lista, alt, lar, compr):
    x = 0
    for bagagem in lista:
        if bagagem[0] > alt or bagagem[1] > lar or bagagem[2] > compr:
            x += 1
    return x