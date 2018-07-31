# Inset video in guide page   

The HTML <video> Element   

The controls attribute adds video controls, like play, pause, and volume.     
It is a good idea to always include width and height attributes. If height and width are not set, the page might flicker while the video loads.    
The <source> element allows you to specify alternative video files which the browser may choose from. The browser will use the first recognized format.     
The text between the <video> and </video> tags will only be displayed in browsers that do not support the <video> element.        
  
    <video width="320" height="240" controls>
      <source src="movie.mp4" type="video/mp4">
      <source src="movie.ogg" type="video/ogg">
      Your browser does not support the video tag.
    </video> 
    
HTML <video> Autoplay     
  

https://www.w3schools.com/htmL/html5_video.asp
