n1 = int(input("primeiro valor: "))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros 
    [ 5 ] sair do programa''')
    opçao = int(input('Qual é a sua opção? '))
    if opçao == 1:
        print('{} + {} é {}'.format(n1, n2, (n1 + n2)))
    elif opçao == 2:
        print('O {} x {} é {}'.format(n1, n2, (n1 * n2)))
    elif opçao == 3:
        if n1 > n2:
            print('Ente os numero digitados {} e {} o maior é {}'.format(n1, n2, n1))
        else:
            print('Entre os numero digitados {} e {} o maior é {}'.format(n1, n2, n2))
    elif opçao == 4:
        print('informe os numero novamente')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))

    elif opçao == 5:
        print('Fim ')

    else:
        print('Opção invalida, Tente novamente')
print('Fim do programa! Volte sempre!')

