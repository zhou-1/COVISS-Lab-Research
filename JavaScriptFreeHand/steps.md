# step 1. get coordinate of image   
MouseEvent clientX Property    
https://www.w3schools.com/jsref/event_clientx.asp    

# Step 2. draw image on canvas    
HTML canvas drawImage() Method   
https://www.w3schools.com/tags/canvas_drawimage.asp   

# step 3. draw small circle based on coordinates     
HTML canvas arc() Method   
https://www.w3schools.com/tags/canvas_arc.asp   

# step 4. Creating an HTML5 Canvas Painting Application   
free hand drawing   
https://dev.opera.com/articles/html5-canvas-painting/    
step a. Testing the Canvas interaction   
Move the mouse over the rectangle below.   
step b. Implementing events   
Hold down the mouse button to draw in the rectangle below.    
step c. Adding drawing tools   
rectangle and pencil(step b)   
step d. Add Line   

# step 5. uploading image inside the "working" box    
draw image in box first, then update draw functions on it, lastly, add coordinates detection function inside.

# step 6. retrieve or download coordinates of x and y   
only can download in download foleder, cnanot change to desired location: Whether the browser asks the user or not is down to the preferences in the browser. You can't bypass those preference, otherwise it would violate user's security. may be not a good way   

Download coordinate values through javaScript   

    download('coordsFile.txt', coords)      
    function download(filename, coords) {
      var pom = document.createElement('a');
      pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + 

    encodeURIComponent(coords));
      pom.setAttribute('download', filename);

      pom.style.display = 'none';
      document.body.appendChild(pom);

      pom.click();

      document.body.removeChild(pom);
     }

Next step: try to add variables inside the file instead of multiple files.   

# However    
# step 7: get data from user side in server side     
see data folder   




resize image: https://askubuntu.com/questions/1164/how-to-easily-resize-images-via-command-line    
useful: https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse     
