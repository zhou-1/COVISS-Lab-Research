# Goal    
Learn to bind trackbar to OpenCV windows   
You will learn these functions : cv.getTrackbarPos(), cv.createTrackbar() etc.     

# Code Demo      
Here we will create a simple application which shows the color you specify. 
You have a window which shows the color and three trackbars to specify each of B,G,R colors. 
You slide the trackbar and correspondingly window color changes. By default, initial color will be set to Black.     

For cv.getTrackbarPos() function, first argument is the trackbar name, second one is the window name to which it is attached, 
third argument is the default value, fourth one is the maximum value and fifth one is the callback function 
which is executed everytime trackbar value changes. The callback function always has a default argument which is the trackbar 
position. In our case, function does nothing, so we simply pass.    

Another important application of trackbar is to use it as a button or switch. 
OpenCV, by default, doesn't have button functionality. So you can use trackbar to get such functionality. 
In our application, we have created one switch in which application works only if switch is ON, otherwise screen is always black.     
