import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro')
else:
    print('funcionou')
    print(site.read()) # tem acesso a todos os codigos HTML do site