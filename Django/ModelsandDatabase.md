# Models and Database    

# step 1. create models    
In rango/models.py, we will define two classes - both of which must inherit from django.db.models.Model. The two Python classes will be the definitions for models representing categories and pages. Define the Category and Page models     
  
  
      category = models.ForeignKey(    
	      'Category',    
	      on_delete=models.CASCADE,
       )

# step 2. Creating and Migrating the Database   
Setup Database and Create Superuser: python3 manage.py migrate
