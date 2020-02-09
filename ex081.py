contadorNumero = 0
lista = []
while True:
    n = int(input('Digite um valor: '))
    contadorNumero += 1
    lista.append(n)
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {contadorNumero} elementos!')
print(f'Os valores digitados são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')