# step 1. get data from user side (x,y coordinates)   
1. download in user's local folder. we cannot retrive data in server side, pass   
2. send form data, but not for variables we have for x and y directly, pass    
3. web storage/DOM storage, is not automatically transmitted to the server in every HTTP request, and a web server can't directly write to Web storage, pass    
4. cookies. session cookies are enough to use. but hard to analysis and use. pass     
5. send back variables in javaScript while updating values in HTML. did not find a way doing this, pass        
6. collect all data together in user's web storage and then send back to server with click button. local storage only read and that's not possible since sessionStorage lives on the client, server cannot retrieve data.    
7. Pass Data To Our Template In Django   
How to access data from the models within the views and how to present this data via the templates      
http://www.tangowithdjango.com/book17/chapters/models_templates.html      
Five main steps to create a data driven webpage in Django:    
  *. import models wish to use in application's views.py file    
  *. with the view you wish to use, query the model to get the data want to present    
  *. pass the result form model into template's context    
  *. setup template to present the data to the user in whatever way    
  *. map a url to view    
Field error Cannot resolve keyword 'likes' into field. Choices are: id, name, page   
https://stackoverflow.com/questions/33449009/field-error-cannot-resolve-keyword-likes-into-field-choices-are-id-name-pa    
main problem: OperationalError, no such column. Django    
In current version,  normal syncdb is now a two step process, python manage.py makemigrations followed by python manage.py migrate.     
https://stackoverflow.com/questions/26312219/operationalerror-no-such-column-django/27286896   

8. Handling ajax request in Django    
client = Ajax = Django view   
 . initialize Django project   
 . create models   
 . create views   
 . create URLs   
 . making templates and carrying out ajax request   
 . register models to admin and add some posts   
<b> see hints.md  </b>     

send form data: https://www.w3schools.com/jsref/met_form_submit.asp      
HTML web storage (session storage object): https://www.w3schools.com/Html/html5_webstorage.asp    



# step 2. collect all data user have dynamically     
For rectangle: where click the mouse, where then release the mouse  
For line: same to rectangle   
needs two coordinates: click and release   
when mouse down which means click the mouse, get coordinates once; when up, get click coordinates again.      

For pencil: need almost every points (in a short time/period)      
needs danamic coordinates   
<b> especially for pencil method </b>    
get mouse position: https://stackoverflow.com/questions/1439022/get-mouse-position   
track mouse position: https://stackoverflow.com/questions/7790725/javascript-track-mouse-position    
More: https://www.w3schools.com/jsref/event_clientx.asp    
https://www.w3schools.com/js/js_events_examples.asp       

Therefore, only remaining solution is getting the current mouse position while moving.     
what we also need to care for: after click mose, moving the mouse is valid; otherwise, invalid.   
modifying in the pencil tool makes whole things much easier.    
example useful fo rmoving mouse: https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_event_mouse_clientxy2       
  
# Step 3. store post data in server as a file, then our python app can use it    
After user finish all drawing, click submit button to submit all data to server. All data should be used together.    














