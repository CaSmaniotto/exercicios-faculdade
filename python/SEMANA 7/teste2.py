def check():
    numero = False

    a = int(input())
    b = int(input())
    c = int(input())

    l = [a, c, b]

    for i in range(len(l)):
        x = l[i]
        if (x >= 5) and (x <= 100):
            numero = True

    if numero is True:
        l.sort()
        print(l[1])

check()

