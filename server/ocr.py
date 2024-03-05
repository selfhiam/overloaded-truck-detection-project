from fastapi import FastAPI
from fastapi.responses import FileResponse
from paddle import perspective, getOCR
import os
import cv2

app = FastAPI()

image_path = 'pics'
image_name = '2024-03-04-15-54-12.jpeg'
coord = [[290,930],[375,930],[375,970],[290,970]]

def evaluate_ocr(image_path):
    # 이미지 처리
    perspective_image = perspective(image_path, coord)
    plate_text = getOCR(perspective_image)

    # OCR 결과 평가 (텍스트 길이)
    score = len(plate_text)
    return score

@app.get("/pics")
async def get_pics():
    # pics 폴더에서 이미지 파일 목록 가져오기
    pics_dir = "./pics"
    image_names = os.listdir(pics_dir)

    # OCR 결과가 가장 좋은 이미지 찾기
    best_image_name = None
    best_score = float('-inf')  # 초기화: 음수 무한대
    for image_name in image_names:
        image_path = os.path.join(pics_dir, image_name)
        score = evaluate_ocr(image_path)
        if score > best_score:
            best_score = score
            best_image_name = image_names

    # 가장 좋은 이미지 선택
    best_image_path = os.path.join(pics_dir, best_image_name)

    # 선택된 이미지 처리
    perspective_image = perspective(best_image_path, coord)
    plate_text = getOCR(perspective_image)
    
    # 처리된 이미지 저장
    processed_image_path = os.path.join(pics_dir, "processed_" + best_image_name)
    cv2.imwrite(processed_image_path, perspective_image)
    
    return {"processed_image_path": processed_image_path, "plate_text": plate_text}



@app.get("/info")
async def send_info():
    # pics 폴더에서 이미지 파일 목록 가져오기
    pics_dir = "pics"
    image_names = os.listdir(pics_dir)

    # OCR 결과가 가장 좋은 이미지 찾기
    best_image_name = None
    best_score = float('-inf')  # 초기화: 음수 무한대
    for image_name in image_names:
        image_path = os.path.join(pics_dir, image_name)
        score = evaluate_ocr(image_path)
        if score > best_score:
            best_score = score
            best_image_name = image_name

    # 가장 좋은 이미지 선택
    best_image_path = os.path.join(pics_dir, best_image_name)

    # 선택된 이미지 처리
    perspective_image = perspective(best_image_path)
    plate_text = getOCR(perspective_image)

    # 이미지 이름 가져오기 (날짜와 시간)
    image_name = os.path.splitext(best_image_name)[0]

    return {
        "best_image_name": best_image_name,
        "perspective_image": perspective_image,
        "plate_text": plate_text,
        "image_name": image_name
    }
