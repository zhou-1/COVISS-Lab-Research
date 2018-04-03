# Goal   
In this tutorial, you will learn Simple thresholding, Adaptive thresholding, Otsu's thresholding etc.    
You will learn these functions : cv.threshold, cv.adaptiveThreshold etc.    
https://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html     

# Simple Thresholding 
First argument is the source image, which should be a grayscale image. Second argument is the threshold value which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.    
![alt text](https://docs.opencv.org/trunk/threshold.png)   


# Adaptive Thresholding    
In the previous section, we used a global value as threshold value. But it may not be good in all the conditions where image has different lighting conditions in different areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.    
Adaptive Method - It decides how thresholding value is calculated.

    cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
    cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
Block Size - It decides the size of neighbourhood area.       
C - It is just a constant which is subtracted from the mean or weighted mean calculated.       

ADAPTIVE_THRESH_MEAN_C     
Python: cv.ADAPTIVE_THRESH_MEAN_C    
the threshold value T(x,y) is a mean of the 𝚋𝚕𝚘𝚌𝚔𝚂𝚒𝚣𝚎×𝚋𝚕𝚘𝚌𝚔𝚂𝚒𝚣𝚎 neighborhood of (x,y) minus C   

ADAPTIVE_THRESH_GAUSSIAN_C   
Python: cv.ADAPTIVE_THRESH_GAUSSIAN_C   
the threshold value T(x,y) is a weighted sum (cross-correlation with a Gaussian window) of the 𝚋𝚕𝚘𝚌𝚔𝚂𝚒𝚣𝚎×𝚋𝚕𝚘𝚌𝚔𝚂𝚒𝚣𝚎 neighborhood of (x,y) minus C . The default sigma (standard deviation) is used for the specified blockSize .   


