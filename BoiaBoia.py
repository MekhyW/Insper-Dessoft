import math

#DADO UM TORÓIDE DE PESO P, RAIO R E SEÇÃO TRANVERSAL r, SERÁ QUE IRÁ FLUTUAR NA ÁGUA?
def will_it_float(P, R, r):
    densidade_água = 0.997
    PesoToróide = P*1000
    VolumeToróide = 2*(math.pi**2)*R*(r**2)
    Densidade = PesoToróide/VolumeToróide
    if Densidade <= densidade_água:
        return True
    else:
        return False