resp = ''
total = 0
totalHigh1k = 0
produtoBarato = 0
produto = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if produtoBarato == 0:
        produtoBarato = preco
    if preco > 1000.00:
        totalHigh1k += 1
    if preco < produtoBarato:
        produtoBarato = preco
        produto = nome
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalHigh1k} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto} que custa R${produtoBarato:.2f}')
