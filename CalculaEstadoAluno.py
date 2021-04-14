#PARA CADA ALUNO E SUAS NOTAS NA LISTA, ELE SERÁ OU NÃO APROVADO NA MÉDIA PONDERADA FINAL?
def calcula_estado(dados):
    resultado = []
    for dado in dados:
        #Separando os dados obtidos de acordo com o seu significado, obtendo cada um dos 3 tipos de notas
        nome = dado[0]
        av_quizzes = (dado[1][0] + dado[1][1] + dado[1][2] + dado[1][3])/4
        av_intermediaria = dado[2][0]
        av_final = dado[2][1]
        #Cálculo da nota final
        nota_final = (0.1*av_quizzes) + (0.4*av_intermediaria) + (0.5*av_final)
        if nota_final >= 5:
            #Aluno foi aprovado
            resultado.append([nome, 'A'])
        else:
            #Aluno reprovou na matéria
            resultado.append([nome, 'R'])
    return resultado