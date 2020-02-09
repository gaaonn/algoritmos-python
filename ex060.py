n = int(input("Digite o valor de n: "))
fatorial = 1
while n > 0:
   print('{}'.format(n), end='')
   print(' x ' if n > 1 else ' = ', end='')
   fatorial = fatorial * n
   n -= 1
print(fatorial)
