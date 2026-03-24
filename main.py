from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# عندما يدخل أي شخص إلى الصفحة الرئيسية، اعرض له ملف الواجهة
@app.get("/")
def read_root():
    return FileResponse("index.html")