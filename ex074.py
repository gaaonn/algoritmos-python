from random import randint
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = 0

for cont in range(0, len(t)):
    print(t[cont], end=' ')
print(f'\nMaior [{max(t)}] ~ Menor [{min(t)}]')
