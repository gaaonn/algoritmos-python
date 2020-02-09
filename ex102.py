def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número  a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial em um número n
    """
    fat = 1
    if n > 0:
        while n > 0:
            if show:
                print(n, end=' x ' if n > 1 else ' = ')
            fat = fat * n
            n -= 1
        return fat


print(fatorial(8))

