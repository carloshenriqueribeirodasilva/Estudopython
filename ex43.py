print('{:=^40}'.format(' LOJAS CARLOS ')) # {:=^40} centraliza em 40 espaços com =====
preço = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qaul é a opção do pagamento? '))
um = preço - (preço * 10 / 100)
dois = preço - (preço * 5 / 100)
tres = preço
quatro = preço + (preço * 20 / 100)
if opção == 1:
    print('Sua compra de R${:.2f} vai curstar R${:.2f} no final.'.format(preço, um))
elif opção == 2:
    print('Avista no cartão o valor de R${:.2f} com 5% de desconto fica R${:.2f}.'.format(preço, dois))
elif opção == 3:
    print('Sua compra de R${:.2f} em 2x fica R${:.2f}'.format(preço, tres))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    totalpc = quatro / parcelas
    print('Sua compra sera parcelada em {}x de R${:.2f} com JUROS '.format(parcelas, totalpc))
    print('Sua compar de R${:.2f} vai custar R${:.2f} no final.'.format(preço, quatro))
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO, Tente novamente!')





