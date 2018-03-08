# Different ways

The HTML <canvas> element is used to draw graphics, on the fly, via scripting (usually JavaScript).   
The <canvas> element is only a container for graphics. You must use a script to actually draw the graphics.   
Canvas has several methods for drawing paths, boxes, circles, text, and adding images.  

1. JavaScript
upload the canvas Image by using Canvas DataURL  
Saving HTML 5 Canvas as Image on the server using ASP.NET   
https://stackoverflow.com/questions/10792986/saving-html-5-canvas-as-image-on-the-server-using-asp-net  

Send canvas image to server and return processed image from server to client to display   
If you want to send the image back from the server to the client, you should use SignalR (or another framework/library 
which implements websockets). The other way is to request the image from the server, but you have to be sure that the webserver 
has finished processing the image.  
https://stackoverflow.com/questions/39320495/send-canvas-image-to-server-and-return-processed-image-from-server-to-client-to  

2.
