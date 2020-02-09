lista = list()
maior = menor = 0
pos1 = 0
pos2 = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('-*' * 25)
print(f'Maior valor é {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'Menor valor é {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()
