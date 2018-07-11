# Use Ajax in necessory place.    
For load image/new image:  


          $.ajax({
                url: 'urlSend/',
                type: 'POST',
                data: {"BB": bound},
                success: function(data) {
                  var linesbounding = data.bbList;    //string

                  bb = []; //clear the array

                  for (var i = 0, len = linesbounding.length; i < len; i++) {
                    //alert( linesbounding[i])

                    //convert from string to int array include comma
                    var intbounding = linesbounding[i].split(",").map(Number);   //object

                    bb.push(intbounding)   //object

                    contexto.beginPath();
                    contexto.rect(intbounding[0], intbounding[1], intbounding[2], intbounding[3]);
                    //contexto.fillStyle = 'yellow';
                    //contexto.fill(); 
                    contexto.lineWidth = 2;

                    colorArray[i] = getRandomColor();
                    contexto.strokeStyle = colorArray[i];
                    contexto.stroke();

                    
                  }
                }
              });  


For other, in order to use in convenience:    

    function drawBoundingBox(){
          for (var j = 0; j < bb.length; j++) {

          // alert( bb[j][0])
          // alert(typeof bb[j][0])// number
        
          contexto.beginPath();
          contexto.rect(bb[j][0], bb[j][1], bb[j][2], bb[j][3]);

          contexto.lineWidth = 2;
          contexto.strokeStyle = colorArray[j];
          contexto.stroke();        
        
          }
     }
