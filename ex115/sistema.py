from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteudo de um arquivo!
        lerArquivo(arq)
        sleep(1)
        cabeçalho('Opção 1')

    elif resposta == 2:
        # opçao de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
        cabeçalho('Opção 2')

    elif resposta == 3:
        # opçao de sair do sistema
        sleep(2)
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        # Digitou uma opção errada no menu.
        sleep(1.5)
        print('\033[31mERRO! Digite uma opção valida!\033[m')
