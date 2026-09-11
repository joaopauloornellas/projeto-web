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

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de Idade'

    else:
        status = 'Menor de Idade - ACESSO NEGADO'

    return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)    

@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4, 
    }
    return render_template('dicio.html', **dados)

@app.route('/condicao/<int:numero>')
def condicao(numero):
    
    return render_template('condicao.html', numero = numero)

@app.route('/perfil/<nome>')
def perfil(nome):

    
    usuarios = {
        'admin' : {
            'nome' : 'Administrador',
            'email': 'admin@fatec.br',
            'nivel': 'administrador',
            'ativo': True,
            'posts': 47
        },

        'joao': {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'nivel': 'usuario',
            'ativo': True,
            'posts': 12
        }, 

         
        'maria': {
            'nome': 'Maria Souza',
            'email': 'maria@email.com',
            'nivel': 'moderador',
            'ativo': False,
            'posts': 31
        }
    }

    usuario = usuarios.get(nome)

    return render_template('perfil.html', usuario=usuario, nome_buscado=nome)




# ---Ultima coisa do arquivo, sempre escrever ela por ultimo---
if __name__ == '__main__':
    app.run(debug=True)

