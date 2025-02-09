import cv2
import numpy as np

img_path_rat = "rat.jpg"
img_path_beaver = "beaver.jpg"

image = cv2.imread(img_path_rat)
image = cv2.resize(image, (1200, 600))
cv2.imshow("Rat", image)

brightMatrix = np.full(image.shape, 150)
brightImage = cv2.add(image, np.full(image.shape, 150, dtype=np.uint8))
brightImage = cv2.resize(brightImage, (1200, 600))
cv2.imshow("Bright Rat", brightImage)

contrastImage = cv2.convertScaleAbs(brightImage, alpha=0.5, beta=0)
contrastImage = cv2.resize(contrastImage, (1200, 600))
cv2.imshow("Contrast Rat", contrastImage)

image2 = cv2.imread(img_path_beaver)
image2 = cv2.resize(image2, (1200, 600))
cv2.imshow("Beaver", image2)

alpha = float(input("Enter alpha between 0 and 1: "))

imageBlend = cv2.addWeighted(image, 1-alpha, image2, alpha, 0)
cv2.imshow("RatBeaver", imageBlend)

cv2.waitKey(0)
cv2.destroyAllWindows()
