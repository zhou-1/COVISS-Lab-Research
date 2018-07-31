# Guide page before main page    
Move contents in index.html to new main.html.    
Change index html being a tutorial page.   
Add a link in play main page to back to guide page.   

NOtes: need to change urls.py. If name of main page now is called play, use   

      path('play/loadlist/', views.loadlist, name='loadlist'),
      
      
