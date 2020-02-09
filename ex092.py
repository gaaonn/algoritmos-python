from datetime import date
data = date.today().year
vet = dict()
vet['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
vet['idade'] = data - ano
vet['ctps'] = int(input('Carteira de trabalho: (0 não tem!) '))
if vet['ctps'] != 0:
    vet['contratação'] = int(input('Qual o ano de contratação? '))
    vet['salario'] = float(input('Qual o salário? '))
    apo = (vet['contratação'] + 35) - ano
    vet['idade-aposentadoria'] = apo
print('=-' * 30)
for e, k in vet.items():
    print(f'    - {e} tem o valor {k}')
