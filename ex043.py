import math

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

altura = pow(altura, 2)

imc = peso / altura

if imc < 18.5:
    print('ABAIXO DO PESO.')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('Obesidade mórbida')
