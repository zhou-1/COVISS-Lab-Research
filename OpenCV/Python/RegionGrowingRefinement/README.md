# RGR (Region Growing Refinement)   

# Read matlab file in python   
File IO (scipy.io)    
https://docs.scipy.org/doc/scipy/reference/tutorial/io.html    

        >>> mat_contents = sio.loadmat('octave_a.mat')
        >>> mat_contents
        {'a': array([[[  1.,   4.,   7.,  10.],
                [  2.,   5.,   8.,  11.],
                [  3.,   6.,   9.,  12.]]]),
                '__version__': '1.0',
                '__header__': 'MATLAB 5.0 MAT-file, written by
                Octave 3.6.3, 2013-02-17 21:02:11 UTC',
                '__globals__': []}
        >>> oct_a = mat_contents['a']
        >>> oct_a
        array([[[  1.,   4.,   7.,  10.],
                [  2.,   5.,   8.,  11.],
                [  3.,   6.,   9.,  12.]]])
        >>> oct_a.shape
                (1, 3, 4)



# Matlab convert into Python   
matlab code to numpy    
http://mathesaurus.sourceforge.net/matlab-numpy.html   

# numpy zeros
https://docs.scipy.org/doc/numpy-1.10.4/reference/generated/numpy.zeros.html  

3-dimensional array in numpy    
https://stackoverflow.com/questions/22981845/3-dimensional-array-in-numpy   

# original CNN prediction    


# Structuring Element - Rectangular Kernel        
>>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))     

        array([[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]], dtype=uint8)

https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html    

# count Number of nonzero matrix elements    
nnz in matlab: n = nnz(X) returns the number of nonzero elements in matrix X.   
cv.countNonZero in opencv in python   

# bwmorph   
Morphological operations on binary images   
Matlab: BW2 = bwmorph(BW,operation) applies a specific morphological operation to the binary image BW.      

# Display image as grayscale using matplotlib   
https://stackoverflow.com/questions/3823752/display-image-as-grayscale-using-matplotlib   
https://stackoverflow.com/questions/22777660/display-an-rgb-matrix-image-in-python/22778084#22778084   

# Bitwise operations   
bitxor in MatLab: bit-wise xor   
cv.bitwise_xor in opencv python    
https://docs.opencv.org/3.2.0/d0/d86/tutorial_py_image_arithmetics.html      

# Skeletonization using OpenCV-Python    
http://opencvpython.blogspot.com/2012/05/skeletonization-using-opencv-python.html   

# Find indices of elements    
find in matlab = np.where in python   
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.where.html   

# Total number of elements     
length(x) returns max(size(x)) and numel(x) returns the total number of elements of x    
size(a) or a.size 	//get the number of elements of an array    

# Round up
ceil(a)	in matlab equals numpy.ceil(a) in python   
http://mathesaurus.sourceforge.net/matlab-numpy.html   













 
