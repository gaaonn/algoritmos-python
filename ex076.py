listagem = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, \
           'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

print('_' * 40)
print(f'{"Listagem de Preços":^40}')
print('_' * 40)
for itens in range(0, len(listagem), 2):
    print('{:.<30}R$ {:>6.2f}'.format(listagem[itens], listagem[itens+1]))
print('_' * 40)
