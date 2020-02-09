from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.25)
        if cont == 0:
            cont = maior
        else:
            if v > maior:
                maior = v
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


def lin():
    print('-=' * 30)


lin()
maior(2, 9, 5, 10, 22, 3)
lin()
maior(4, 3, 4, 99, 100, 21200)
lin(),
maior(298, 488, 309, 634, 678, 234, 845, 562, 147)
lin()
maior(2928, 48138, 309, 634, 6478, 2394, 84335, 562, 101147)
lin()
maior()
