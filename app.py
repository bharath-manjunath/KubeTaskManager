# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS  # Import the CORS extension

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Boolean, default=False)

# @app.route('/tasks', methods=['GET', 'POST'])
# def handle_tasks():
#     if request.method == 'GET':
#         tasks = Task.query.all()
#         tasks_list = [{'id': task.id, 'content': task.content, 'completed': task.completed} for task in tasks]
#         return jsonify({'tasks': tasks_list})
    
#     elif request.method == 'POST':
#         data = request.get_json()
#         new_task = Task(content=data['content'])
#         db.session.add(new_task)
#         db.session.commit()
#         return jsonify({'message': 'Task added successfully'}), 201

# @app.route('/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = Task.query.get_or_404(task_id)
#     data = request.get_json()
#     task.content = data['content']
#     db.session.commit()
#     return jsonify({'message': 'Task updated successfully'})

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)



from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        tasks_list = [{'id': task.id, 'content': task.content, 'completed': task.completed} for task in tasks]
        return jsonify({'tasks': tasks_list})
    
    elif request.method == 'POST':
        data = request.get_json()
        new_task = Task(content=data['content'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully'}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def handle_single_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'PUT':
        data = request.get_json()
        task.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
