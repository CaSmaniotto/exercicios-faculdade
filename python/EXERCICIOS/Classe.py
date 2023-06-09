class Retângulo:
#    def __init__(self, largura, comprimento):
#       self.largura = largura
#        self.comprimento = comprimento

    def setTamanho(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def perimetro(self):
        return (self.largura + self.comprimento)

    def area(self):
        return (self.largura * self.comprimento)

    def print(self):
        print("Área: ", self.area())
        print(f"Perimetro: ", self.perimetro())


p = Retângulo()
p.setTamanho(100,100)
p.print()
