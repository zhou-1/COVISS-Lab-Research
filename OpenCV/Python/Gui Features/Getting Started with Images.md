# how to read an image, how to display it and how to save it back  
functions: cv.imread(), cv.imshow() , cv.imwrite()  
https://docs.opencv.org/trunk/dc/d2e/tutorial_py_image_display.html  

# read an image  
Use the function cv.imread() to read an image.    
a flag which specifies the way image should be read.  

    cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
    cv.IMREAD_UNCHANGED : Loads image as such including alpha channel

Note:  
Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.  
<b> 1 for color, 0 for grayscale, -1 for unchanged  </b> 
    
# display an image  
Use the function cv.imshow() to display an image in a window. The window automatically fits to the image size.   

    cv.imshow('image',img)
First argument is a window name which is a string. second argument is our image. You can create as many windows as you wish, but with different window names.   

    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
cv.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke.   
cv.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window, use the function cv.destroyWindow() where you pass the exact window name as the argument.      

    cv.namedWindow('image', cv.WINDOW_NORMAL)
There is a special case where you can already create a window and load image to it later. In that case, you can specify whether window is resizable or not. It is done with the function cv.namedWindow(). By default, the flag is cv.WINDOW_AUTOSIZE. But if you specify flag to be cv.WINDOW_NORMAL, you can resize window. It will be helpful when image is too large in dimension and adding track bar to windows.    




 
