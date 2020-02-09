from datetime import date
ano = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    userYear = int(input(f'Qual o ano de nascimento da {c}° pessoa? '))
    if ano - userYear >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade.')