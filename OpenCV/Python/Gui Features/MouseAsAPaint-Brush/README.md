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
