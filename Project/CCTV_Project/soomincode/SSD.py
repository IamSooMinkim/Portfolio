import torch
import torch.nn as nn
from torchvision.datasets import VOCDetection
from torch.utils.data import DataLoader
from torchvision.transforms import transforms
import torch.optim as optim

# 데이터 경로 지정
DATA_PATH = '/ai3/study/deeplearning_project/data_SSD'

# 데이터 전처리 정의
transform = transforms.Compose([
    transforms.Resize((300, 300)),  # SSD 입력 크기
    transforms.ToTensor()          # 이미지를 텐서로 변환
])

# 데이터셋 로드
dataset = VOCDetection(
    root=DATA_PATH, 
    year='2012', 
    image_set='train', 
    download=False,  # 다운로드 비활성화
    transform=transform
)

VOC_CLASSES = { "서울망원시장001":1 }


# 데이터 로더 정의
def collate_fn(batch):
    #배치 데이터에서 이미지와 어노테이션을 처리하는 함수
    images, targets = zip(*batch)  # 이미지와 어노테이션 분리

    # targets에서 'labels'와 'boxes' 추출
    processed_targets = []
    for target in targets:
        labels = [VOC_CLASSES[obj['name']] for obj in target['annotation']['object']]
        boxes = [
            [
                int(obj['bndbox']['xmin']),
                int(obj['bndbox']['ymin']),
                int(obj['bndbox']['xmax']),
                int(obj['bndbox']['ymax'])
            ]
            for obj in target['annotation']['object']
        ]
        processed_targets.append({
            'labels': torch.tensor(labels, dtype=torch.long),
            'boxes': torch.tensor(boxes, dtype=torch.float)
        })

    return torch.stack(images), processed_targets

data_loader = DataLoader(
    dataset,
    batch_size=8,
    shuffle=True,
    collate_fn=collate_fn
)

# SSD 모델 정의
class SSD(nn.Module):
    def __init__(self, num_classes):
        super(SSD, self).__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.classifier = nn.Conv2d(256, num_classes, kernel_size=3, padding=1)
        self.regressor = nn.Conv2d(256, 4, kernel_size=3, padding=1)  # 바운딩 박스 좌표

    def forward(self, x):
        features = self.backbone(x)
        class_preds = self.classifier(features)
        bbox_preds = self.regressor(features)
        return class_preds, bbox_preds

# 모델 초기화
num_classes = 21  # VOC 클래스 수
model = SSD(num_classes=num_classes)

# 손실 함수 및 옵티마이저
criterion_cls = nn.CrossEntropyLoss()
criterion_loc = nn.SmoothL1Loss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)


# 학습 루프
num_epochs = 2  # epochs 수 조정
for epoch in range(num_epochs):
    for images, targets in data_loader:
        optimizer.zero_grad()
        class_preds, bbox_preds = model(images)

        # 'labels'와 'boxes'를 추출
        labels = [target['labels'] for target in targets]
        boxes = [target['boxes'] for target in targets]

        # 텐서로 변환
        labels = torch.cat(labels).view(-1)
        boxes = torch.cat(boxes).view(-1, 4)

        # 손실 계산
        loss_cls = criterion_cls(class_preds.view(-1, num_classes), labels)
        loss_loc = criterion_loc(bbox_preds, boxes)
        loss = loss_cls + loss_loc

        loss.backward()
        optimizer.step()

        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")


