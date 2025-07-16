import json
import sys
import os
import datetime


def manage_db():
    if not os.path.exists(database_path):
        os.mknod(database_path)
        data = {"tasks": []}
    else:
        with open(database_path, "r") as file:
            data = json.load(file)
    
    return data

def add(task):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = manage_db()
    try:
        last_id = data["tasks"][-1]["id"]
    except:
        last_id = 0
    id = last_id + 1

    info = {
        "id": id,
        "description": task,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    data['tasks'].append(info)
    with open(database_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Task added successfully (ID:{id})")

def update(task_id, new_description):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = manage_db()
    for task in data.get("tasks", []):
        if task["id"] == int(task_id):
            task["description"] = new_description
            task["updatedAt"] = now
            print("Task updated successfully ")
    with open(database_path, "w") as file:
        json.dump(data, file, indent=4)
 
def remove(task_id):
    data = manage_db()

    tasks = data.get("tasks", [])
    new_tasks = [task for task in tasks if int(task["id"]) != int(task_id)]

    if len(new_tasks) == len(tasks):
        print(f"Task with ID: {task_id} not found")
    else:
        data["tasks"] = new_tasks
        print("Task deleted successfully")
        with open(database_path, "w") as file:
            json.dump(data, file, indent=4)

def change_status(task_id, new_status):
    data = manage_db()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for task in data.get("tasks", []):    
        if task["id"] == int(task_id):
            task["status"] = new_status
            task["updatedAt"] = now
            print("Status updated successfully")

    with open(database_path, "w") as file:
        json.dump(data, file, indent=4)


def task_list(status=None):
    data = manage_db()
    tasks = data.get("tasks", [])

    print("ID ---------- Task Name ---------- Status ---------- createdAt -------------------- updatedAt")
    for task in tasks:
        if status == None:
            print(f"{task["id"]} ---------- {task["description"]} ---------- {task["status"]} ---------- {task["createdAt"]} ---------- {task["updatedAt"]}")
        elif status == 'done':
            if task['status'] == 'done':
                print(f"{task["id"]} ---------- {task["description"]} ---------- {task["status"]} ---------- {task["createdAt"]} ---------- {task["updatedAt"]}")
        elif status == 'todo':
            if task["status"] == "todo":
                print(f"{task["id"]} ---------- {task["description"]} ---------- {task["status"]} ---------- {task["createdAt"]} ---------- {task["updatedAt"]}")
        elif status == "in-progress":
            if task["status"] == "in-progress":
                print(f"{task["id"]} ---------- {task["description"]} ---------- {task["status"]} ---------- {task["createdAt"]} ---------- {task["updatedAt"]}")

args = sys.argv

arg1 = args[1] if len(args) > 1 else None
arg2 = args[2] if len(args) > 2 else None
arg3 = args[3] if len(args) > 3 else None


database_path="database.json"

if arg1 == 'add':
    if type(arg1) != str:
        print("Usage python3 add <string>")
        sys.exit(1)
    add(arg2)
elif arg1 == 'update':
    update(arg2,arg3)
elif arg1 == 'remove':
    remove(arg2)
elif arg1 == "mark-todo":
    change_status(arg2,"todo")
elif arg1 == "mark-in-progress":
    change_status(arg2,"in-progress")
elif arg1 == "mark-done":
    change_status(arg2,"done")
elif arg1 == 'list':
    if arg2 == "done":
        task_list("done")
    elif arg2 == "todo":
        task_list("todo")
    elif arg2 == "in-progress":
        task_list("in-progress")
    else:
        task_list()
