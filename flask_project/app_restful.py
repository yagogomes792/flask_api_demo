from flask import Flask, json, request
from flask_restful import Resource, Api
from tarefas import AddTarefas, UpdateTarefas

#Exemplo de criação de APIs utilizando flask Restful para deixar o código mais limpo
app = Flask(__name__)
api = Api(app)

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
#classe para retornar, atualizar e deletar os dados
class Tarefas(Resource):
    #método get
    def get(self, id):
        try:
            #variável que guarda o id da lista
            response = tarefas[id]
            #retorna a variável com os dados da lista
            return response
        except Exception:
            #caso ocorra um erro informa essa mensagem
            return {'status':'Erro', 'mensagem':'Id inexistente, entrar em contato com o adm'}
    #método put
    def put(self, id):
        try:
            #variável que guarda os dados enviados via request e transforma em JSON
            dados = json.loads(request.data)
            #pega o id e status da tarefa e recebe somente a alteração do status fazendo a alteração do mesmo
            tarefas[id]["status"] = dados["status"]
            #retorna os dados com o novo status
            return dados
        except:
            #caso ocorra um erro informa essa mensagem
            return {'status':'Erro', 'mensagem':'Problema ao alterar o status'}
    #método delete
    def delete(self):
        try:
            #exclui uma tarefa pelo id informado
            tarefas.pop(id)
            #retorna mensagem de sucesso caso o item seja excluido
            return {'status':'sucesso', 'mensagem':'tarefa excluida'}
        except:
            #retorna erro caso ocorra algum problema
            return {'status':'Erro', 'mensagem':'Ocorreu um problema ao excluir a tarefa, contate o adm'}

#classe para listar e adicionar dados
class ListaTarefas(Resource):
    #método get
    def get(self):
        return tarefas
    #método post
    def post(self):
        try:
            #variável que guarda os dados enviados via request e transforma em JSON 
            dados = json.loads(request.data)
            #guarda o tamanho da lista na variável posição
            posicao = len(tarefas)
            #recebe os dados por id e guarda na variável posição
            dados['id'] = posicao
            #variavel que recebe os dados de tarefa
            tarefa_recebida = dados['tarefa']
            #variavel que recebe a tarefa que está guardada na variavel (d) e faz iteração para verificar se já existe a tarefa na lista 
            lista_tarefa = [d['tarefa'] for d in tarefas]
            #se a tarefa enviada por request não existir na lista então será adicionada
            if tarefa_recebida not in lista_tarefa:
                #adiciona os dados na lista
                tarefas.append(dados)
                #retorna a lista com as posições
                return tarefas[posicao]
            #caso contrário será informado que a tarefa já existe
            else:
                return {'message':'Essa tarefa já existe'}
        except:
            #caso ocorra erro informa essa mensagem
            return {'status':'Erro', 'mensagem':'Problema ao inserir tarefa'}

#Rota para acessar as APIs
api.add_resource(Tarefas, '/tarefas/<int:id>')
api.add_resource(ListaTarefas, '/tarefas/')
api.add_resource(AddTarefas, '/tasks/')
api.add_resource(UpdateTarefas, '/tasks/<int:id>')


if __name__ == "__main__":
    app.run(debug=True)



