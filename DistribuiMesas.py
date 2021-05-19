text_alunos = open("alunosEmbaralhados.txt", 'r')
text_mesas = open("mesas.txt", 'w')
lines = text_alunos.readlines()
alunos_por_mesa = input("Quantos alunos por mesa? ")
contador = 1
numero_mesa = 1
for line in lines:
    text_mesas.write(str(numero_mesa) + " " + line)
    contador += 1
    if contador > int(alunos_por_mesa):
        contador = 1
        numero_mesa += 1
text_alunos.close()
text_mesas.close()
