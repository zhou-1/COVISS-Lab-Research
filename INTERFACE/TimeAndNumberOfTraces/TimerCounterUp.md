# Show count up timer    
Show the timer, start it when we load image, start a page; pause it when we click pause; re-run it when we click pause again.   
Basic one: https://www.quora.com/How-can-I-make-a-basic-HTML-count-up-timer    

# setInterval()   
The setInterval() method calls a function or evaluates an expression at specified intervals (in milliseconds).    
The setInterval() method will continue calling the function until clearInterval() is called, or the window is closed.       
The ID value returned by setInterval() is used as the parameter for the clearInterval() method.       
Refer from: https://www.w3schools.com/jsref/met_win_setinterval.asp     

    // Update the count down every 1 second
    var x = setInterval(function() {
    // Get todays date and time
    var now = new Date().getTime();

    var distance = now - startTime - pauseInterval;

    var seconds = Math.floor(distance / 1000);

    // Output the result in an element with id
    document.getElementById("clockId").innerHTML =  seconds + "s ";
    });

# Progress Bar for counting down    
https://www.w3schools.com/howto/howto_js_progressbar.asp    

    function move() {
    var elem = document.getElementById("myBar");
    var width = 10;
    var id = setInterval(frame, 10);
    function frame() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++;
            elem.style.width = width + '%';
            elem.innerHTML = width * 1 + '%';
        }
    }
    } 

# Style width Property     
https://www.w3schools.com/jsref/prop_style_width.asp    

    object.style.width = "auto|length|%|initial|inherit" 



