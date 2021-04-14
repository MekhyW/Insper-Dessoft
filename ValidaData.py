#CHECAR SE A DATA INFORMADA EXISTE OU NÃO EXISTE NO CALENDARIO GREGORIANO
def valida_data(dia, mes, ano):
    #CHECAR O LIMITE BASICO DE DIA E MES
    if dia < 0 or mes < 0 or dia > 31 or mes > 12:
        return False
    #SE O DIA FOR 31, CHECAR SE ESTÁ EM UM MES COM DIA 31
    elif dia == 31 and mes not in [1, 3, 5, 7, 8, 10, 12]:
        return False
    #CHECAR SE O DIA É 29 DE FEVEREIRO DE UM ANO BISSEXTO
    elif dia > 28 and mes == 2 and ((ano%4 != 0 or ano%400 != 0) or (ano%4 != 0 or (ano%4==0 and ano%100==0 and ano%400!=0))):
        return False
    else:
        return True