from flask import Flask, json, request
from flask_restful import Api, Resource

#módulo que faz integração com o "app_restful.py"

#lista de tarefas a ser editada
newTarefas = [{'id':0, 'tarefa':'Aprender Flask'},
{'id':1, 'tarefa':'Aprender Django'},
{'id':2, 'tarefa':'Aprender Docker'}
]
#classe responsável por retornar tarefas por id, atualizar e deletar as tarefas da lista por id
class UpdateTarefas(Resource):
    def get(self, id):
        response = newTarefas[id]
        return response

    def put(self, id):
        dados = json.loads(request.data)
        newTarefas[id]['tarefa'] = dados['tarefa']
        return dados

    def delete(self, id):
        newTarefas.pop(id)
        return {'Message':'Tarefa excluida com sucesso'}
#classe responsável por retornar toda a lista e incluir nova tarefa
class AddTarefas(Resource):
    def get(self):
        response = newTarefas
        return response

    def post(self):
        dados = json.loads(request.data)
        #guarda na variavel posicao o tamanho da lista
        posicao = len(newTarefas)
        #variavel dados na chave "id" recebe posicao da lista
        dados['id'] = posicao
        #variavel que recebe os dados de tarefa
        tarefa_recebida = dados['tarefa']
        #variavel que recebe a tarefa que está guardada na variavel (d) e faz iteração para verificar se já existe a tarefa na lista 
        listagem_tarefas = [d['tarefa'] for d in newTarefas]
        #se a tarefa enviada por request não existir na lista então será adicionada
        if tarefa_recebida not in listagem_tarefas:
            newTarefas.append(dados)
            return newTarefas[posicao]
        #caso contrário será informado que a tarefa já existe
        else:
            return {'Message':'Essa tarefa já existe'}