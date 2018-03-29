# Goal   
We will learn different morphological operations like Erosion, Dilation, Opening, Closing etc.     
We will see different functions like : cv.erode(), cv.dilate(), cv.morphologyEx() etc.    

# Morphological transformations Theory        
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. 
It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of 
operation. Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, 
Gradient etc also comes into play.     

# Erosion 侵蚀         
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). So what it does? The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).    

# Dilation 扩张       
It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.     

# Opening      
Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above. Here we use the function, cv.morphologyEx()      

# Closing     
Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.     

# Morphological Gradient 形态梯度    
It is the difference between dilation and erosion of an image.
The result will look like the outline of the object.     

![alt text](https://docs.opencv.org/trunk/gradient.png)        
<p align="center">
  <img />
</p>
