# Hints  

# DJango  
Django is server-side. It means, say a client goes to url you have a function inside views that renders 
what he sees and returns a response in html.     

https://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications     
https://stackoverflow.com/questions/11762629/pass-information-from-javascript-to-django-app-and-back    

# Ajax   
AJAX calls are client-side code that does asynchronous requests. That sounds complicated, but it simply means it does a request for you in the background and then handles the response. So when you do an AJAX call for some url, you get the same data you would get as a user going to that place.    
no need to refresh page to get update. Instead of reloading the full page, only part of the page or the data in the page is reloaded.        
Create a view that checks the data, return a response as JSON.   
