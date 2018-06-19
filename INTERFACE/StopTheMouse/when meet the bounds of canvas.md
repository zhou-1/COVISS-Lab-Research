# Keep mouse movement inside the canvas   
After click the mouse, movement bahavior should be in the canvas.     

ref； Keep mouse inside a div， https://stackoverflow.com/questions/5730433/keep-mouse-inside-a-div   

# Stop the trace when mouse is out of canvas   

ref； https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onmouseenter_addeventlistener      
https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onmouseover_addeventlistener   

# implement "onmouseup" in side onmousemove when mouse move out of canvas    

        document.getElementById("imageTemp").onmouseout = function(){mouseOut()}; 

        function mouseOut() {       
          tool.started = false;

          $.ajax({
            //POST stuff

          });
        
          }

https://www.w3schools.com/jsref/event_onmouseout.asp    

