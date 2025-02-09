import cv2
import numpy as np

# Image Arithmetic
img_path_rat = "rat.jpg"
img_path_beaver = "beaver.jpg"

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

cv2.waitKey(0)
cv2.destroyAllWindows()
