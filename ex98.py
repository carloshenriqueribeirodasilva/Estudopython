from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até o fim {f} de {p} em {p}.')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        contador = i
        while contador <= f:
            print(f'{contador}', end=' ')
            sleep(0.5)
            contador += p
        print('FIM')
    else:
        contador = i
        while contador >= f:
            print(f'{contador}', end=' ')
            sleep(0.5)
            contador -= p
        print('FIM')

contador(1, 10 ,1)
contador(10, 0, 2)
print('Agora é sua vez')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)



