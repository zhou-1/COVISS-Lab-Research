# how to read an image, how to display it and how to save it back  
functions: cv.imread(), cv.imshow() , cv.imwrite()  

# read an image  
Use the function cv.imread() to read an image.    
a flag which specifies the way image should be read.  

    cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
    cv.IMREAD_UNCHANGED : Loads image as such including alpha channel

