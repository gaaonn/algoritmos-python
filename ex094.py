pessoas = dict()
listaPessoas = list()
contador = médiaIdade = 0
mulheres = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    while pessoas['sexo'] != 'M' and pessoas['sexo'] != 'F':
        print('ERRO! Sexo informado inválido. Tente novamente')
        pessoas['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    pessoas['idade'] = int(input('Idade: '))
    médiaIdade += pessoas['idade']
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    listaPessoas.append(pessoas.copy())
    contador += 1
    resp = str(input('Deseja prosseguir? S/N: ')).upper()
    if resp in 'Nn':
        break
media = médiaIdade / contador
print(f'- Foram cadastradas {contador} pessoas.')
print(f'- A média de idades foi {media}.')
print(f'- Lista de mulheres {mulheres}')
print(f'- Lista de pessoas com idade acima da média.')
for v in listaPessoas:
    if media < v['idade']:
        print(f'    nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}\n')
print(listaPessoas)