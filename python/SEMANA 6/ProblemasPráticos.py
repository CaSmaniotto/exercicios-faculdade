# Problema Prático 11.1

# Escreva o método news() que aceita um URL de um site Web de notícias e uma lista de tópicos de notícias
# (ou seja, strings) e calcula o número de ocorrências de cada tópico nas notícias.
# news('http://bbc.co.uk',['economy','climate','education'])
# retorna:  economy appears 3 times.
#           climate appears 3 times.
#           education appears 1 times.

from urllib.request import urlopen

def news(url, topicos):
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()

    for topico in topicos:
        n = content.count(topico)
        print(f'O tópico {topico} aparece {n} vezes')

news('https://www.bbc.com/',['sport','climate','education'])

# Problema Prático 11.2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.i = 0

    def handle_starttag(self, tag, attrs):
        self.i += 4
        print(self.i*'', tag)

    def handle_endtag(self, tag):
        self.i -= 4
        print(self.i*'', tag)


infile = open('/Users/smani/PycharmProjects/Univesp/SEMANA 6/generico.html')
content = infile.read()
infile.close()
myparser = MyHTMLParser()
myparser.feed(content)


