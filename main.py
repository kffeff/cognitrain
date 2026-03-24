from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv
import os
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExerciseResult(BaseModel):
    skill_name: str
    accuracy: float
    avg_response_time: int
    level: int

def save_to_csv(data: ExerciseResult):
    file_name = 'cognitrain_results.csv'
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['التاريخ والوقت', 'المهارة', 'الدقة %', 'السرعة ms', 'المستوى'])
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, data.skill_name, data.accuracy, data.avg_response_time, data.level])

# --- التعديل الأهم: جعل الرابط الرئيسي يفتح الواجهة الفخمة ---
@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/api/save-result")
def save_result(result: ExerciseResult):
    save_to_csv(result)
    print(f"\n✅ تم تسجيل نتيجة جديدة: {result.skill_name} | دقة: {result.accuracy}%")
    return {"status": "success"}