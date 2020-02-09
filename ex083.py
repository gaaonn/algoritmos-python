f = str(input('Digite a formula: '))
cont = 0
for i in range(0, len(f)):
    if f[i] == '(':
        cont += 1
    if f[i] == ')':
        cont -= 1
if cont > 0:
    print('incorrect')
else:
    print('correct')
