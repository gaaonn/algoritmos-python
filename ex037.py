num = int(input('Insira um número: '))
print("""Qual conversão deseja fazer?
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
""")
op = int(input('Digite sua opção: '))

if op == 1:
    print(f'{num} convertido para BINARIO é = {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para OCTAL é = {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é = {hex(num)[2:]}')
else:
    print(f'Opção {op} é invalida!')
