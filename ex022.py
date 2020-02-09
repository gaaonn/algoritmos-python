nome = input('Digite seu nome: ')
print(f'Nome com letras maiusculas {nome.upper()}')
print(f'Nome com letras minisculas: {nome.lower()}')
print('Quantidade de letras do nome: {}'.format(len(nome)-nome.count(' ')))
print('Primeiro nome = {}'.format(nome.find(' ')))

