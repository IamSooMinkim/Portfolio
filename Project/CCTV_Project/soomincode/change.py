# -*- coding: utf-8 -*-
"""
JSON 파일 변환
"""

import json
import os

# 경로 설정
json_dirs = {
    'train': '/deepLearning_project/data/labels',  # 학습 라벨 JSON 폴더
    'val': '/deepLearning_project/data/labels'       # 검증 라벨 JSON 폴더
}

output_dirs = {
    'train': '/deepLearning_project/data/labels/txt_train',  # YOLO 형식 라벨 저장 폴더
    'val': '/deepLearning_project/data/labels/txt_val'
}
os.makedirs(output_dirs['train'], exist_ok=True)
os.makedirs(output_dirs['val'], exist_ok=True)

# 이미지 크기 설정 (수동 설정 또는 자동 추출)
img_width, img_height = 1280, 720

def convert_json_to_yolo(json_dir, output_dir):
    for file_name in os.listdir(json_dir):
        if file_name.endswith('.json'):
            with open(os.path.join(json_dir, file_name), 'r') as f:
                data = json.load(f)
            
            output_file = os.path.join(output_dir, file_name.replace('.json', '.txt'))
            with open(output_file, 'w') as out:
                for ann in data['annotations']:
                    class_id = ann['class']
                    x_min, y_min, width, height = ann['bbox']
                    
                    # 좌표 정규화
                    x_center = (x_min + width / 2) / img_width
                    y_center = (y_min + height / 2) / img_height
                    norm_width = width / img_width
                    norm_height = height / img_height

                    # YOLO 형식: <class> <x_center> <y_center> <width> <height>
                    out.write(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}\n")

# 라벨 변환 실행
convert_json_to_yolo(json_dirs['train'], output_dirs['train'])
convert_json_to_yolo(json_dirs['val'], output_dirs['val'])
print("✅ JSON to YOLO format conversion complete!")
