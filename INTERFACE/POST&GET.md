HTTP POST requests supply additional data from the client (browser) to the server in the message body.        

In contrast, GET requests include all required data in the URL. Forms in HTML can use either method by specifying method="POST" or method="GET" (default) in the <form> element.       


The method specified determines how form data is submitted to the server.     
When the method is GET, all form data is encoded into the URL, appended to the action URL as query string parameters.     
With POST, form data appears within the message body of the HTTP request.     
