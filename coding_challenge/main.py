from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import DB

# Define the data model for tasks
class Task(BaseModel):
    title: str
    description: str

# Create a FastAPI instance
app = FastAPI()

# Endpoint to create a new task
@app.post("/create_task/")
async def create_task(title: str, description: str):
    DB.db_create_task(title, description)
    return {"message": "Task created successfully"}

# Endpoint to retrieve all tasks
@app.get("/get_tasks/")
async def get_tasks():
    tasks_list = DB.db_get_tasks()
    formatted_tasks = '\n'.join(tasks_list)
    return formatted_tasks

# Endpoint to remove a task
@app.delete("/remove_task/") 
async def remove_task(title: str, description: str):
    print(f"remove_task: title={title}, description={description}")
    removed_count = DB.db_remove_task(title, description)
    if removed_count > 0:
        return {"message": "Task removed successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")