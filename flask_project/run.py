from flask import Flask, request, jsonify
import json

#inicio da aplicação
app = Flask(__name__)

#Lista com dicionários simulando dados de um DB
tarefas = [
    {
    "id":0,
    "responsavel": "Yago",
    "tarefa":"criar API",
    "status":"concluido"
    },
    {
    "id": 1,
    "responsavel": "Gomes",
    "tarefa":"criar integracoes",
    "status":"pendente"
    }
]
#função para buscar, atualizar e excluir dados da lista
@app.route('/tarefas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tasks(id):
    if request.method == 'GET':
        try:
            #variável que guarda o id da lista
            response = tarefas[id]
            #retorna a variável com os dados da lista
            return jsonify(response)
        except Exception:
            #caso ocorra um erro informa essa mensagem
            return jsonify({'status':'Erro', 'mensagem':'Id inexistente, entrar em contato com o adm'})
    elif request.method == 'PUT':
        try:
            #variável que guarda os dados enviados via request e transforma em JSON
            dados = json.loads(request.data)
            #pega o id e status da tarefa e recebe somente a alteração do status fazendo a alteração do mesmo
            tarefas[id]["status"] = dados["status"]
            #retorna os dados com o novo status
            return jsonify(dados)
        except:
            #caso ocorra um erro informa essa mensagem
            return jsonify({'status':'Erro', 'mensagem':'Problema ao alterar o status'})
    elif request.method == 'DELETE':
        try:
            #exclui uma tarefa pelo id informado
            tarefas.pop(id)
            #retorna mensagem de sucesso caso o item seja excluido
            return jsonify({'status':'sucesso', 'mensagem':'tarefa excluida'})
        except:
            #retorna erro caso ocorra algum problema
            return jsonify({'status':'Erro', 'mensagem':'Ocorreu um problema ao excluir a tarefa, contate o adm'})

#funcção para adicionar e listar os dados
@app.route('/tarefas/', methods=['POST', 'GET'])
def new_task():
    if request.method == 'POST':
        try:
            #variável que guarda os dados enviados via request e transforma em JSON 
            dados = json.loads(request.data)
            #guarda o tamanho da lista na variável posição
            posicao = len(tarefas)
            #recebe os dados por id e guarda na variável posição
            dados['id'] = posicao
            #adiciona os dados na lista
            tarefas.append(dados)
            #retorna a lista com as posições
            return jsonify(tarefas[posicao])
        except:
            #caso ocorra erro informa essa mensagem
            return jsonify({'status':'Erro', 'mensagem':'Problema ao inserir tarefa'})
    elif request.method == 'GET':
        #retorna a lista completa
        return jsonify(tarefas)
#executa a função somente neste módulo
if __name__ == "__main__":
    #debug = true reinicia o app automaticamente
    app.run(debug=True)