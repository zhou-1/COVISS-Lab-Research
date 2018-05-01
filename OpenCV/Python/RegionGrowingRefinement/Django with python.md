# Django API with Python    

***  
Creating a face detection API with Python and OpenCV (in just 5 minutes)   
***   
 
# Step 1: Setup your environment    
$ pip install numpy django requests   

# Step 2: Create our Django project   
$ django-admin startproject cv_api    
$ cd cv_api     
A Django project consists of multiple apps. And one of the core paradigms of the Django framework is that each app should be reusable in any project (theoretically, anyway) — therefore, we do not (normally) place any app-specific code inside the cv_api  directory. Instead, we explicitly create separate “apps” inside the cv_api  project.    
$ python manage.py startapp face_detector     
When you install django using just pip install django, then you have to run python manage.py startapp else if you used pip3Click here to view terminal example install django, then you have to run python3 manage.py startapp    

