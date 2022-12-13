cidade = str(input('Em que cidade você nasceu?: ')).strip() # elimina os espaços, caso o usuario coloque espaço antes de digitar o texto
print(cidade[:5].upper() == 'SANTO' ) # upper deixa todas as letras em maiuscula pra facilitar a analize do texto
