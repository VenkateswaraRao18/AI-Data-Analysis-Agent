from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from fastapi.staticfiles import StaticFiles

from agent.executor import DataAnalysisAgent

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/reports", StaticFiles(directory="reports"), name="reports")

UPLOAD_FOLDER = "uploaded_datasets"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

agent = DataAnalysisAgent()


@app.get("/")
def home():
    return {"message": "Data Analysis AI Agent API"}


@app.post("/analyze")
async def analyze_dataset(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    agent.analyze_dataset(file_path)

    return {
        "status": "success",
        "message": "Dataset analyzed successfully",
        "report_url": "http://127.0.0.1:8000/reports/data_report.md"
    }