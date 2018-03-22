# Goal    
Learn to draw different geometric shapes with OpenCV   
You will learn these functions : cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText() etc.   
https://docs.opencv.org/trunk/dc/da5/tutorial_py_drawing_functions.html  


# Code
In all the above functions, you will see some common arguments as given below:  

1. Img : The image where you want to draw the shapes  
2. Color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.  
3. Thickness : Thickness of the line or circle etc. If **-1** is passed for closed figures like circles, it will fill the shape. default thickness = 1  
4. LineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.  
