resp = ''
lista = list()
while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while resp != 'N' and resp != 'S':
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
print('-='*25)
print(f'Você digitou os valores {lista}')
