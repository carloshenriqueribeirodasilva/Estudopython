valor = float(input("Qual o preço do produto?: "))
desconto = valor - (valor * 5 / 100)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(valor, desconto))
