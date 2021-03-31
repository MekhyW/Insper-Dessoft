PESO_VERDURAS = 0
PESO_LEGUMES = 0

def classifica_caixa(c, p):
    a = c * (-6.193)
    b = p * 7.312
    if (a + b - 110.579) > 0:
        return 'verdura'
    else:
        return 'legume'

while True:
    i = input()
    if i == 'não':
        break
    elif i == 'sim':
        peso = float(input())
        comprimento = float(input())
        tipo = classifica_caixa(comprimento, peso)
        if tipo == 'verdura':
            PESO_VERDURAS += peso
        elif tipo == 'legume':
            PESO_LEGUMES += peso

print('Peso total das caixas de verduras: {:.2f} kg'.format(PESO_VERDURAS))
print('Peso total das caixas de legumes: {:.2f} kg'.format(PESO_LEGUMES))