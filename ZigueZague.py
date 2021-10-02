def lista_em_zigue_zague(lista):
    if len(lista) <= 1:
        return True
    atual = lista[0]
    sentido = ''
    for item in lista[1:]:
        if item == atual or (item > atual and sentido == '>') or (item < atual and sentido == '<'):
            return False
        elif item > atual:
            sentido = '>'
        else:
            sentido = '<'
        atual = item
    return True