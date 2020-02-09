km = int(input('Digite a distancia da viagem em km: '))

if km <= 200:
    valorPassagem = km * 0.50
    print(f'O valor da passagem é R$ {valorPassagem}')
else:
    valorPassagem = km * 0.45
    print(f'O valor da passagem é R$ {valorPassagem}')
