matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somador = 0
somador2 = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))
print('='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somador += matriz[linha][coluna]
        if coluna == 2:
            somador2 += matriz[linha][coluna]
        if linha == 1:
            if maior == 0:
                maior = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maior:
                    maior = matriz[linha][coluna]

        print(f'[{matriz[linha][coluna]}]', end='')
    print()
print(f'A soma dos valores pares é {somador}')
print(f'A soma dos valores da terceira coluna é {somador2}')
print(f'A o maior elemento da 2° linha é {maior}')
