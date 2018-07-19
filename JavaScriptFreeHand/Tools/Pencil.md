# Pencil drawing tool    

      // The drawing pencil.
  tools.pencil = function () {
    var tool = this;
    this.started = false;

    document.body.style.cursor = "url('/static/images/pencilB.png') 0 0, default";

    // This is called when you start holding down the touch.
    // This starts the pencil drawing.
    this.touchstart = function (ev) {
        
        // this prevents the page to scroll while drawing on temp_canvas
        if (ev.target == temp_canvas) {
          ev.preventDefault();
        }

        var x = ev._x;
        var y = ev._y;

        temp_context.beginPath();
        temp_context.moveTo(ev._x, ev._y);
        tool.started = true;
    };

    // This is called when you start holding down the mouse button.
    // This starts the pencil drawing.
    this.mousedown = function (ev) {
        var x = ev._x;
        var y = ev._y;

        temp_context.beginPath();
        temp_context.moveTo(ev._x, ev._y);
        tool.started = true;
    };


    // This function is called every time you move the finger. Obviously, it only 
    // draws if the tool.started state is set to true (when you are holding down 
    // the mouse button).
     this.touchmove = function (ev) {
      if (tool.started) {
        // this prevents the page to scroll while drawing on temp_canvas
        if (ev.target == temp_canvas) {
          ev.preventDefault();
        }

        var color_select = document.getElementById('dcolor').value;
        var z = document.getElementById('dcolor').value;
        if(color_select == 1)
          temp_context.strokeStyle = 'rgb(0,0,0)';
        else if(color_select == 2)
          temp_context.strokeStyle = 'rgb(128,0,0)';
        else if(color_select == 3)
          temp_context.strokeStyle = 'rgb(0,128,0)';
        else if(color_select == 4)
          temp_context.strokeStyle = 'rgb(128,128,0)';
        else if(color_select == 5)
          temp_context.strokeStyle = 'rgb(0,0,128)';
        else if(color_select == 6)
          temp_context.strokeStyle = 'rgb(128,0,128)';
        else if(color_select == 7)
          temp_context.strokeStyle = 'rgb(0,128,128)';
        else if(color_select == 8)
          temp_context.strokeStyle = 'rgb(128,128,128)';
        else if(color_select == 9)
          temp_context.strokeStyle = 'rgb(64,0,0)';
        else if(color_select == 10)
          temp_context.strokeStyle = 'rgb(192,0,0)';
        else if(color_select == 11)
          temp_context.strokeStyle = 'rgb(64,128,0)';
        else if(color_select == 12)
          temp_context.strokeStyle = 'rgb(192,128,0)';
        else if(color_select == 13)
          temp_context.strokeStyle = 'rgb(64,0,128)';
        else if(color_select == 14)
          temp_context.strokeStyle = 'rgb(192,0,128)';
        else if(color_select == 15)
          temp_context.strokeStyle = 'rgb(64,128,128)';
        else if(color_select == 16)
          temp_context.strokeStyle = 'rgb(192,128,128)';
        else if(color_select == 17)
          temp_context.strokeStyle = 'rgb(0,64,0)';
        else if(color_select == 18)
          temp_context.strokeStyle = 'rgb(128,64,0)';
        else if(color_select == 19)
          temp_context.strokeStyle = 'rgb(0,192,0)';
        else if(color_select == 20)
          temp_context.strokeStyle = 'rgb(128,192,0)';
        else if(color_select == 21)
          temp_context.strokeStyle = 'rgb(0,64,128)';
        else 
          temp_context.strokeStyle = 'grey';


        var size_select = document.getElementById('dsize').value;
        if(size_select == "small")
          temp_context.lineWidth = 1;
        else if(size_select == "normal")
          temp_context.lineWidth = 2; 
        else if(size_select == "large")
          temp_context.lineWidth = 4;
        else if(size_select == "huge")
          temp_context.lineWidth = 8;  

        temp_context.globalCompositeOperation="source-over";
     
        var x = ev._x;
        var y = ev._y;

        temp_context.lineTo(ev._x, ev._y);
        temp_context.stroke();

        thick = temp_context.lineWidth;

        trace.push(x,y,thick,z);

        document.getElementById("imageTemp").ontouchleave = function(){touchLeave()}; 

        function touchLeave() {
          tool.started = false;

          $.ajax({
            url: 'test/',
            type: 'POST',
            data: {'trace': trace},     
            success: function(resp){
              document.getElementById("imageTemp").ontouchleave = function(){}
            }

          });
          trace = [];
          img_update();
        
          }

      }
    };

    // This function is called every time you move the mouse. Obviously, it only 
    // draws if the tool.started state is set to true (when you are holding down 
    // the mouse button).
    this.mousemove = function (ev) {

      if (tool.started) {

        var color_select = document.getElementById('dcolor').value;
        var z = document.getElementById('dcolor').value;
        if(color_select == 1)
          temp_context.strokeStyle = 'rgb(0,0,0)';
        else if(color_select == 2)
          temp_context.strokeStyle = 'rgb(128,0,0)';
        else if(color_select == 3)
          temp_context.strokeStyle = 'rgb(0,128,0)';
        else if(color_select == 4)
          temp_context.strokeStyle = 'rgb(128,128,0)';
        else if(color_select == 5)
          temp_context.strokeStyle = 'rgb(0,0,128)';
        else if(color_select == 6)
          temp_context.strokeStyle = 'rgb(128,0,128)';
        else if(color_select == 7)
          temp_context.strokeStyle = 'rgb(0,128,128)';
        else if(color_select == 8)
          temp_context.strokeStyle = 'rgb(128,128,128)';
        else if(color_select == 9)
          temp_context.strokeStyle = 'rgb(64,0,0)';
        else if(color_select == 10)
          temp_context.strokeStyle = 'rgb(192,0,0)';
        else if(color_select == 11)
          temp_context.strokeStyle = 'rgb(64,128,0)';
        else if(color_select == 12)
          temp_context.strokeStyle = 'rgb(192,128,0)';
        else if(color_select == 13)
          temp_context.strokeStyle = 'rgb(64,0,128)';
        else if(color_select == 14)
          temp_context.strokeStyle = 'rgb(192,0,128)';
        else if(color_select == 15)
          temp_context.strokeStyle = 'rgb(64,128,128)';
        else if(color_select == 16)
          temp_context.strokeStyle = 'rgb(192,128,128)';
        else if(color_select == 17)
          temp_context.strokeStyle = 'rgb(0,64,0)';
        else if(color_select == 18)
          temp_context.strokeStyle = 'rgb(128,64,0)';
        else if(color_select == 19)
          temp_context.strokeStyle = 'rgb(0,192,0)';
        else if(color_select == 20)
          temp_context.strokeStyle = 'rgb(128,192,0)';
        else if(color_select == 21)
          temp_context.strokeStyle = 'rgb(0,64,128)';
        else 
          temp_context.strokeStyle = 'grey';


        var size_select = document.getElementById('dsize').value;
        if(size_select == "small")
          temp_context.lineWidth = 1;
        else if(size_select == "normal")
          temp_context.lineWidth = 2; 
        else if(size_select == "large")
          temp_context.lineWidth = 4;
        else if(size_select == "huge")
          temp_context.lineWidth = 8;   

        temp_context.globalCompositeOperation="source-over";
     
        var x = ev._x;
        var y = ev._y;

        temp_context.lineTo(ev._x, ev._y);
        temp_context.stroke();

        thick = temp_context.lineWidth;

        trace.push(x,y,thick,z);

        document.getElementById("imageTemp").onmouseout = function(){mouseOut()}; 

        function mouseOut() {
          // alert("hi");
          //tool.mousemove(ev);
          tool.started = false;

          $.ajax({
            url: 'test/',
            type: 'POST',
            data: {'trace': trace},     
            success: function(resp){
              document.getElementById("imageTemp").onmouseout = function(){}
            }

          });
          trace = [];
          img_update();        
        }

      }
    };

    // This is called when you release the touch button.
    this.touchend = function (ev) {


      if (tool.started) {
        // this prevents the page to scroll while drawing on temp_canvas
        if (ev.target == temp_canvas) {
          ev.preventDefault();
        }

        // tool.touchmove(ev);
        tool.started = false;

        $.ajax({
          url: 'test/',
          type: 'POST',
          data: {'trace': trace},
          success: function(){
                trace = [];
          },   
          error: function(){
                trace = [];
          }          
        });

        img_update();

        trace_number += 1;
      }
    };

    // This is called when you release the mouse button.
    this.mouseup = function (ev) {
      if (tool.started) {
        // tool.mousemove(ev);
        tool.started = false;

        $.ajax({
          url: 'test/',
          type: 'POST',
          data: {'trace': trace},     
          success: function(){
            trace = [];
            img_update();

            trace_number += 1;
          },
          error: function(){
              trace = [];
          } 
        });
      }
    };
  };

