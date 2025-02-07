# yolo 모델
import cv2
from ultralytics import YOLO
import os
import torch
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" #환경 변수 설정

# YOLOv8 모델 불러오기
model = YOLO('yolov8n.pt')  # YOLOv8 Nano 모델


# 모델 학습
results = model.train(
    data='D:/ai3/study/deeplearning_project/data.yaml',  # data.yaml 파일 경로
    epochs=30,  #에포크 수 조정하기 ★★
    imgsz=640,
    batch=16,
    project='D:/ai3/study/deeplearning_project',
    name='학습된 군중 데이터',
    pretrained=True,
    workers=4  # 데이터 로드 병렬 처리
)

# --------------------------------------------------군중 밀집도 분석

# 이미지 또는 비디오 경로
source = '/ai3/study/deeplearning_project/data/train/images'  # 또는 비디오 파일 경로

# 예측 실행
results = model.predict(source=source, save=True, conf=0.5)

# 결과 확인 및 경고
for result in results:
    num_people = len(result.boxes)  # 감지된 사람 수
    print(f"Detected {num_people} people.")
    
    if num_people > 30:  # 30명으로 임계값 설정
        print("⚠️ Warning: High crowd density detected!")
'''

# -------------------------------------------------실시간 경고 시스템
cap = cv2.VideoCapture(1)  # 웹캠 사용

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 예측 실행
    results = model(frame)
    
    # 결과 그리기
    annotated_frame = results[0].plot()
    
    # 경고 조건 확인
    num_people = len(results[0].boxes)
    if num_people > 10:
        cv2.putText(annotated_frame, "⚠️ High Crowd Density!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # 화면 출력
    cv2.imshow('Crowd Density Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''