# Display a MATLAB Plot on the Web using a Java Servlet   
https://www.mathworks.com/help/compiler_sdk/java/web-application-example.html   

# Install Apache for ubuntu
https://help.ubuntu.com/lts/serverguide/httpd.html
web server   

# "Compiling Your Java Code" step
Ensure your classpath is set to include:  
<b> javabuilder.jar — included with MATLAB Compiler SDK </b>     
To use the compiled classes, you need to include a file called javabuilder.jar on the Java class path. You can find this file in one of the following folders: MATLAB installed on your system	matlabroot/toolbox/javabuilder/jar; MATLAB Runtime installed on your system	mcrroot/toolbox/javabuilder/jar  
Location:
/usr/share  
/var/www

<b> vararg_java.jar — the JAR file you just built </b>    
the JAR file you just built in "built java package" step, Project Nameis vararg_java.  
Location:  
/home/medeiros/varargexample/for_redistribution_files_only  
/home/medeiros/varargexample/for_testing  

<b> servlet-api.jar — included as part of the servlet container </b>  
included as part of the servlet container    
location:  
/usr/local/MATLAB/R2016a/java/jarext/j2ee  
/usr/local/MATLAB/R2016a/sys/tomcat/lib  
/usr/local/MATLAB/R2017a/java/jarext/j2ee  
/usr/local/MATLAB/R2017a/sys/tomcat/lib  
