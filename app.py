from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

print(__name__)

@app.route('/')
def inicio():
    return '<h1>Vai Corinthians</h1>'

@app.route('/sobre')
def sobre():
    return '''
    <h1 style='color:blue'>Meu nome é: </h1>
    <p> João Paulo <b>Ornellas</b>
    <!-- Tudo que eu pensar em html pode vir aqui, inclusive imagens, links, etc -->
    
    '''

@app.route('/var')
def variavel():
    palavra = 'Joao'
    return f'<h1>Adicionando texto de var: {palavra}'

@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Voê tem {calculoIdade} anos'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto [{nome}] com sucesso!'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/Historia')
def historia():
    return f'Essa é a hitória do Corinthians!'

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de Idade'
    else:
        status = 'Menor de Idade - ACESSO NEGADO'

    return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)    



 


# ---Ultima coisa do arquivo, sempre escrever ela por ultimo---
if __name__ == '__main__':
    app.run(debug=True)

