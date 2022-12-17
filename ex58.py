from random import randint
computador = randint(1, 8)
print('SOU SEU COMPUTADOR ACABEI DE PENSAR EM UM NUMERO ENTRE 0 E 10')
print('SERA QUE VOCÊ CONSEGUE ADIVINHAR QUAL FO?')
maximo = 0
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Escolha um numero entre 0 e 10: '))
    palpites += 1
    maximo += 1
    if palpites == 3:
        print('SUAS TENTATIVAS ACABARAM, TENTE NOVAMENTE')
        acertou = True

    elif jogador == computador:
        acertou = True
        print('VOCÊ ACERTOU COM {} PALPITE'.format(palpites))
    elif jogador < computador:
        print('MAIS >>>>>')
    else:
        print('MENOS <<<<')




