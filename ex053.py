frase = str(input('Digite uma frase: '))
newFrase = frase.replace(' ', '').lower()
newFrase2 = newFrase[::-1]
if newFrase == newFrase2:
    print('palindromo')
else:
    print('não e palindromo')