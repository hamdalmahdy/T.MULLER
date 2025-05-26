from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import shutil
import random

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# This is a simple fake detector (we'll replace it later)
def fake_detector(video_path):
    score = random.uniform(0, 1)  # Random number between 0 and 1
    return score

@app.post("/detect/")
async def detect_video(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    score = fake_detector(file_location)

    return JSONResponse(content={
        "filename": file.filename,
        "fake_score": round(score, 2),
        "likely_fake": score > 0.5
    })
