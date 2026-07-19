import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Failed to open the camera.")
    exit()

success, frame = camera.read()

if not success:
    print("Failed to capture an image.")
    camera.release()
    exit()

print("Image captured successfully!")

print("Image Shape:", frame.shape)
print("Image Data Type:", frame.dtype)
print("Top-left Pixel:", frame[0, 0])

camera.release()