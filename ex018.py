import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno de {angulo} eh {seno:.2f}')
print(f'O cosseno de {angulo} eh {cosseno:.2f}')
print(f'A tangente de {angulo} eh {tangente:.2f}')
