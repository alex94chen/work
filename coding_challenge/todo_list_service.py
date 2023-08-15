from fastapi import FastAPI, HTTPException
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = FastAPI()

# Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)  # Replace with your actual credentials file path
client = gspread.authorize(credentials)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1heGf4FS1UirXhZLCSclCgzQRtF3OFILns_D1_fk3q3Q/edit?usp=sharing").sheet1  # Use your Google Sheets URL

@app.post("/create_task/")
async def create_task(title: str, description: str):
    task = (title, description)
    # Store the task in the Google Sheet
    sheet.insert_row(list(task), 2)  # Insert the task in the second row
    return {"message": "Task created successfully"}

@app.get("/get_tasks/")
async def get_tasks():
    # Retrieve tasks from the Google Sheet
    tasks = sheet.get_all_records()
    return tasks

@app.delete("/remove_task/")
async def remove_task(title: str, description: str):
    tasks = sheet.get_all_records()
    for task in tasks:
        if task["Title"] == title and task["Description"] == description:
            sheet.delete_row(tasks.index(task) + 2)  # Delete the row (offset by 2)
            return {"message": "Task removed successfully", "removed_task": task}
    raise HTTPException(status_code=404, detail="Task not found")
