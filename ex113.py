def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[33mERRO:, por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeuboardInterrrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[33mERRO:, por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeuboardInterrrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

n1 = leiaint('Digite um valor: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')