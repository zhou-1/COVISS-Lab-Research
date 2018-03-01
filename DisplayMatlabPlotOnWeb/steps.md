# Display a MATLAB Plot on the Web using a Java Servlet   
https://www.mathworks.com/help/compiler_sdk/java/web-application-example.html   

# Install Apache for ubuntu
web server   
https://help.ubuntu.com/lts/serverguide/httpd.html
  

# "Compiling Your Java Code" step
<b> installed JAVA SDK using: <b/>
sudo apt-get install default-jdk

- In terminal call "hostname -I" to get hostname of this machine and check if apache is running
134.48.90.48  
* some basic apache instructions https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-16-04   

# To run .war applications  
we do not need the Apache Tomcat, which I downloaded from here http://tomcat.apache.org/download-80.cgi#8.5.28   

- Instructions for configuring tomcat https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-8-on-ubuntu-16-04   

# to set JAVA_HOME path in Ubuntu 
1) open /etc/environment in any text editor like nano or gedit and add the following line:
JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64"  

2) use source to load the variables, by running this command:

source /etc/environment  

3) check the variable, by running this command:

echo $JAVA_HOME  

- Check that TOMCAT is running fine: http://134.48.90.48:8080/  

- added a user for you in tomcat-user.xml:   <user username="zhou" password="12345" roles="manager-gui,admin-gui"/>  

- configure .war in tomcat server:  
1) http://localhost:8080/ and click in Manager App, type your user: zhou / 12345  

https://stackoverflow.com/questions/15113628/java-lang-classnotfoundexception-javax-servlet-jsp-jstl-core-config  

## Setting CLASSPATH => same as JAVAHOME  
1) open /etc/environment and add a line as for example CLASSPATH="/opt/tomcat/lib/servlet-api.jar"  
2) run in terminal: source /etc/environment  
