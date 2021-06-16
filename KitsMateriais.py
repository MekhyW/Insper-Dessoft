def separa_por_inicial(dicionario):
    alunos = []
    resultado = {}
    #cria uma lista com todos os alunos do dicionario; a turma é irrelevante
    for lista in dicionario.values():
        for aluno in lista:
            alunos.append(aluno)
    #para cada aluno, colocar na chave da sua inicial do dicionario resultado o seu nome
    for aluno in alunos:
        if aluno[0] not in resultado:
            resultado[aluno[0]] = []
        resultado[aluno[0]].append(aluno)
    return resultado