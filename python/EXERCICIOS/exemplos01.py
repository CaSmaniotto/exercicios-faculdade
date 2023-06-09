numero1 = eval(input("Digite o número 1: "))
numero2 = eval(input("Digite o número 2: "))
numero3 = eval(input("Digite o número 3: "))

if (numero1 > numero2) and (numero1 > numero3) and (numero2 > numero3):
    print("O maior número é o primeiro: ", numero1)
elif (numero2 > numero1) and (numero2 > numero3) and (numero3 > numero1):
    print("O maior número é o segundo: ", numero2)
elif (numero3 > numero1) and (numero3 > numero2) and (numero1 > numero2):
    print("O maior número é o terceiro: ", numero3)
else: print("erro")
#obs: no caso de n1=1, n2=2, n3=3 dará erro

def cidades():
    lst = []

    while True:
        cidade = input('Digite a cidade: ')

        if cidade == '':
            return lst

        lst.append(cidade)


def fatorial(n):
    res = 1

    for i in range(2, n + 1):
        res *= i

    return res


n = 1
while n <= 5:
    if (n == 3):
        n += 1
        continue
    print(n)
    n += 1
print("fim")

x = 'Abacaxi'

for c in x:
    if c not in 'AEIOUT':
        print("c", c)

for x in range(1, 10 + 1):
    print(x)

frase = 'Algoritmo e ProgramaçãO de Computadores I'
count = 0
for c in frase:
    if c in 'oO':
        print('Vogal', c)
        count += 1
print('total = ', count)


# --------

# retorna true se a matriz m for simetrica
def simetrica(m):
    nline = len(m)
    nRow = len(m[0])
    a = [[0] * 3] * 3  # como inicializa um array bidimensional vazio

    for i in range(nline):
        for j in range(i, nRow):
            if m[i][j] != m[j][i]:
                return False
    print(a)
    return True


m = [['1', '2', '3'], ['2', '4', '5'], ['3', '5', '3']]
print(simetrica(m))

# -------------------