from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:

            print('VOCE PERDEU!')
            v += 1
        else:

            print('VOCE PERDEU!')
            break
    elif tipo == 'I':

        if total % 2 == 1:
            print('VOCE VENCEU')
        else:
            print('VOCE PERDEU')
            break
    print('VAMOS JOGAR NOVAMENTE.......')


