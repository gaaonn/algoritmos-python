def voto(y=0):
    from datetime import date
    data = date.today().year
    r = data - y
    if r < 16:
        return f'Com {r} anos: NÃO VOTA.'
    elif 16 <= r < 18 or r > 65:
        return f'Com {r} anos: VOTO OPCIONAL.'
    else:
        return f'Com {r} anos: VOTO OBRIGATÓRIO.'


# Programa principal
print(voto(1900))