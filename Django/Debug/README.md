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

    # import the logging library
    import logging

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def my_view(request, arg1, arg):
        ...
        if bad_mojo:
            # Log an error message
            logger.error('Something went wrong!')
