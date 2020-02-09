from time import sleep


def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela!
    :param inicio:
    :param fim:
    :param passo:
    :return: sem retorno
    """
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de [{inicio} até {fim}] de {passo} em {passo}')
    sleep(1)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')

help(contador)
contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)