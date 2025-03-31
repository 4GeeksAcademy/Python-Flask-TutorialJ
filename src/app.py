from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
#METODO GET
@app.route('/todos', methods=['GET'])
def hello_world():
    todo_text = jsonify(todos)
    return todo_text

#METODO POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_dict= request.get_json(force=True)
    todos.append(new_dict)
    todosText =jsonify(todos)
    return todosText

#METODO DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    deleteTodo = todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)