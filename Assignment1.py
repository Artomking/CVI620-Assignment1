import numpy as np
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
    # Exit if key pressed is Escape
    if key == 27:
        break
    # Take a picture of key pressed is spacebar
    # Save to photos folder
    elif key == 32:
        photoNumber = photo_number("Photobooth/photos")
        photoName = os.path.join("photos", f"photo{photoNumber}.png")
        cv2.imwrite(photoName, frame)
        print(f"Photo taken: {photoName}")

# Image Arithmetic (must press escape to access)
img_path_rat = "Image Arithmetic/rat.jpg"
img_path_beaver = "Image Arithmetic/beaver.jpg"

# Show normal rat image
image = cv2.imread(img_path_rat)
image = cv2.resize(image, (1200, 600))
cv2.imshow("Rat", image)

# Show rat brightened by adding 150
brightMatrix = np.full(image.shape, 150)
brightImage = cv2.add(image, np.full(image.shape, 150, dtype=np.uint8))
brightImage = cv2.resize(brightImage, (1200, 600))
cv2.imshow("Bright Rat", brightImage)

# Show rat contrasted by 0.5
contrastImage = cv2.convertScaleAbs(brightImage, alpha=0.5, beta=0)
contrastImage = cv2.resize(contrastImage, (1200, 600))
cv2.imshow("Contrast Rat", contrastImage)

# Show beaver
image2 = cv2.imread(img_path_beaver)
image2 = cv2.resize(image2, (1200, 600))
cv2.imshow("Beaver", image2)


# Create function for blending images through trackbar alpha value
def update(val):
    alpha = val / 100
    imageBlend = cv2.addWeighted(image, 1 - alpha, image2, alpha, 0)
    cv2.imshow("RatBeaver", imageBlend)


cv2.imshow("RatBeaver", image)
# Create trackbar to easily modify alpha
cv2.createTrackbar("Alpha", "RatBeaver", 50, 100, update)

# Drawing application
img_path_rhino = "Drawing Application/rhino.jpg"
image = cv2.imread(img_path_rhino)

# Framework for rectangle
pt1 = (100, 150)
pt2 = (400, 300)
color = (0, 255, 0)
thickness = -1
lineType = cv2.LINE_4

# Draw rectangle on image
image_rect = cv2.rectangle(image, pt1, pt2, color, thickness, lineType)

# Framework for text
text = "Rhino"
org = (200, 225)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (50, 0, 50)

# Draw text on the image
image_text = cv2.putText(image_rect, text, org, fontFace, fontScale, color, lineType)

# show the image with text and green rectangle
cv2.imshow("Rectangle Rhino with Text", image_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
