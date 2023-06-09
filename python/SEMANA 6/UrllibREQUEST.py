# O módulo urllib.request permite requisitar e
# receber recursos da Web, de modo similar a
# um navegador.
from urllib.request import urlopen

# a função urlopen:
#   -recebe como parâmetro uma URL
#   -formula uma requisição HTTP que será enviada ao servidor especificado na URL
#   -obtém e retorna uma resposta HTTP completa do servidor.
def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('https://www.uol.com.br/')
print(html)


