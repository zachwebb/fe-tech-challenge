from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# Mount static images folder
app.mount("/images", StaticFiles(directory="app/images"), name="images")

# Load taco JSON
@app.get("/api/tacos")
def get_taco_data():
    with open("app/data.json") as f:
        data = json.load(f)
    return data
