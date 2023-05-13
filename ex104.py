def leiaint(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Você digitou no {n}')