import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

# cep = "17380000"
#
# cep.replace("-", "").replace(".", "").replace(" ", "")
#
# if len(cep) == 8:
#     link = f"https://viacep.com.br//ws/{cep}/json/"
#
#     requisicao = requests.get(link)
#
#     dic_requisicao = requisicao.json()
#
#     for key, value in dic_requisicao.items():
#         print(key, ' : ', value)
# else:
#     print("CEP Inválido")
