# Goal   
Learn to handle mouse events in OpenCV     
You will learn these functions : cv.setMouseCallback()     

# Simple Demo   
Here, we create a simple application which draws a circle on an image wherever we double-click on it.    

    while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
        
0xFF is a hexadecimal constant which is 11111111 in binary. By using bitwise AND (&) with this constant, it leaves only the last 8 bits of the original (in this case, whatever cv2.waitKey(0) is).

# More Advanced Demo   
This one is helpful, kind of free hand drawing.   
Now we go for a much better application. In this, we draw either rectangles or circles (depending on the mode we select) by dragging the mouse like we do in Paint application. So our mouse callback function has two parts, one to draw rectangle and other to draw the circles. This specific example will be really helpful in creating and understanding some interactive applications like object tracking, image segmentation etc.    
Next we have to bind this mouse callback function to OpenCV window. In the main loop, we should set a keyboard binding for key 'm' to toggle between rectangle and circle.     
