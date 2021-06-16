class Retangulo:
    def __init__(self, pontoIE, pontoSD):
        self.pontoIE = pontoIE
        self.pontoSD = pontoSD
    def calcula_perimetro(self):
        perimetro = 2*(abs(self.pontoIE.x - self.pontoSD.x) + abs(self.pontoIE.y - self.pontoSD.y))
        return perimetro
    def calcula_area(self):
        area = abs(self.pontoIE.x - self.pontoSD.x)*abs(self.pontoIE.y - self.pontoSD.y)
        return area
