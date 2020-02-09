def notas(* nota, sit=False):
    """
    --> Função recebe [n] notas e calcula a média
    --> e adiciona em um dicionario
    :param nota: Recebe os valores das notas
    :param sit: (opcional) Irá mostrar a situação em que o aluno se encontra de acordo com a média
    :return: retorna o Dicionario com os dados computados dentro
    """
    d = dict()
    cont = len(nota)
    acumuluador = maior = menor = 0
    for n in nota:
        acumuluador += n
        if maior == 0 and menor == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    media = acumuluador / cont
    d['total'] = cont
    d['maior'] = maior
    d['menor'] = menor
    d['media'] = f'{media:.2f}'
    if sit:
        if media >= 7:
            d['situação'] = 'BOA'
        elif 6 <= media < 7:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


# Programa Principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)