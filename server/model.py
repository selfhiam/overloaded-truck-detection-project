import cv2
import torch

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

def get_stream_video(query):
    # camera 정의
    video = cv2.VideoCapture(f'./videos/{query}')

    model = torch.hub.load('ultralytics/yolov5', 'custom', 'best2.pt')

    while (video.isOpened()):
        # 카메라 값 불러오기
        success, frame = video.read()

        if ret:
            # 모델 돌리기
            with torch.no_grad():
                prediction = model(frame)

            annotated_image = visualize_prediction(frame, prediction)
            # 객체 검출되면 폴더에 저장

            ret, buffer = cv2.imencode('.jpg', frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에
            # yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(frame) + b'\r\n')
            
def visualize_prediction(image, prediction):
    cord = prediction.xyxy[0]
    name = prediction.names
    # print(name)
    size = len(cord)
    # print(cord)
    for i in range(size - 1):
        XMin, YMin, XMax, YMax, conf, cls = cord[i, :6]
        # print(XMin, YMin, XMax, YMax)
        print(f"{name[int(cls)]} cord:", cord[i, :5])
        if int(cls) == 0:
            if conf > 0.2:  # 신뢰도가 일정 수준 이상인 객체만 표시
                cv2.rectangle(image, (int(XMin), int(YMin)), (int(XMax), int(YMax)), (0, 0, 255), 2)
                cv2.putText(image, f'{name[int(cls)]}:{conf:.2f}', (int(XMin), int(YMin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
                
    return image