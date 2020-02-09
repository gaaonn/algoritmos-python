n = 0
s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
print('A soma dos números digitados é igual a {}'.format(s))
