# Goal   
We will learn different morphological operations like Erosion, Dilation, Opening, Closing etc.     
We will see different functions like : cv.erode(), cv.dilate(), cv.morphologyEx() etc.   
Detailed Explain:    
https://docs.opencv.org/2.4/doc/tutorials/imgproc/opening_closing_hats/opening_closing_hats.html   

# Morphological transformations Theory        
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. 
It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of 
operation. Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, 
Gradient etc also comes into play.     

# Erosion 侵蚀         
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). So what it does? The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).    

![alt text](https://docs.opencv.org/trunk/erosion.png)

# Dilation 扩张       
It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.     

![alt text](https://docs.opencv.org/trunk/dilation.png)

# Opening      
Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above. Here we use the function, cv.morphologyEx()   

![alt text](https://docs.opencv.org/trunk/opening.png)

# Closing     
Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.     

![alt text](https://docs.opencv.org/trunk/closing.png)

# Morphological Gradient 形态梯度    
It is the difference between dilation and erosion of an image.
The result will look like the outline of the object.     

![alt text](https://docs.opencv.org/trunk/gradient.png)       

# Top Hat     
It is the difference between input image and Opening of the image. Below example is done for a 9x9 kernel. 

    kernel = np.ones((9, 9), np.uint8)
    tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    cv.imshow('image', tophat)
    cv.waitKey(0) & 0xFF

![alt text](https://docs.opencv.org/trunk/tophat.png) 

# Black Hat   
It is the difference between the closing of the input image and input image.     

![alt text](https://docs.opencv.org/trunk/blackhat.png) 

