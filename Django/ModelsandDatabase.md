# Models and Database    
link； http://www.tangowithdjango.com/book17/chapters/models.html   

# step 1. create models    
In rango/models.py, we will define two classes - both of which must inherit from django.db.models.Model. The two Python classes will be the definitions for models representing categories and pages. Define the Category and Page models.
For "Getting TypeError: __init__() missing 1 required positional argument: 'on_delete' when trying to add parent table after child table with entries" error:  
  
      category = models.ForeignKey(    
	      'Category',    
	      on_delete=models.CASCADE,
       )

# step 2. Creating and Migrating the Database   
Setup Database and Create Superuser: python3 manage.py migrate
Now you will want to create a superuser to manage the database： python manage.py createsuperuser   
zhou, zhou.shen@marquette.edu   
password: mu123456   
Creating / Updating Models / Tables: Whenever you make changes to the models, then you need to register the changes, via the makemigrations command for the particular app.     
to apply these migrations (which will essentially create the database tables), then you need to issue:

	$ python manage.py migrate

