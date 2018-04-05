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

# Structuring Element    
# Rectangular Kernel
>>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))     


        array([[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]], dtype=uint8)

https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
 
