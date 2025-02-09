import cv2
import numpy as np

img_path = "rhino.jpg"
image = cv2.imread(img_path)

pt1 = (100, 150)
pt2 = (400, 300)
color = (0, 255, 0)
thickness = -1
lineType = cv2.LINE_4

image_rect = cv2.rectangle(image, pt1, pt2, color, thickness, lineType)

text = "Rhino"
org = (200, 225)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (50, 0, 50)

image_text = cv2.putText(image_rect, text, org, fontFace, fontScale, color, lineType)

cv2.imshow("Rectangle Rhino with Text", image_text)
cv2.waitKey(0)
cv2.destroyAllWindows()