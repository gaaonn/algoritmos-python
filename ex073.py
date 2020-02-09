times = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético Mineiro', 'São Paulo',
'Internacional', 'Corinthians', 'Atlético-PR', 'Botafogo', 'Bahia', 'Ceará SC', 'Goiás',
'Grêmio', 'Fortaleza', 'Vasco da Gama', 'Fluminense', 'Cruzeiro', 'Chapecoense',
'CSA', 'Avaí')

print(f'Cinco primeiros colocados são {times[:5]}')
print(f'Os ultimos quatro colocados são {times[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(times)}')
pos = 0
for cont in range(0, len(times)):
    if times[cont] == 'Chapecoense':
        pos = cont
print(f'O Chapecoense está na {pos+1}° posição na tabela!')

