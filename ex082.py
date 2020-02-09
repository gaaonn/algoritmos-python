lista = []
listaPar = []
listaImpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] '))
    if resp == 'N':
        break
print(f'Todos os valores digitados são {lista}')
if len(listaPar):
    print(f'Todos os valores pares digitados são {listaPar}')
if len(listaImpar):
    print(f'Todos os valores ímpares digitados são {listaImpar}')