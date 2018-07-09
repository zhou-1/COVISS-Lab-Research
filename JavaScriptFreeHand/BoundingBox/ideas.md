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
