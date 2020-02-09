import random
r = random.randint(0, 5)
user = int(input('Digite um número entre 0 e 5: '))
print(r)
print('VENCEU' if user == r else 'PERDEU')
