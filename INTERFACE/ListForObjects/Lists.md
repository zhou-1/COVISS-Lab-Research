# Show a list for different objects beside the image   
In loadImage function and initial createUserAnns function, create a variable objects.    
convert string data.bbList to string array   

      var intbounding = linesbounding[i].split(",").map(String);   //string object
Then add in HTML    

       objects = objects + '</br>' + intbounding[4];
       
       document.getElementById("accId").innerHTML = objects;
