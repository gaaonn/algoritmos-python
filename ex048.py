s = 0
contador = 0
for c in range(1, 501):
    if not c % 2 == 0:
        if c % 3 == 0:
            s += c
            contador += 1
print(f'A soma de todos os {contador} valores solicitados é {s}')