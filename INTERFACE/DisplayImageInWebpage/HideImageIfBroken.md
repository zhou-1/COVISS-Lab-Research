If there is no image to show, hide it.   

        <!-- hide R if there is no result yet -->
        <img id="R" style ="position: absolute; top: 0; left: 0;" onerror="this.style.display='none'"> 

In refine button, call it back to normal  

        document.getElementById("R").style.display = "inline"; 

https://stackoverflow.com/questions/22051573/how-to-hide-image-broken-icon-using-only-css-html-without-js    
https://www.w3schools.com/jsref/prop_style_display.asp   
