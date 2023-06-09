import math
import fractions

'''
l = [0, 1, 2, 3]
l.append(4)
print(l)
print("Quatro está na posição", l.index(4))
type(l)

x = str(3)
print(x)
'''

math.log10(2)
math.log(2, 10)
'''calcula o log de 8 na base 2, os 2 fazem a mesma coisa creio eu'''

math.ceil(5.7)
'''arredonda pra cima'''

math.floor(6.6)
'''arredonda pra baixo'''

math.pi
'''valor de pi'''

math.e
'''valor do exponencial'''

math.sqrt(25)
'''calcula raiz quadrado de um numero'''

math.sin(260)
'''calcula o seno de x'''

a = fractions.Fraction(1, 2)
b = fractions.Fraction(3, 4)

print(a + b)

'''a = ['caetano', 2]
a[0] = 3
print(a)
isso mostra que as listas (arrays) são mutaveis'''

'''
x = 1
y = 2

print('X =', x, 'e', 'Y =', y, sep='A', end='...')

'''

'''
nome = input('Olá, qual o seu nome?')
print(nome)

OBS: a função input retorna uma string independente do valor
'''

'''
def f(x, y):
    res = x * y
    return res


f(3, 4)
'''

'''----------------'''
import math

num = int(input("Digite um número: "))

quadrado = math.pow(num, 2)
cubo = math.pow(num, 3)

raiz = math.sqrt(num)

print(f'O numero ao quadrado é {quadrado} e ao cubo é {cubo}')
print(f'A raiz quadrada é {raiz:.2f}')

'''----------------'''

salario = eval(input("Digite o seu salário: "))

aumento = eval(input("Digite o seu aumento: "))

aumento = salario * aumento / 100

novo_salario = salario + aumento

print("O novo salário é R$", novo_salario)

'''----------------'''


def mediaH(n, num1, num2, num3):
    media = n / ((1 / num1) + (1 / num2) + (1 / num3))

    return media


n1 = int(input("digite o primeiro número"))

n2 = int(input("digite o segundo número"))

n3 = int(input("digite o terceiro número"))

print("Media Harmonica = ", mediaH(3, n1, n2, n3))

'''-----'''

# Programa que calcula a média ponderada
a = eval(input("Digite a primeira nota: "))
b = eval(input("Digite a segunda nota: "))

m = 0.4 * a + 0.6 * b

if m >= 0.5:
    print(f'Aprovado com média: {m}')
else:
    print(f'Reprovado com média: {m}')

salario = float(input('Digite o salario: '))

tempo_casa = int(input('Digite o tempo de casa: '))

if salario >= 5:

    bonus = salario * 20 / 100

else:

    bonus = salario * 10 / 100

print(f'O bonus é R$ {bonus}')

numero1 = eval(input("Digite o número 1: "))
numero2 = eval(input("Digite o número 2: "))
numero3 = eval(input("Digite o número 3: "))
if (numero1 > numero2) and (numero1 > numero3) and (numero2 > numero3):
    print("O maior número é o primeiro: ", numero1)
if (numero2 > numero1) and (numero2 > numero3) and (numero3 > numero1):
    print("O maior número é o segundo: ", numero2)
if (numero3 > numero1) and (numero3 > numero2) and (numero1 > numero2):
    print("O maior número é o terceiro: ", numero3)
print("fim")
