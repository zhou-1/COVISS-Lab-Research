# Python logging configuration      
https://docs.djangoproject.com/en/2.1/topics/logging/    

loggers      
A logger is the entry point into the logging system. Each logger is a named bucket to which messages can be written for processing.     

Handlers   
The handler is the engine that determines what happens to each message in a logger. It describes a particular logging behavior, such as writing a message to the screen, to a file, or to a network socket.     
A logger can have multiple handlers, and each handler can have a different log level.     

Filters    
A filter is used to provide additional control over which log records are passed from logger to handler.     

Formatters   
Ultimately, a log record needs to be rendered as text. Formatters describe the exact format of that text.    

# Place logging calls into code    
import logging library, get an instance of a logger, using the logging framework.     

    # import the logging library
    import logging

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def my_view(request, arg1, arg):
      ...
      if bad_mojo:
        # Log an error message
        logger.error('Something went wrong!')


# Naming loggers    

    # Get an instance of a specific named logger
    logger = logging.getLogger('project.interesting.stuff')
The dotted paths of logger names define a hierarchy. The project.interesting logger is considered to be a parent of the project.interesting.stuff logger; the project logger is a parent of the project.interesting logger.    

# Making logging calls    
The logger instance contains an entry method for each of the default log levels:

    logger.debug()
    logger.info()
    logger.warning()
    logger.error()
    logger.critical()
    
    logger.log(): Manually emits a logging message with a specific log level.
    logger.exception(): Creates an ERROR level logging message wrapping the current exception stack frame.

# Confirguring logging     
Instead, you can set disable_existing_loggers to False and redefine some or all of the default loggers; or you can set LOGGING_CONFIG to None and handle logging config yourself.      

First, here’s a simple configuration which writes all logging from the django logger to a local file.      

Second, here’s an example of how to make the logging system print Django’s logging to the console. It may be useful during local development.     
By default, this config only sends messages of level INFO or higher to the console. 
With this config, however, you can also set the environment variable DJANGO_LOG_LEVEL=DEBUG to see all of Django’s debug logging which is very verbose as it includes all database queries.     

# Custom logging configuration   
If you don’t want to use Python’s dictConfig format to configure your logger, you can specify your own configuration scheme.     
https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-LOGGING_CONFIG    
https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig     

# Disabling logging configuration     
If you don’t want to configure logging at all (or you want to manually configure logging using your own approach), you can set LOGGING_CONFIG to None.      

    LOGGING_CONFIG = None

    import logging.config
    logging.config.dictConfig(...)










