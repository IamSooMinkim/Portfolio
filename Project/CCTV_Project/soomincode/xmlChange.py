import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def json_to_pascal_voc(json_file, output_dir):
    # JSON 파일 로드
    with open(json_file, "r") as f:
        data = json.load(f)
    
    # 출력 디렉토리 생성
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Directory created: {output_dir}")
        except PermissionError as e:
            print(f"PermissionError: {e}")
            return
    else:
        print(f"Directory already exists: {output_dir}")

    # 각 이미지에 대해 XML 생성
    for image_id, content in data.items():
        annotation = ET.Element("annotation")

        # 폴더 정보 (기본값)
        folder = ET.SubElement(annotation, "folder")
        folder.text = "images"

        # 파일 이름
        filename = ET.SubElement(annotation, "filename")
        filename.text = content["filename"]

        # 이미지 크기 정보
        size = ET.SubElement(annotation, "size")
        width = ET.SubElement(size, "width")
        width.text = str(content["size"]["width"])
        height = ET.SubElement(size, "height")
        height.text = str(content["size"]["height"])
        depth = ET.SubElement(size, "depth")
        depth.text = str(content["size"]["depth"])

        # 객체 정보 추가
        for obj in content["objects"]:
            object_element = ET.SubElement(annotation, "object")
            
            # 클래스 이름
            name = ET.SubElement(object_element, "name")
            name.text = obj["name"]
            
            # 바운딩 박스 좌표
            bndbox = ET.SubElement(object_element, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin")
            xmin.text = str(obj["bndbox"]["xmin"])
            ymin = ET.SubElement(bndbox, "ymin")
            ymin.text = str(obj["bndbox"]["ymin"])
            xmax = ET.SubElement(bndbox, "xmax")
            xmax.text = str(obj["bndbox"]["xmax"])
            ymax = ET.SubElement(bndbox, "ymax")
            ymax.text = str(obj["bndbox"]["ymax"])

        # XML 저장
        xml_string = ET.tostring(annotation, encoding="unicode")
        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
        
        output_file = os.path.join(output_dir, f"{image_id}.xml")
        print(f"Saving XML to: {output_file}")  # 디버깅용 로그
        try:
            with open(output_file, "w") as f:
                f.write(pretty_xml)
        except PermissionError as e:
            print(f"PermissionError: {e}")
        except Exception as e:
            print(f"Error while saving XML: {e}")

    print(f"XML files have been saved to {output_dir}")
