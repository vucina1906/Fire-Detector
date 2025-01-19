from ultralytics import YOLO

model = YOLO("yolov8l.pt")  

# Train the model
results = model.train(data="config.yaml", epochs=100)  # Train with the specified config.yaml
