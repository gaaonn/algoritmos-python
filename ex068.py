from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-='*20)
humano = True
s = 0
vito = 0
while True:
    machine = randint(0, 10)
    value = int(input('Diga um valor: '))
    jogada = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    s = value + machine
    if s % 2 == 0 and jogada == 'P':
        print('-' * 20)
        print(f'Você jogou {value} e o computador {machine}. Total de {s} DEU PAR')
        print('-' * 20)
        print('VOCÊ VENCEU!!')
        print('Jogue novamente...')
        print('-' * 20)
        humano = True
        vito += 1
    elif not s % 2 == 0 and jogada == 'I':
        print('-' * 20)
        print(f'Você jogou {value} e o computador {machine}. Total de {s} DEU IMPAR')
        print('-' * 20)
        print('VOCÊ VENCEU!!')
        print('Jogue novamente...')
        print('-' * 20)
        humano = True
        vito += 1
    else:
        print('-' * 20)
        print('Você perdeu')
        print('-' * 20)
        break
print(f'GAME OVER! VOCÊ VENCEU {vito} vezes.')