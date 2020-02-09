escola = {}
escola['nome'] = str(input('Nome: '))
escola['media'] = float(input('Média: '))

if escola['media'] >= 7.0:
    escola['situação'] = 'Aprovado'
elif 5 <= escola['media'] < 7:
    escola['situação'] = 'Recuperação'
else:
    escola['situação'] = 'Reprovado'

print('*-' * 15)
for k, v in escola.items():
    print(f'    - {k.capitalize()}: {v}')