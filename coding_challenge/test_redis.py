import redis

# Create a connection to the Redis server
redis_host = "localhost"
redis_port = 6379
try:
    connection = redis.Redis(host=redis_host, port=redis_port)
    print("Connected successfully to Redis")
except Exception as e:
    print(f"Error: {e}")
