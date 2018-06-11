# No need for face_detector app   
change the photo in static/images folder    
use url image in the future   

# add option list for all diferent objects   
There are 21 objects    

# Each object corresponds to different color   
context.strokeStyle = 'red'; for color change in drawing tool.  
https://stackoverflow.com/questions/18093912/html-javascript-canvas-color-changing   

# show (x,y,id of object in final value)    
add var z after x and y    

     if(color_select == 'aero')
            var z = 1;
     else if(color_select == 'back')
            var z = 2;

# Use database in google drive to add URL to upload image  
step 1. upload 1 image via url   
https://www.w3schools.com/html/html_filepaths.asp    

step 2. from google drive  
Provided that you put your files in a public folder, you can get any file in a folder by this URL:    
https://googledrive.com/host/<folderID>/<filename>       
1- upload ur image    
2- right click and chose "get sharable link"   
3- copy the link which should look like    
https://drive.google.com/open?id=xxxxxxx    
4-change the open? to uc? and use it like     
<!--<img src="https://drive.google.com/uc?id=xxxxx">   --> 
https://stackoverflow.com/questions/10311092/displaying-files-e-g-images-stored-in-google-drive-on-a-website      
     
step 3. show all images one by one    


