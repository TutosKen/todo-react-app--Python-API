from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import json
from Classes.Task import Task

app = Flask(__name__)
cors = CORS(app)

tasks = []

def generateID():
    id = 0
    if tasks:
        id = tasks[-1].id + 1
    return id

@app.route('/', methods=['GET'])
def hello():
    return 'Welcome to my Flask API'

@app.route('/addTask', methods=['POST'])
@cross_origin()
def addTask():
    id = generateID()
    req_json = request.json
    name = req_json['name']
    task = Task(id,name)

    try:
        tasks.append(task)
        print(tasks)
        return str(task.id), 200
    except Exception as e:
        return f"Error while adding task: {e}", 500


@app.route('/completeTask/<ID>', methods=['POST'])
@cross_origin()
def completeTask(ID):
    for task in tasks:
        if int(task.id) == int(ID):
            task.completed = not task.completed

            return "Task updated successfully", 200

    return "Error while updating task", 500
    

@app.route('/removeTask/<ID>', methods=['POST'])
@cross_origin()
def removeTask(ID):
    flag = False
    for task in tasks:
        if int(task.id) == int(ID):
            tasks.remove(task)
            flag = True
    
    if flag:
        return "Task removed succesfully", 200
    
    return "Error while removing task", 500

@app.route('/getTasks', methods=['GET'])
@cross_origin()
def getTasks():
    json_list = json.dumps([item.__dict__ for item in tasks])
    return json_list

@app.route('/getTask/<ID>', methods=['GET'])
@cross_origin()
def getTask(ID):
    for task in tasks:
        if int(task.id) == int(ID):
            task = json.dumps(task.__dict__)
            return task

    return "Task does not exist", 404

@app.route('/test', methods=['POST'])
@cross_origin()
def test():
    req_json = request.json
    return req_json['name']





if __name__ == '__main__':
    app.run(debug=True)