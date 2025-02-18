from flask import Flask, jsonify, request

app = Flask(__name__)

# Una lista para almacenar elementos 
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Ruta para recuperar la lista de todos
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

# Ruta para añadir items a todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Obtener datos JSON del cuerpo de solicitud
    request_body = request.json
    
    # Añadir el nuevo elemento todo a la lista de todos
    todos.append(request_body)
    
    # Devolver la lista de todos actualizada como una respuesta JSON
    json_text = jsonify(todos)
    return json_text

#Pedir ayuda en clase (eliminar elemento,devolver lista act)


# Ruta para eliminar un elemento todo en una posición específica
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Eliminar el elemento en la posición especificada en la lista de todos
    todos.pop(position)
    
    # Devolver la lista de todos actualizada como una respuesta JSON
    json_text = jsonify(todos)
    return json_text

# (((((APUNTE IMPORTANTE)))))Estas dos líneas siempre deben estar al final de su archivo app.py para iniciar la aplicación Flask
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)