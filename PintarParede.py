largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area = largura * altura
print('sua parede tem a dimensao de {}x{} e sua area é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('para pintar a essa parede voce vai precisar de {}L de tinta'.format(tinta))
