from flask import Flask, jsonify, request
import json
app = Flask(__name__)


#ponemos contenido en la variable todos para test
todos =[ { "label": "My first task", "done": False },
{ "label": "My first task dddddd", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos) # paso a Json los datos de la variable todos
    return json_text #los devuelvo como retorno


@app.route('/todos', methods=['POST'])
def add_new_todo():
    #Para decodificar cualquier string json y convertirlo a un objeto de python Json.loads
    datos_recibidos_decodificados = json.loads(request.data) #en request data almacenaremos los datos enviados desde el Post
    print("Datos recibidos y decodficados a Json    ---------------->", datos_recibidos_decodificados)
    #Anadimos el objeto a la lista de todos
    todos.append(datos_recibidos_decodificados)
    print(todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    print(todos)
    return "se ha eliminado una tarea"


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)