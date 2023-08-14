import httpx
import json

class Task:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def model_dump(self):
        return {"title": self.title, "content": self.content}

# סימולציה של מחיקת פתק
sample_task = Task(title="My First task", content="This is the content of my first task.")
created_task_response = httpx.post("http://localhost:8000/tasks/", data=json.dumps(sample_task.model_dump()))
created_task_id = created_task_response.json().get("task_id")
if created_task_id is None:
    print("Failed to get task_id from response:", created_task_response.text)
else:
    print("task created:", created_task_id)


deleted_task_response = httpx.delete(f"http://localhost:8000/tasks/{created_task_id}")
# print(deleted_task_response.json()["message"])
print(created_task_response.text)
