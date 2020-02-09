from random import randint
from time import sleep
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
lista2 = []
inicio = 1
for i in range(0, qtd):
    for c in range(0, 6):
        a = randint(1, 60)
        lista.append(a)
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
for i in lista2:
    print(f'Jogo {inicio}: {i}')
    sleep(1)
    inicio += 1
