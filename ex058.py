from random import randint
tentativas = 1
humano = -1
computador = randint(0, 10)
while humano != computador:
    humano = int(input('O número que o computador pensou é? '))
    if humano == computador:
        print('SIM')
    else:
        print('NÃO')
        tentativas += 1
print('Você tentou {} vezes até acertar! Parabéns!!'.format(tentativas))