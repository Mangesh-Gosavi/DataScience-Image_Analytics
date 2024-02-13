from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('C:\\Users\\Pritam\\runs\\detect\\train\\weights\\last.pt')  # load a custom model

print("Prediction:")
# Predict with the model
results = model('E:\\@RUIA\\Data Science\\Internal Project\\Object_detection\\test_data\\IMG0000059.jpg')  # predict on an image
