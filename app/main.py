from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Add CORS middleware to allow all origins and GET method
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"], 
)

# Mount static images folder (if needed)
app.mount("/images", StaticFiles(directory="app/images"), name="images")

# Load taco JSON with a GET method
@app.get("/api/tacos")
def get_taco_data():
    with open("app/data.json") as f:
        data = json.load(f)
    return JSONResponse(content=data)  # Returning the JSON data as a response
