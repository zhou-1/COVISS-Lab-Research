# Hints  
https://www.quora.com/JQuery-AJAX-HTML5-JSON-and-JavaScript-How-are-these-different-similar-or-related-What-are-some-good-sources-to-learn-each    

# HTML5   
HTML5 is simply the latest version of HTML. You use it to provide structure to the content of a web page.   

# JavaScript   
JavaScript is a client-side scripting language used to “program” or run interactions on the web. “Client-side” just means it runs on your local computer, not on a server far away.     

# jQuery   
jQuery is a JavaScript framework or library which lets you manipulate the DOM (basically, elements of a web page) in a more straightforward, easy-to-learn manner than straight JavaScript does, especially for beginners and non-programmers. But jQuery is, at heart, JavaScript.     

# Json   
JSON, or JavaScript Object Notation, is a way of transmitting data so that it's readable by humans as well as machines. Each datum is sent with two pieces of information: an attribute and a value. It's an alternative to XML, which has syntax similar to HTML.    

# DJango  
Django is server-side. It means, say a client goes to url you have a function inside views that renders 
what he sees and returns a response in html.     

https://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications     
https://stackoverflow.com/questions/11762629/pass-information-from-javascript-to-django-app-and-back    

# Ajax   
AJAX calls are client-side code that does asynchronous requests. That sounds complicated, but it simply means it does a request for you in the background and then handles the response. So when you do an AJAX call for some url, you get the same data you would get as a user going to that place.    
no need to refresh page to get update. Instead of reloading the full page, only part of the page or the data in the page is reloaded.        
Create a view that checks the data, return a response as JSON.   

# Ajax in Django with JQuery   
http://www.tangowithdjango.com/book17/chapters/ajax.html    

# Send an array to Django via ajax   
https://stackoverflow.com/questions/40977166/sending-an-array-to-django-via-ajax   
In views.py   

    def main(request):
        arr = request.POST.getlist('arr[]')
        print(type(arr))
        print(arr)
        return render(request, 'rango/index.html')

In JS   

    <a href=#>Click</a>

    <script>
    $(document).on('click', 'a', function() {

     var arr = [1, 2, 3, 4, 5, 6];
  
     $.ajax({
      url: 'test/',
      type: 'POST',
      data: {'arr': arr},

      });

    });
    </script>

In urls.py   

    urlpatterns = [
        #path('', views.index, name='index'),


        path('', views.main, name='results'),
        path('test/', views.main, name='test'),
        #path('', views._grab_image, name='grabImage'),
    ]

I












