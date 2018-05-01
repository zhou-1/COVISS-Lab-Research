# Tutorial   
Credit to: https://www.learnopencv.com/turn-your-opencv-code-into-a-web-api-in-under-10-minutes-part-1/   


1. Register for PythonAnywhere.com    
2. Once you have registered and are logged in, go to the Web tab, and Add a new web app.   
3. Select web2py as your python framework.   
4. Select an admin password for web2py. Note that this is a web2py admin password, and it is different from your PythonAnywhere.com password   
This completes the  registration on PythonAnywhere and web2py installation. Next we will create a new web app on web2py    


# Create a new web app on web2py   
1. Open a new tab, and go to web2py admin interface located at
https://username.pythonanywhere.com/admin/default/index
( Change username to your username ) and use your web2py password to sign in.
Add a new application by providing an appname. [ See the screenshot below ]. Remember this appname. We will refer to it several times in this article.     
2.  Check installation :  If everything went right, you should see your application folder under the Files tab on PythonAnywhere when you go down the directory structure  home/username/web2py/appname       


*****
In a simple web application, the database serves as the model, the code that manipulates the database ( say based on user action ) is the controller, and the html page that faces the user is the view. In web2py the models, views, and controllers are neatly arranged in separate directories.      
*****

# Add OpenCV code to web2py application   

