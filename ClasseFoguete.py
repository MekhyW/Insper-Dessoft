class Foguete:
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.distpercorrida = 0
    def atualizar(self, tempo):
        self.distpercorrida += self.velocidade * (tempo/3600)
        return self.distpercorrida