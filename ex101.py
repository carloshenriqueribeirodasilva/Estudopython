def voto(ano):
    from datetime import date
    atual = date.today().year

    idade = atual - ano
    if idade < 16:
        return f'Com {idade}, o voto não é obrigatorio'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}, O voto é opcional.'
    else:
        return f'Com {idade}, o voto é OBRIGATORIO'

ano = int(input('Digite o ano de seu nascimento: '))
print(voto(ano))