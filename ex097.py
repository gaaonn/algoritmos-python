def escreva(txt):
    t = len(txt) + 4
    print('-' * t)
    print(f'  {txt}')
    print('-' * t)


f = str(input("Digite uma frase: "))
escreva(f)
