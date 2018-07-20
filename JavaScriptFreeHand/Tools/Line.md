# Line drawing tool     
draw the line at the time when mouse release.   

Once mouse down ot touch starts, choose color, size, push value in trace array   
WHile mouse or touch moving, "preview" the process of line going, when it is out, let tool being false, call ajax to stop the trace, and update the image.    
Once mouse up or touch ends, let tool being false, end pushing trace array, call ajax to stop the trace.    
