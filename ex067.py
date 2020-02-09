while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    t = 1
    if n < 0:
        break
    while t <= 10:
        print(f'{n} * {t} = {t * n}')
        t += 1
    print('-' * 30)
