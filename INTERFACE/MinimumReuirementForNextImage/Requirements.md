# 1. Try to move to Next Image only when you get this minimum accuracy.    
In function comparetoGT(), there is compare step and acc_.  

    //function handled with clear all traces on image
    function reloadImage()
    {
      reply_ = confirm("Average accuracy is lower than 90%, are you sure to continue?");

      if (reply_) {
        loadImage(i);
        trace = [];
      }          
    }  

based on the value of average accuracy, if it is none, show a warning; if it is less than expected, pop up a request window; if the average accuracy is satisifing for us, go to next image.    


# 2. Show elements in one image     
Not being considered now. 
