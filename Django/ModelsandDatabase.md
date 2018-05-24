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

	$ python3 manage.py migrate

Whenever you add to existing models, you will have to repeat this process running python manage.py makemigrations <app_name>, and then python manage.py migrate !!!!      

# step 3. Django Models and the Django Shell   
Before we turn our attention to demonstrating the Django admin interface, it’s worth noting that you can interact with Django models from the Django shell - a very useful aid for debugging purposes.   

	print (Category.objects.all())

# step 4. Configuring the Admin Interface
One of the stand-out features of Django is that it provides a built in, web-based administrative interface that allows us to browse and edit data stored within our models and corresponding database tables.   
add 127.0.0.1 in ALLOWSED_HOSTS    
http://127.0.0.1:8000/admin/      
we will need to instruct Django to also include the models from rango   
register the models with the admin interface. If we were to have another model, it would be a trivial case of calling the admin.site.register() function, passing the model in as a parameter   

# step5. Creating a Population Script   


