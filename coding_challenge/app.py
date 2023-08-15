from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []  # מערך לאחסון המשימות

@app.post("/create_task/")
async def create_task(title: str, description: str):
    tasks.append({"title": title, "description": description})
    return {"message": "Task created successfully"}

@app.get("/get_tasks/")
async def get_tasks():
    return tasks

@app.delete("/remove_task/")
async def remove_task(task_index: int):
    if task_index >= 0 and task_index < len(tasks):
        tasks.pop(task_index)
        return {"message": "Task removed successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid task index")
