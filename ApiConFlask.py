#Vicente Zavala IRC9.2
from flask import Flask, jsonify

app = Flask(__name__) 
tasks = [    
{"id":1, "user":"omar", "active": True},
{"id":2, "user": "leo", "active":False},
{"id":3, "user": "luz", "active": True},
{"id":4, "user":"alan", "active":False},
{"id":5, "user":"Vicente Zavala", "active":True} 
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify (tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"No USER": "User no encontrado"}), 404

    return jsonify(task)

if __name__ == '__main__':
    app.run(debug=True)