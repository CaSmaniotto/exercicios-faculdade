x = 0
m = 0
while x < 4:
    n = eval(input(f'Nota n{x + 1}:'))
    m += n
    x += 1
print(f'Média: {m / x}')
# pede 4 notas e calcula a media

x = eval(input('Digite a temperatura em C:'))
n = 1.8 * x + 32
print(f'{x}C = {n}F')
# converte a temperatura de celsius para fahrenheits

def f(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i)
        print()
# imprime até a n-ésima linha

#-----------------------------
def imprimeLinha(numero):
    for n in range(1, numero + 1):
        print(f'{n}', end=' ')
    print()
# imprime o 'range' de n + 1 (para 1 imprime 1, para 2 imprime 1, 2, para n imprime 1, 2, ..., n)

def imprimeSequencia(numero):
    for numero in range(1, numero + 1):
        imprimeLinha(numero)
# imprime a lista de 1 até numero

numero = input('Digite um número: ')
imprimeSequencia(int(numero))
# imprime até a n-ésima linha
#-----------------------------

def h(a, b, c):
    return a + b + c
# uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def m(x):
    if x > 0:
        print('P')
    elif x < 0:
        print('N')
    else:
        return 'Zero'
# se o valor for positivo retorna P, se for negativo retorna N, se for zero retorna 0

import math

a = float(input("Digite o valor de a"))
b = float(input("Digite o valor de b"))
c = float(input("Digite o valor de c"))

delta = (b**2) - (4*a*c)

if delta > 0:
    n = math.sqrt(delta)
    x1 = (-b + n)/(2*a)
    x2 = (-b - n)/(2*a)
    print(f"As raízes são {x1} e {x2}")
elif delta == 0:
    n = math.sqrt(delta)
    x1 = (-b + n)/(2*a)
    print(f"Existe apenas uma raíz real que é {x1}")
else:
    print("Não existem raízes reais")


# ---------------------------- #
class Ponto:
    x = -1
    y = -1


p = Ponto()
p.x = 2
p.y = 3

Ponto.x = 1
Ponto.y = 4
print(Ponto.x)

print(p.x)
print(p.y)

print(Ponto.y)

# ---------------------------- #
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Ponto(2, 3)
q = Ponto(4, 5)
# ---------------------------- #

class func:
    def __init__(self, nome, data, salario):
        self.nome = nome
        self.data = data
        self.salario = salario

class ger(func):
    def __int__(self, nome, data, salario):
        super().__init__(nome, data, salario)

    def aumento(self, porcento, bonus):
        self.porcento = porcento
        self.bonus = bonus
        self.salario += bonus


f1 = ger('caetano', '10/01/20', 400)

'-----------'


#====
def f(v, i):
    if i == 0:
        return v[i]
    else:
        return max(v[i], f(v, i - 1))


l = [5, 4, 6, 8, 1, 2]
print(f(l, len(l) - 1))

def f(x):
    return sum(x)
y = [3,4,5]
f(y)



