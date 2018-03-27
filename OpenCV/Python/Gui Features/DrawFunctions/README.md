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

# Line
To draw a line, you need to pass starting and ending coordinates of line.  

# Rectangle
To draw a rectangle, you need top-left corner and bottom-right corner of rectangle.   

# Circle
To draw a circle, you need its center coordinates and radius.   

# Ellipse
To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). Next argument is axes lengths (major axis length, minor axis length). angle is the angle of rotation of ellipse in anti-clockwise direction. startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse.   
https://docs.opencv.org/trunk/d6/d6e/group__imgproc__draw.html#ga28b2267d35786f5f890ca167236cbc69  

# Polygon  
To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32.  
Here we draw a small polygon of with four vertices in yellow color.  

    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.polylines(img,[pts],True,(0,255,255))

# Adding Text to Images:   
To put texts in images, you need specify following things.   

Text data that you want to write   
Position coordinates of where you want put it (i.e. bottom-left corner where data starts).      
Font type (Check cv.putText() docs for supported fonts)   
Font Scale (specifies the size of font)   
regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended.    

