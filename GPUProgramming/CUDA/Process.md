# Typical CUDA work process   
分配host内存，并进行数据初始化；    
分配device内存，并从host将数据拷贝到device上；    
调用CUDA的核函数在device上完成指定的运算；   
将device上的运算结果拷贝到host上；   
释放device和host上分配的内存。    

# Kernel  
在device上线程中并行执行的函数   
kernel在device上执行时实际上是启动很多线程，一个kernel所启动的所有线程称为一个网格（grid），
同一个网格上的线程共享相同的全局内存空间，grid是线程结构的第一层次，而网格又可以分为很多线程块（block），
一个线程块里面包含很多线程，这是第二个层次。     

