# OpenCV - Python Tutorials  

https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html 

1. Install Python 3 and Set Up a Local Programming Environment on Ubuntu 16.04  
a. Step 1 — Setting Up Python 3  
b. Step 2 — Setting Up a Virtual Environment  
c. Step 3 — Creating a Simple Program  
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04  
Congratulations! At this point you have a Python 3 programming environment set up on your local Ubuntu machine and can begin a coding project!  


2. Install IDLE Python IDE on Ubuntu Desktop 16.04  
Install idle for Python 3  
http://www.configserverfirewall.com/ubuntu-linux/install-python-idle-ubuntu-16/  
For Python shell
error: SyntaxError: multiple statements found while compiling a single statement [duplicate]  
reason: In the shell, you can't execute more than one statement at a time  
https://stackoverflow.com/questions/21226808/syntaxerror-multiple-statements-found-while-compiling-a-single-statement    


3. Install Pycharm IDLE on Linux  
https://www.jetbrains.com/help/pycharm/requirements-installation-and-launching.html#linux   
Starting PyCharm on Linux  
/opt/pycharm-community-2017.3.4/bin  
Run pycharm.sh from the bin subdirectory by using code ./pycharm.sh.  
How to set the default library path for python  
https://stackoverflow.com/questions/42548750/how-to-set-the-default-library-path-for-python   
import OpenCV in pycharm  
need to click "inherit global site-packages" while creating project  
How to Install OpenCV – OpenCV 3.2 on Ubuntu 17.04 with PyCharm  
https://shahsparx.me/install-opencv-ubuntu-python-pycharm/  


4. Install OpenCV-Python in Ubuntu  
Building OpenCV from source   
sudo apt-get install cmake  
sudo apt-get install python-dev python-numpy
sudo apt-get install gcc g++
sudo apt-get install libgtk2.0-dev  
sudo apt-get install libgtk2-dev  
How to install FFmpeg on Ubuntu 14.04  
FFmpeg has been removed from Ubuntu 14.04 and was replaced by Libav. This decision has been reversed so that FFmpeg is available now in Ubuntu 15.04 again, but there is still no official package for 14.04. In this tutorial, I will show you how to install FFmpeg from mc3man ppa.   
https://www.faqforge.com/linux/how-to-install-ffmpeg-on-ubuntu-14-04/  
sudo apt install  gstreamer0.10-plugins-good  
https://docs.opencv.org/trunk/d2/de6/tutorial_py_setup_in_ubuntu.html  
Downloading OpenCV (Now open a terminal window and navigate to the downloaded "opencv" folder. )  
Configuring and Installing   
Python 2:  
--     Interpreter:                 /usr/bin/python2.7 (ver 2.7.12)  
--     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.12)  
--     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)  
--     packages path:               lib/python2.7/dist-packages  
--   
--   Python 3:  
--     Interpreter:                 /usr/bin/python3 (ver 3.5.2)  
--     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython3.5m.so (ver 3.5.2)  
--     numpy:                       /home/zhou/.local/lib/python3.5/site-packages/numpy/core/include (ver 1.14.2)  
--     packages path:               lib/python3.5/dist-packages  
--   
--   Python (for build):            /usr/bin/python2.7  
Now you build the files using "make" command and install it using "make install" command.  
$ make  
#sudo make install  
Installation is over. All files are installed in "/usr/local/" folder. Open a terminal and try import "cv2".  

        import cv2 as cv  
        print(cv.__version__)  


