def manual(txt):
    print('-=' * 30)
    print(f'    Acessando o manual do comando {txt}')
    print('-=' * 30)
    return help(txt)


while True:
    t = str(input("Função ou Biblioteca > ")).lower()
    if t == 'fim':
        print('<FINALIZANDO... Até logo!>')
        break
    manual(t)
