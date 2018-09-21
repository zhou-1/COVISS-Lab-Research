# What is CUDA?  
CUDA: 
1. cuda MASSIVELY PARALLEL ARCHITECTURE of modern GPUs with hundreds of cores     
2. CUDA parallel programming model used to program these GPUs

CPUs have several cores, GPUs have hundreds of cores. 

# Benefits of CUDA   
efficiently process thousands of elements for a particular task in parallel second - communicate and collarborate efficiently   
process thousands of threads simultaneously.   
CUDA provides intuitive way to express parallelism

# How does CUDA work?   
CUDA ecosystem: partners, tools, libraries, languages & APIs, training     
each thread operates on exactly one element, int i = threadIdx...; vecAdd<<n>>(A,B,C)   
execute n times as in separate thread, one thread per data element   

https://www.youtube.com/watch?v=IzU4AVcMFys    
