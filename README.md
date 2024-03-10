# 현재 전문가팀 Project 

## ✯ overloaded-truck-detection-project
* 도로의 CCTV를 이용하여 과적차량(트럭)을 탐지하여 과적차량의 사진 및 번호판을 인식하는 AI
* Ultralytics의 YOLOv5s모델을 사용하여 과적차량의 분석 및 탐지에 도움을 주는 서비스
* 기존 CCTV의 역활을 추가하여 제한속도 위반 뿐만 아니라 과적차량까지 실시간 동시탐지 및 안전한 도로를 위해 기획

## ☑ 과정
* 최종 프로젝트에 사용할 모델을 테스트하기 위해 YOLOv8n 과 YOLOv5, YOLOv5s, YOLOv5s6, YOLOv5l6등 많은 모델 테스트 결과 YOLOv5s를 이용하여 사용하기를 결정
* 이미지 및 라벨링 데이터 정제화
* [YOLOv5s](https://github.com/ultralytics/yolov5) 라벨링 변환 및 데이터 전처리

## ☑ 사용한 데이터
* [AIHUB 과적차량 도로 위험 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=530)
* [AIHUB 자동차 차종/연식/번호판 인식용 영상](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=172)
* 데이터 라벨링 변환 : Google Colab을 이용하여 필요한 라벨링만 추출 후 정제

# ☑ Skills
### Language
<div align="center">
    <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white" />
</div>

### AI
<div align="center">
    <img src="https://img.shields.io/badge/Opencv-5C3EE8?style=flat&logo=opencv&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/YOLO-1572B6?style=flat&logo=YOLO&logoColor=white" />
</div>

### Front-End
<div align="center">
    <img src="https://img.shields.io/badge/html-E34F26?style=flat&logo=html5&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=flat&logo=javascript&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/css-1572B6?style=flat&logo=css3&logoColor=white" />
</div>

### Back-End
<div align="center">
    <img src="https://img.shields.io/badge/fastapi-009688?style=flat&logo=fastapi&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/jinja2-B41717?style=flat&logo=Jinja&logoColor=white" />
</div>

### Tools
<div align="center">
    <img src="https://img.shields.io/badge/git-F05032?style=flat&logo=git&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/slack-4A154B?style=flat&logo=slack&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/discord-5865F2?style=flat&logo=discord&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/canva-00C4CC?style=flat&logo=canva&logoColor=white" /> <br/> <br/>
    <img src="https://img.shields.io/badge/pycharm-000000?style=flat&logo=pycharm&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/jupyter-F37626?style=flat&logo=jupyter&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=flat&logo=googlecolab&logoColor=white" /> &nbsp&nbsp
    <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat&logo=visualstudiocode&logoColor=white" /> &nbsp&nbsp
</div>

## 필요한 모듈 설치
1. pip install -r requirements.txt
* requirments.txt에 들어가있는 버전 및 모듈을 자동으로 설치를 진행합니다.

* 만약 맥북에서 paddlepaddle, paddleocr 설치 중 오류가 발생시 아래와 같이 진행하면 됩니다.
  1. brew update
  2. brew install mupdf swig
  3. pip install https://github.com/pymupdf/PyMuPDF/archive/master.tar.gz
  4. 다시 처음부터 paddlepaddle, paddleocr을 설치하면 됩니다.
  5. 다시 설치 코드 : pip install paddlepaddle, paddleocr

# 사용방법
1. 자신의 다운로드 OR git clone을 이용하여 VScode에 받습니다.
2. 터미널에서 pip install -r requirements.txt
3. cd /server
4. uvicorn main:app --reload 를 입력하여 서버를 기동합니다.
5. 터미널에서 http://127.0.0.1:8000를 ctrl + 마우스 왼쪽 클릭으로 실행합니다.<br />
만약 VScode에서 live server가 설치되어 있으면 아래와 같이 실행하면 됩니다.
* 윈도우 : client/html/index.html을 클릭 후 ALT + L + O
* 맥북 : client/html/index.html을 클릭 후 command + L + O

* 주의사항 : 맥 관련하여 서버 실행중 <br/>
"NotImplementedError: cannot instantiate 'WindowsPath' on your system"에러 발생시 <br/>

/server/model.py에서 
```
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath 
``` 
를 제거합니다.

6. 과적차량 탐지 이미지
![image](/overloaded.png)

<br/>

7. PaddleOCR로 번호판 글자 인식
