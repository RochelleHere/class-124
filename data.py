from flask import Flask, jsonify, request
app=Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide data"
    },400)
    task={
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description",""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })
@app.route("/get-data")
def getTask():
    return jsonify({
        "data": tasks
    })
app.run(debug=True)
