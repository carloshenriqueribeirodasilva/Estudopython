from datetime import date
sexo = int(input('''Assinale a alternativa correta!
[ 1 ] HOMEM
[ 2 ] MULHER: '''))
if sexo == 2:
    print('Você nao precisa responder estas perguntas!')
    atual = date.today().year # comando para pegar a data atual
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
    if idade == 18:
         print('Você tem que alistar IMEDIATAMENTE!:')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = idade + saldo
        print('Seu alistamnto será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
        ano = idade - saldo
        print('Seu alistamento foi em {}.'.format(ano))



