def valida_senha(senha):
    #caso em que a senha é muito pequena
    if len(senha) < 8:
        return False
    numerodeespeciais = 0
    especiais = []
    #itera por todos os caracteres da senha
    for i in range(len(senha)):
        if i < len(senha)-1 and senha[i] == senha[i+1]:
            #caso em que um caractere é igual ao próximo
            return False
        if senha[i] in ['?', '!', '@', '#', '$', '%', '&', '*'] and senha[i] not in especiais:
            numerodeespeciais += 1
            especiais.append(senha[i])
    #caso em que não há caracteres especiais suficientes
    if numerodeespeciais < 2:
        return False
    else:
        return True