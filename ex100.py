from random import randint


def sorteia(lst):
    for i in range(0, 5):
        lst.append(randint(1, 10))

def somaPar(lst):
    soma = 0
    for c in range(0, len(lst)):
        if lst[c] % 2 == 0:
            soma += lst[c]
    return soma

números = list()
sorteia(números)
print(números)
print(somaPar(números))
