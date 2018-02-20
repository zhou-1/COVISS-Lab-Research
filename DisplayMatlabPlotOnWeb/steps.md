# Display a MATLAB Plot on the Web using a Java Servlet   
https://www.mathworks.com/help/compiler_sdk/java/web-application-example.html   

# "Compiling Your Java Code" step
Ensure your classpath is set to include:  
javabuilder.jar — included with MATLAB Compiler SDK <b/>     
To use the compiled classes, you need to include a file called javabuilder.jar on the Java class path. You can find this file in one of the following folders: MATLAB installed on your system	matlabroot/toolbox/javabuilder/jar; MATLAB Runtime installed on your system	mcrroot/toolbox/javabuilder/jar  

vararg_java.jar — the JAR file you just built  
  
servlet-api.jar — included as part of the servlet container
