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


# Otsu’s Binarization     
otsu又叫最大类间方差。主要是找到一个阈值，使整个图像中前景与背景这两部分差别最大，（这方法主要用于分割其实）     
In global thresholding, we used an arbitrary value for threshold value, right? So, how can we know a value we selected is good or not? Answer is, trial and error method. But consider a bimodal image (In simple words, bimodal image is an image whose histogram has two peaks). For that image, we can approximately take a value in the middle of those peaks as threshold value, right ? That is what Otsu binarization does. So in simple words, it automatically calculates a threshold value from image histogram for a bimodal image. (For images which are not bimodal, binarization won’t be accurate.)     
For this, our cv.threshold() function is used, but pass an extra flag, cv.THRESH_OTSU. For threshold value, simply pass zero. Then the algorithm finds the optimal threshold value and returns you as the second output, retVal. If Otsu thresholding is not used, retVal is same as the threshold value you used.    


