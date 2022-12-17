from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O atleta é MIRIN')
elif idade > 9 and idade <= 14:
    print('O atle é INFANTIL!')
elif idade > 14 and idade <= 19:
    print('O atleta é JUNIOR!')
elif idade > 19 and idade <= 25:
    print('O atleta é SENIOR!')
elif idade > 25:
    print('O atleta é MASTER!')
