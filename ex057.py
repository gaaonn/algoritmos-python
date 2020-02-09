sexo = str(input('Digite seu sexo M ou F: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo Invalido')
    sexo = str(input('Digite seu sexo M ou F: ')).upper()
if sexo == 'F':
    print('Seu sexo é Feminino!')
else:
    print('Seu sexo é masculino')