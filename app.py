#1. objetivo - criar api p consultar, criar, editar e excluir livros
#2. url base - localhost
#3. endpoints:
#  - localhost/livros (GET)
#  - localhost/livros (POST)
#  - localhost/livros/id (GET)
#  - localhost/livro/id (PUT)
#  - localhost/livro/id (DELETE)

#4. quais recursos - livros


#No Prompt: pip install flask

from flask import Flask, jsonify, request
#request serve pra acessar os dados q estao indo e vindo dentro das requisiçoes

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Habitos atomicos'
    },
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    #retornas as infos do usuario q foram enviadas p api
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])   
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def exlcuir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)