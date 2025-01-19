import cv2
from ultralytics import YOLO

# Load the trained model
model = YOLO(r"E:\Programiranje\Projects\Fire Detection\runs\detect\train\weights\best.pt")

# --------- Option 1: For Video ---------
video_path = r"E:\Programiranje\Projects\Fire Detection\Fire3.mp4"  # Replace with your video file path

# --------- Option 2: For Image ---------
image_path = r"E:\Programiranje\Projects\Fire Detection\fire3.jpg"  # Replace with your image file path

# Check if you want to use video or image:
use_video = True  # Set to True if using video, False if using image

if use_video:
    # --------- Video Processing ---------
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    max_width = 800
    max_height = 600

    while True:
        ret, frame = cap.read()
        if not ret:
            break  

        height, width, _ = frame.shape

        if width > max_width or height > max_height:
            resize_factor = min(max_width / width, max_height / height)
            new_width = int(width * resize_factor)
            new_height = int(height * resize_factor)

            frame_resized = cv2.resize(frame, (new_width, new_height))
        else:
            frame_resized = frame

        results = model(frame_resized)

        result = results[0] 
        annotated_frame = result.plot() 

        cv2.imshow("Fire Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    # --------- Image Processing ---------
    frame = cv2.imread(image_path)

    if frame is None:
        print("Error: Could not load image.")
        exit()

    max_width = 800 
    height, width, _ = frame.shape
    resize_factor = max_width / width
    new_width = max_width
    new_height = int(height * resize_factor)

    frame_resized = cv2.resize(frame, (new_width, new_height))

    results = model(frame_resized)

    result = results[0] 

    annotated_frame = result.plot()  

    annotated_frame_resized = cv2.resize(annotated_frame, (new_width, new_height))

    cv2.imshow("Fire Detection", annotated_frame_resized)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
