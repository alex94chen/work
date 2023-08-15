import redis

# Connect to the Redis database
redis_db = redis.StrictRedis(host='my_red', port=6379, db=0, decode_responses=True) 

# This can be used for resetting the database when needed.
#redis_db.flushall() 

# Store the task in the Redis database
def db_create_task(title: str,description: str):
    new_task = (title, description)
    redis_db.rpush("tasks", str(new_task)) 

# Retrieve tasks from the Redis database
def db_get_tasks():
    return redis_db.lrange("tasks", 0, -1)


# Remove task from the Redis database
def db_remove_task(title: str, description: str):
    print(f"db_remove_task: title={title}, description={description}")
    task_to_remove = (title, description)
    removed_count = redis_db.lrem("tasks", 1, str(task_to_remove))
    return removed_count
