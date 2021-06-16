def anagrama(palavra1, palavra2):
    for caractere in palavra1:
        if palavra1.count(caractere) == palavra2.count(caractere):
            if caractere == palavra1[len(palavra1)-1]:
                return True
        else:
            return False
            break