from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print(f'Os numero sorterador foram: ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}') # MAX MOSTRA O MAIOR NUMERO SORTEADO
print(f'O menor valor sorteado foi {min(numeros)}') # MIN MOSTRA O MENOR NUMERO SORTEADO