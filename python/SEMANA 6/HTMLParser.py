# O módulo html.parser, por meio da classe HTMLParser, permite processar elementos HTML de uma página Web.
from html.parser import HTMLParser

# O método feed() da classe HTMLParser recebe como entrada uma página HTML no formato string,
# e para cada 'token' lido (tags de início, tags de fim, texto, etc.), executa um handler correspondente.
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('https://www.uol.com.br/')
parser = MyParser()
parser.feed(html)
