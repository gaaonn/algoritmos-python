vet = {}
vet['nome'] = str(input('Nome: '))
qtd = int(input('Quantidade de partidas? '))
gols = []
total = 0
for i in range(1, qtd+1):
    gols.append(int(input(f'Quantidade gols na partida {i}: ')))
for g in gols:
    total += g
vet['gols'] = gols
vet['total'] = total
print('-=' * 30)
print(vet)
print('-=' * 30)
for e, k in vet.items():
    print(f'O campo {e} tem o valor {k}')
print('-=' * 30)
print(f'O jogador {vet["nome"]} jogou {qtd} partida (s).')
for g in range(0, len(gols)):
    print(f'{"=>":>5} Na partida {g+1}, fez {gols[g]} gols.')
print(f'Foi um total de {total} gols.')