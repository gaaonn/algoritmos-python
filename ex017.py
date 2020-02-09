import math
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))

a = math.pow(catetoOposto, 2)
b = math.pow(catetoAdjacente, 2)
c = a + b
c = math.sqrt(c)
print(f'O valor da hipotenusa eh: {c:.2f}')
