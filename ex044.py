print('{:=^40}'.format('LOJAS TG'))

value = float(input('Digite o valor: '))

print('ESCOLHA A FORMA DE PAGAMENTO')
print('[1] Dinheiro ou cheque')
print('[2] À vista no cartão')
print('[3] Em 2x no cartão')
print('[4] Em 3x no cartão ou mais')

op = int(input('Digite a condição de pagamento: '))

if op == 1:
    desc = value * 0.1
    newValue = value - desc
    print(f'O valor a pagar com desconto é R${newValue:.2f}')
elif op == 2:
    desc = value * 0.05
    newValue = value - desc
    print(f'O valor a pagar com desconto é R${newValue:.2f}')
elif op == 3:
    desc = 0
    newValue = value
    print(f'O valor a pagar é R${newValue:.2f}')
elif op == 4:
    parcela = int(input('Quantidade de parcelas?.. '))
    acresc = value * 0.20
    newValue = value + acresc
    valueP = newValue / parcela
    print(f'O valor da parcela é R${valueP:.2f} em {parcela}X.')
    print(f'O valor a pagar  com acrescimo é R${newValue:.2f}')
else:
    print('Opção Inválida!')
