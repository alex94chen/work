from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import uuid

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)


class Task(BaseModel):
    title: str
    description: str

@app.post("/task/")
def create_task(task: Task):
    # אולי יותר ברור כך \ דרך נוספת
    # def create_task(self: Task, task: Task):
    # id = str(uuid.uuid4()) 
    # key = id
    # r.set(key, note.json())
    # return {"message": "Task created successfully"}
    key = str(uuid.uuid4())
    r.set(key, f"{task.title}_{task.description}")
    return f"Task: {task.title} created with description: {task.description}"

   
@app.get("/tasks/")
def get_tasks():
    keys = r.keys("task_*")
    tasks = []
    for key in keys:
        task_data = r.get(key).decode('utf-8')
        task = Task.parse_raw(task_data)
        tasks.append(task.dict())
    return tasks

@app.delete("/tasks/delete")
def delete_task(task: Task):
    keys = r.keys()
    for key in keys:
        id = key.decode("utf-8")
        




# סימולציה של יצירת פתק ומחיקתו
sample_task = Task(title="My First Task", description="This is the description of my first task.")
created_task_response = app.post("/tasks/", json=sample_task.dict())
created_task_id = created_task_response.json()["task_id"]

print("Task created:", created_task_id)

deleted_task_response = app.delete(f"/tasks/{created_task_id}")
print(deleted_task_response.json()["message"])