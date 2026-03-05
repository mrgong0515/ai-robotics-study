from ultralytics import YOLO

model = YOLO("yolov8s.pt")

def detect_img(img_path):
    detect = model(img_path)
    class_name = detect[0].summary()[0]["name"]
    class_conf = detect[0].summary()[0]["confidence"]
    return class_name, class_conf


