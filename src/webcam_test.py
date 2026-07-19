import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Failed to open the camera.")
    exit()

print("Camera opened successfully!")

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to capture a frame.")
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()