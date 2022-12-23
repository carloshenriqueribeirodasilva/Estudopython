temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip()
    if resp in 'nN':
        break
print(f'Os dados foram {princ}')
print(f'Voce cadastrou {len(princ)}')


