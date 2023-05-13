def linha():
    print('-=' * 10)
    print('Controle de terreno')
    print('-=' * 10)


linha()

def area(l, c):
    a = l * c
    print(f'O valor {l} x {c} a area é {a}')


l = float(input('largura m '))
c = float(input('Comprimento m '))
area(l, c)
