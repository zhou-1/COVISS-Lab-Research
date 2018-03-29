# Erosion
# as an example, I would use a 5x5 kernel with full of ones.

import cv2 as cv
import numpy as np

img = cv.imread('/home/zhou/opencv/doc/py_tutorials/py_imgproc/py_morphological_ops/images/j.png', 0)
cv.imshow('image', img)
cv.waitKey(0) & 0xFF
kernel = np.ones((5, 5), np.uint8)

erosion = cv.erode(img, kernel, iterations=1)  #erosion is the image after processed
#cv.imshow('image', erosion)
#cv.waitKey(0) & 0xFF

dilation = cv.dilate(img, kernel, iterations=1)
#cv.imshow('image', dilation)
#cv.waitKey(0) & 0xFF

#assumed that the objects are bright on a dark foreground
#Useful for removing small objects
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
#cv.imshow('image', opening)
#cv.waitKey(0) & 0xFF

#Useful to remove small holes (dark regions).
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#cv.imshow('image', closing)
#cv.waitKey(0) & 0xFF

#Morphological Gradient
#useful for finding the outline of an object
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
#cv.imshow('image', gradient)
#cv.waitKey(0) & 0xFF

#Top Hat
kernel = np.ones((9, 9), np.uint8)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
#cv.imshow('image', tophat)
#cv.waitKey(0) & 0xFF

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow('image', blackhat)
cv.waitKey(0) & 0xFF