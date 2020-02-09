from datetime import date
dataAtual = str(date.today())
dataAtual.split()
dataAtual = int(dataAtual[0:4])
anoNascimento = int(input('Digite o seu ano de nascimento: '))

r = dataAtual - anoNascimento
total = r - 18

if r < 18:
    print('Ainda irá se alistar.')
elif r == 18:
    print('É hora de se alistar.')
else:
    print(f'Seu tempo de alistamento passou já faz {total} ano(s).')
