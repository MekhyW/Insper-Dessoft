#EXEMPLO
#0-11 anos: 0.00 %
#12-17 anos: 50.00 %
#18-25 anos: 0.00 %
#26-35 anos: 0.00 %
#36-59 anos: 0.00 %
#Acima de 60 anos: 50.00 %

idades = []
numerodepessoas = 0
while True:
    idades.append(input())
    if int(idades[len(idades)-1]) < 0:
        numerodepessoas = len(idades)-1
        break

grupoA = []
grupoB = []
grupoC = []
grupoD = []
grupoE = []
grupoF = []

for idade in idades:
    if 0 <= int(idade) <= 11:
        grupoA.append(int(idade))
    elif 12 <= int(idade) <= 17:
        grupoB.append(int(idade))
    elif 18 <= int(idade) <= 25:
        grupoC.append(int(idade))
    elif 26 <= int(idade) <= 35:
        grupoD.append(int(idade))
    elif 36 <= int(idade) <= 59:
        grupoE.append(int(idade))
    elif 60 <= int(idade):
        grupoF.append(int(idade))

print("0-11 anos: {:.2f} %".format((len(grupoA)*100)/numerodepessoas))
print("12-17 anos: {:.2f} %".format((len(grupoB)*100)/numerodepessoas))
print("18-25 anos: {:.2f} %".format((len(grupoC)*100)/numerodepessoas))
print("26-35 anos: {:.2f} %".format((len(grupoD)*100)/numerodepessoas))
print("36-59 anos: {:.2f} %".format((len(grupoE)*100)/numerodepessoas))
print("Acima de 60 anos: {:.2f} %".format((len(grupoF)*100)/numerodepessoas))