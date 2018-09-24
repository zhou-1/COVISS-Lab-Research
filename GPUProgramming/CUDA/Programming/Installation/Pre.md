# Guide    
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html    

1.Verify You Have a CUDA-Capable GPU    

    $ lspci | grep -i nvidia     
    01:00.0 VGA compatible controller: NVIDIA Corporation GM107GL [Quadro K620] (rev a2)
    01:00.1 Audio device: NVIDIA Corporation Device 0fbc (rev a1)

2.Verify You Have a Supported Version of Linux     

    $ uname -m && cat /etc/*release
    x86_64
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=16.04

3.Verify the System Has gcc Installed    

    $ gcc --version

4.Verify the System has the Correct Kernel Headers and Development Packages Installed    
 
    $ uname -r     
    4.15.0-34-generic
If not, can use below command to install     

    $ sudo apt-get install linux-headers-$(uname -r)
    In mine, 0 upgraded, 0 newly installed, 0 to remove and 55 not upgraded.

5.Choose an Installation Method     
The CUDA Toolkit can be installed using either of two different installation mechanisms: distribution-specific packages (RPM and Deb packages), or a distribution-independent package (runfile packages).     

6.Download the NVIDIA CUDA Toolkit    
The NVIDIA CUDA Toolkit is available at http://developer.nvidia.com/cuda-downloads.    
Installation Instructions:

    Run `sudo sh cuda_10.0.130_410.48_linux.run`
    Follow the command-line prompts


# Add on   
https://zhuanlan.zhihu.com/p/34587739   


