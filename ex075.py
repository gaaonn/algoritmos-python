t = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
cont = 0
pos = 0
pares = []
for i in range(0, len(t)):
    if t[i] == 9:
        cont += 1
    if t[i] == 3:
        pos = i
        pos += 1
    if t[i] % 2 == 0:
        pares.append(t[i])
print(f'O valor 9 apareceu {cont} vezes.')
if pos > 0:
    print(f'O valor 3 apareceu na {pos}° posição.')
else:
    print('O valor 3 não aparece em nenhuma posição.')
print(f'Os valores pares digitados foram {pares[0:]}')