def remove_vogais(string):
    newstring = ""
    for caractere in string:
        if caractere not in ['a', 'e', 'i', 'o', 'u']:
            newstring += caractere
    return newstring