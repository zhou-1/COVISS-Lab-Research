import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# in the middle
cv.line(img, (0, 255), (511, 255), (255, 0, 0), 5)

# Draw a green rectangle at the top-right corner of image.
cv.rectangle(img, (180, 0), (330, 150), (0, 255, 0), 3)

# Draw a red circle inside the rectangle drawn above
cv.circle(img, (255, 70), 63, (0, 0, 255), -1)

# Draw a blue half ellipse at the center of the image
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

#
# did not understand
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

# Write OpenCV on our image in white color
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('Image', img)
cv.waitKey(0)