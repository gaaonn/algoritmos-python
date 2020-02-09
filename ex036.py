valueHouse = float(input('Qual o valor da casa? '))
salary = float(input('Qual o seu salário? '))
payYear = int(input('Quantos anos para pagar? '))

percentSalary = salary * 0.30
valueMonth = valueHouse / (payYear * 12)

if valueMonth <= percentSalary:
    print(
        f'Para pagar uma casa de R${valueHouse:.0f} em {payYear} anos a prestação será de {valueMonth:.2f}!')
    print('Emprestimo concedido!')
else:
    print(
        f'Para pagar uma casa de R${valueHouse:.0f} em {payYear} anos a prestação será de {valueMonth:.2f}!')
    print('Emprestimo negado!')
