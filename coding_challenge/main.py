from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []  #List: Tuple (title, description)

@app.post("/create_task/")
async def create_task(title: str, description: str):
    task = (title, description)
    tasks.append(task)
    return {"message": "Task created successfully"}


@app.get("/get_tasks/")
async def get_tasks():
    if not tasks:
        return "No tasks to perform"
    formatted_tasks = ' \n '.join([f"title: {title} - description: {description}" for title, description in tasks])
    return formatted_tasks


@app.delete("/remove_task/{title}/{description}")  # Notice the URL parameters
async def remove_task(title: str, description: str):
    if not tasks:
        return {"message": "No tasks to remove"}

    task_to_remove = (title, description)
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        return {"message": "Task removed successfully", "removed_task": task_to_remove}
    else:
        raise HTTPException(status_code=404, detail="Task not found")





