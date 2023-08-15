from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()
# Connect to the Redis database
redis_db = redis.StrictRedis(host='my_red', port=6379, db=0, decode_responses=True) 


@app.post("/create_task/")
async def create_task(title: str, description: str):
    task = (title, description)
    # Store the task in the Redis database
    redis_db.rpush("tasks", str(task))    
    return {"message": "Task created successfully"}

@app.get("/get_tasks/")
async def get_tasks():
    # Retrieve tasks from the Redis database
    formatted_tasks = '\n'.join(redis_db.lrange("tasks", 0, -1))
    return formatted_tasks




@app.delete("/remove_task/{title}/{description}") 
async def remove_task(title: str, description: str):
    task_to_remove = (title, description)
    # Remove task from the Redis database
    removed_count = redis_db.lrem("tasks", 1, str(task_to_remove))
    if removed_count > 0:
        return {"message": "Task removed successfully", "removed_task": task_to_remove}
    else:
        raise HTTPException(status_code=404, detail="Task not found")





