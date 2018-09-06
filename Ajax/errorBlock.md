# error block      
for each AJAX call, we have a "error" block that throws an alert when it fails after retrying    
automatically refresh the page in case that happens    

add window.location.reload(); in error function, will refresh automatically every time it fails.    
Only changed in first load, onWindowLoad.    
https://stackoverflow.com/questions/7881089/reload-the-page-after-ajax-success   
