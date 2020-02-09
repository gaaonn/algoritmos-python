from datetime import date
dataAtual = date.today().year
ano = int(input('Digite o ano de nascimento: '))

r = dataAtual - ano

if r <= 9:
    print('MIRIM')
elif r <= 14:
    print('INFANTIL')
elif r <= 19:
    print('JUNIOR')
elif r <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
