numero = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-=' * 30)
numero[0].sort() # sort() deixa todas em ordem numericas
numero[1].sort() # sort() deixa todas em ordem numericas
print(f'Todos os valores {numero}')
print('-=' * 30)
print(f'Os valor pares são {numero[0]}')
print('-=' * 30)
print(f'Os valores impares são {numero[1]}')
