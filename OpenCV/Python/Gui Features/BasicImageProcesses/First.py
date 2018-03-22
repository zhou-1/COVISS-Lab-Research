import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import numpy as np
import cv2 as cv

# read an image
# Load an color image in grayscale
img = cv.imread('/home/zhou/opencv/samples/data/messi5.jpg', 0)  #where the image is

# display the image
# cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)

# give user options to save image or not when leave
# If you are using a 64-bit machine, you will use k = cv.waitKey(0) & 0xFF
# otherwise, use k = cv.waitKey(0)
# Delay in milliseconds. 0 is the special value that means “forever”
k = cv.waitKey(0) & 0xFF
print(k)    # get the value of k then we can know what user type

if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('messigray.png', img)
    cv.destroyAllWindows()
else:
    print('Unrecommended button to close the window')

