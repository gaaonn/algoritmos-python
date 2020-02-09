dias = int(input('Quantidade de dia(s): '))
km = float(input('Quantidade de KM(s) percorridos: '))
somaDias = dias * 60
somaKm = km * 0.15
print(f'O valor da viagem é R$ {somaDias + somaKm:.2f}')

