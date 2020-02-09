idadeMaisVelho = 0
contMulher = 0
mediaIdade = 0
homemMaisVelho = ''
for c in range(1, 5):
    print('------ {}° PESSOA ------'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite [M] para homem e [F] para mulher: '))
    mediaIdade += idade
    if sexo == 'M':
        if idade > idadeMaisVelho:
            idadeMaisVelho = idade
            homemMaisVelho = nome
    if sexo == 'F':
        if idade < 20:
            contMulher += 1
mediaIdade /= 4
print(f'A media de idade do grupo é {mediaIdade:.2f}')
print(f'O homem mais velho tem {idadeMaisVelho} anos e se chama {homemMaisVelho}.')
print(f'Ao todo são {contMulher} mulheres com menos de 20 anos.')