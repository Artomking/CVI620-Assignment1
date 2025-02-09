import cv2

# Drawing application
img_path_rhino = "rhino.jpg"
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
