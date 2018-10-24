# Python logging configuration    
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


