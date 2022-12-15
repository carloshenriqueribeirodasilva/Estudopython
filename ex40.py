n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 5 and media < 7:
    print('O aluno foi reprovado')
elif media >= 5 and media <= 6:
    print('O aluno esta em recuperação!')
elif media >= 7:
    print('O aluno esta APROVADO!')
