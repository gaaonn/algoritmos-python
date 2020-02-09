salario = float(input('Digite o salario: '))
valueBonificacao = 0
if salario <= 1250:
    valueBonificacao = salario * 0.15
    salario += valueBonificacao
else:
    valueBonificacao = salario * 0.10
    salario += valueBonificacao

print(f'Value = {salario:.1f}')
