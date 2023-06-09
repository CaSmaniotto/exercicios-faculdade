#as duas funções removem o elemento val do array arr

def function (arr, val):
    y = arr.count(val)
    for i in range(y):
        arr.remove(val)
    return len(arr)

x = [1,2,2,3,3,4,5,3]
v = 3
#-----------------------------

function(x, v)
print(x)

def function2(arr, val):
    while arr.count(val):
        arr.remove(val)
    return 0

function2(x, v)
print(x)

