n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
op = 0
r = 0
maior = menor = 0
while op != 5:
    print("""
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
    op = int(input('Digite a opção desejada: '))
    if op == 1:
        r = n1 + n2
        print('A soma é {}'.format(r))
    if op == 2:
        r = n1 * n2
        print('A multiplicacao é {}'.format(r))
    if op == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print('Maior valor eh {} menor valor eh {}'.format(maior, menor))
        elif n1 == n2:
            print('Os valores são iguais!')
        else:
            maior = n2
            menor = n1
            print('Maior valor eh {} menor valor eh {}'.format(maior, menor))
    if op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
print('Programa finalizado! Tchau!')
