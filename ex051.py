fst = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = fst + (10 - 1) * razao

for c in range(fst, décimo + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')