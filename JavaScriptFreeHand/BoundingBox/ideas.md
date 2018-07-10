# Bounding box based on coordinates         
canvas rect() Method         


    <script>
    window.onload = function() {
      var c=document.getElementById("myCanvas");
      var ctx=c.getContext("2d");
      var img=document.getElementById("scream");  
      ctx.drawImage(img,10,10);  
      var canvas = document.getElementById('myCanvas');
      var context = canvas.getContext('2d');

      context.beginPath();
      context.rect(188, 50, 200, 100);
      context.fillStyle = 'yellow';
      context.fill();
      context.lineWidth = 7;
      context.strokeStyle = 'black';
      context.stroke();
    }
    </script>    

Referred from: https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_canvas_rect2    
https://stackoverflow.com/questions/26902084/html5-canvas-how-to-draw-rectangle-over-image-in-canvas    


    // load bounding box list
    var bound = bbArray[listIDs[i]];

    // code here to use the dimensions
    var img_size = [img.naturalHeight, img.naturalWidth];
        
    $.ajax({
      url: 'initanns/',
      type: 'POST',
      data: {"img_size": img_size},
      // dataType: "json",
      success: function(resp){
        //img.onload = function(){}

        $.ajax({
          url: 'urlSend/',
          type: 'POST',
          data: {"BB": bound},
          success: function(data) {
           //do sth here
                    
                }
              }
            });  

        }
      }); 
      
      
      
# APPLY ON BELOW FUNCTIONS
callRefine(), img_update(), on load image.      
