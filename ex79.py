numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
numeros.sort()
print(f'Voce digitou os valores {numeros} ')
