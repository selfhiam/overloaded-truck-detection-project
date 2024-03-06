from fastapi import FastAPI, Request, Response, File, UploadFile, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from typing import List
from model import get_stream_video
import shutil
import os
import cv2
# import numpy as np
# import base64


app = FastAPI()


templates = Jinja2Templates(directory='../client/html')
app.mount("/js", StaticFiles(directory="../client/js"), name="js")
app.mount("/css", StaticFiles(directory='../client/css'), name='css')


origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
]

# 모든 출처 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# model.py에서 이미지 불러오는 함수
def video_streaming():
    return get_stream_video()

# index 페이지 로드
@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('index.html', context={'request':request})


folder_name = "videos"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

UPLOAD_DIRECTORY = "./videos"
@app.post("/upload_video")
async def upload_video(video: UploadFile = File(...)):
    # 업로드된 파일의 경로
    upload_path = os.path.join(UPLOAD_DIRECTORY, video.filename)
    # 업로드된 파일을 서버에 저장
    with open(upload_path, "wb") as f:
        content = await video.read()
        f.write(content)
    print('동영상이 업로드 되었습니다')
    # 저장된 파일의 경로 반환
    return {"filename": video.filename, "saved_path": upload_path}

   
# 파일 업로드 POST 반응
@app.get("/video/")
async def videoStream(request: Request, query: str = Query(...)):
    # print(query)
    return StreamingResponse(get_stream_video(query), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/images")
async def send_images(request: Request, q: int = Query(...)):
    overload_folders = os.listdir('overload')
    img_cnt = len(overload_folders)

    if q < img_cnt:
        img_dir = os.path.join('overload', overload_folders[q])
        imgs = os.listdir(img_dir)
        img = cv2.imread(os.path.join(img_dir, imgs[0]))

        return FileResponse(os.path.join(img_dir, imgs[0]), media_type='image/jpg')