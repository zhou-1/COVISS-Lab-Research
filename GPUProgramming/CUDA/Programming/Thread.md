# Thread    
一个线程需要两个内置的坐标变量（blockIdx，threadIdx）来唯一标识，它们都是dim3类型变量，
其中blockIdx指明线程所在grid中的位置，而threaIdx指明线程所在block中的位置      

