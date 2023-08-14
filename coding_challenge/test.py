import httpx

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def model_dump(self):
        return {"title": self.title, "content": self.content}

# סימולציה של מחיקת פתק
sample_note = Note(title="My First Note", content="This is the content of my first note.")
created_note_response = httpx.post("http://localhost:8000/notes/", json=sample_note.model_dump())
created_note_id = created_note_response.json()["note_id"]

print("Note created:", created_note_id)

deleted_note_response = httpx.delete(f"http://localhost:8000/notes/{created_note_id}")
print(deleted_note_response.json()["message"])
