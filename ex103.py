def ficha(jog='<desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gols.')


nome = str(input('Nome do Jogador: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(nome, g)
