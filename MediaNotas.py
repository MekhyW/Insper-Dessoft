def calcula_media(listadedicionarios):
    numerodealunos = 0
    totalpontos = 0
    for dicionario in listadedicionarios:
        numerodealunos += len(dicionario)
        totalpontos += sum(dicionario.values())
    return totalpontos/numerodealunos