velocidade = int(input('Digite a velocidade do carro: '))
multa = 0
if velocidade > 80:
    multa = velocidade - 80
    multa = multa * 7
    print(f"""Você foi multado pois estava a uma velocidade de {velocidade} KM/H em uma via que so permite a velocidade de 80 KM/H!!
O valor da multa é de R$ {multa}""")
else:
    print('Tudo ok!')
