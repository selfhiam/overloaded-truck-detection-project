import cv2
import numpy as np
import os
from paddleocr import PaddleOCR


def perspective(image_name, coord):

    print(image_name)
    img = cv2.imread(image_name)
    w, h = 600, 400
    print(coord)
    srcQuad = np.array(coord, np.float32)
    dstQuad = np.array([[0, 0], [w, 0],[w, h],[0, h]], np.float32)

    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(img, pers, (w, h))

    save_image(dst, "pics", "perspective_image.jpg") # 이미지 저장

    return dst

# perspective된 사진을 pics에 저장
def save_image(image, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)

    save_path = os.path.join(directory, filename)

    cv2.imwrite(save_path, image)




def getOCR(dst):
    # dst 파일을 OCR로 읽어오기
    por = PaddleOCR()
    result = por.ocr(dst, cls=False)
    print(result)

    # OCR 결과가 None인 경우 처리
    if result is None or len(result) == 0:
        return ""

    # OCR 결과에서 텍스트 추출
    text = ""
    for line in result[0]:
    # line이 None이거나 비어 있는 경우를 처리
        if line is None or len(line) == 0:
            continue

    for line in result[0]:
        x1, y1 = map(int, line[0][0])
        x2, y2 = map(int, line[0][1])
        extracted_text = line[1][0]

        # 추출된 텍스트를 기존에 추출된 텍스트에 추가
        text += extracted_text + "\n"

    # 추출된 텍스트를 파일에 저장
    save_text(text, "result/result.txt")
    print(result)
    return text




# 결과값을 텍스트파일 생성,저장
def save_text(text, file_path):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(text)




