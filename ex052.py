factors = []
num =int(input('Qual numero testar? '))
for n in range(1,num+1):
    if num % n == 0:
        factors.append(n)
        if len(factors) > 2:
            print('o numero {} NAO eh primo'.format(num))
            break
if len(factors) == 2:
    print('o numero {} eh PRIMO'.format(num))