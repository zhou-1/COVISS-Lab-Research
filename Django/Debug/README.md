# Local debug    
Django Debug Toolbar    
https://github.com/jazzband/django-debug-toolbar    
https://django-debug-toolbar.readthedocs.io/en/latest/installation.html    
Show the debug toolbar    

    def show_toolbar(request):
      return True
    DEBUG_TOOLBAR_CONFIG = {
      "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
    }


# Back-end debug    
https://docs.djangoproject.com/en/2.1/topics/logging/    
https://docs.python.org/2/howto/logging.html     
