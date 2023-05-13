quantidade = 0
valor = 0
while True:
    n2 = int(input('Digite outro valor: '))
    if n2 == 999:
        break
    quantidade += 1
    valor += n2

print('Fim....')
print(f'A soma dos valores é {valor}, quantidade de vezes somados {quantidade}')



