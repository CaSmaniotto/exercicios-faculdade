# obs: não consegui fazer com que seja impresso uma pessoa por vez ao usar sair()

class Fila():
    def __init__(self):
        self.normal = []
        self.pref = []

    # adiciona uma pessoa a fila
    def entrar(self, idade, nome):
        self.idade = idade
        self.nome = nome

        if self.idade >= 60:
            self.pref.append(nome)
        else:
            self.normal.append(nome)

    # remove uma pessoa da fila
    def sair(self):

        # remove 2 pessoas da fila preferencial e depois uma da normal
        for i in range(2):
            if not self.pref:
                break
            print(self.pref.pop(0))
        print(self.normal.pop(0))
