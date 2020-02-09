resp = 'S'
soma = media = qtd = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? ')).lower().strip()[0]
media = soma / qtd
print('Você digitou {} números e a média foi {}.'.format(qtd, media))
print('O maior número digitado é {} e menor número digitado foi {}.'.format(maior, menor))
