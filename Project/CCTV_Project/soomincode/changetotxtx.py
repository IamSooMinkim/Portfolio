import os
import json

# JSON 파일 경로와 변환된 TXT 파일 경로
input_folder = "D:/AI3/study/deepLearning_project/data/labels/train"  # JSON 파일 경로
output_folder = "D:/AI3/study/deepLearning_project/data/train/labels"  # YOLO 형식 TXT 저장 폴더
os.makedirs(output_folder, exist_ok=True)

# 이미지 크기 설정 (JSON에 있는 이미지 크기 반영)
image_width = 1920
image_height = 1080

for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(root, file)
            txt_path = os.path.join(output_folder, file.replace(".json", ".txt"))

            # JSON 파일 읽기
            with open(json_path, 'r', encoding='utf-8-sig') as json_file:
                data = json.load(json_file)

            # 객체 리스트 가져오기
            objects = data["image"]["crowdinfo"]["objects"]

            # YOLO 형식으로 좌표 변환
            yolo_data = []
            for obj in objects:
                # directionindex 좌표 가져오기
                direction_index = obj["directionindex"]
                x = direction_index[0]  # x 좌표
                y = direction_index[1]  # y 좌표

                # YOLO 형식으로 정규화
                x_center = x / image_width
                y_center = y / image_height
                width = 0.02  # 임의의 너비 설정 (바운딩 박스 크기가 없는 경우)
                height = 0.02  # 임의의 높이 설정

                # 클래스 ID = 0 (사람으로 가정)
                yolo_data.append(f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

            # TXT 파일로 저장
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write("\n".join(yolo_data))

            print(f"Converted: {json_path} → {txt_path}")

print("YOLO 형식 변환 성공!")

