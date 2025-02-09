import cv2
import os
import time


def photo_number(directory):
    existing_photos = [i for i in os.listdir(directory) if i.startswith("photo") and i.endswith(".png")]
    numbers = []

    for photo in existing_photos:
        try:
            num = int(photo[5:].split(".")[0])
            numbers.append(num)
        except ValueError:
            continue
    nextNum = 1
    while nextNum in numbers:
        nextNum += 1
    return nextNum


camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = camera.read()
    if not ret:
        print("Frames are unable to be read. Exiting program")
        break
    cv2.imshow("Photobooth", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('c'):
        photoNumber = photo_number("photos")
        photoName = os.path.join("photos", f"photo{photoNumber}.png")
        cv2.imwrite(photoName, frame)
        print(f"Photo taken: {photoName}")
