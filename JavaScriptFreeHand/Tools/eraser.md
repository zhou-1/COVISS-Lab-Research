# Erasor tool  
Used for top canvas, temp_context   

  
    // eraser tool
    tools.eraser = function() {
    var tool = this;
    this.started = false;

    // change mouse icon to eraser
    document.body.style.cursor = "url('/static/images/eraser.png') 10 25, default";    

    var z = 0;
