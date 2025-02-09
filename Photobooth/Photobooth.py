import cv2
import os


# Photobooth

# Function to determine which number the photo filename should use
# Checks through all existing photos in folder to ensure no numbers are repeated
def photo_number(directory):
    # Check for photos that align with naming scheme
    existing_photos = [i for i in os.listdir(directory) if i.startswith("photo") and i.endswith(".png")]
    numbers = []

    # Add a number for every photo that already has that number
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


# Turn on camera
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
    # Exit if key pressed is escape
    if key == 27:
        break
    # Take a picture of key pressed is spacebar
    # Save to photos folder
    elif key == 32:
        photoNumber = photo_number("photos")
        photoName = os.path.join("photos", f"photo{photoNumber}.png")
        cv2.imwrite(photoName, frame)
        print(f"Photo taken: {photoName}")
