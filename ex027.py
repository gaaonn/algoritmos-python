nick = str(input('Insira seu nome: ')).strip()
nick = nick.split()
print(f'Seu primeiro nome é: {nick[0]}')
print(f'Seu último nome é: {nick[len(nick)-1]}')
