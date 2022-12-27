def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f
n = int(input('Digite um valor para saber seu fatorial: '))
print(fatorial(n, show=True))