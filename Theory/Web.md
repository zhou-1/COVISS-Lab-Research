# Web    
<b> meta tag </b>     
The <meta> tag provides metadata about the HTML document. Metadata will not be displayed on the page, but will be machine parsable.     
Meta elements are typically used to specify page description, keywords, author of the document, last modified, and other metadata.      

<b> link tag </b>   
The <link> tag defines a link between a document and an external resource.      
The <link> tag is used to link to external style sheets.        

<b> main script </b>   
define a lot of global variables: a bunch of urls, image canvas, traces canvas, tools, accuracies, flags, time and so on.        
onkeyup for short-cut using keyboard. (preventDefault() method cancels the event if it is cancelable)    
window.onload to automatic run when window load. 




<b> When you load the webpage at first time </b>   
1.assign global variables pointing to the "definitive" (img) upper canvas    
2.use current time to define the name of the results (log) file (for example Results_{ID}.txt)    
3.initialize mouse cursor as pencil by default, load imag into cursor   
4.AJAX call to loadBatches() in views.py to get list of images and ids, call init() function, lookupInit() and loadImage();once error, try call ajax again and after retrylimit times, reload whole webpage.          
In loadBatches() function, open and save four lists for ApA, ApB, Peach and Pear, another four lists for corresponding ground truth. get username information and create a file for corresponding user. Shuffle once for the 4 no-GT lists. combine required information in single file, append elements in required order. After the loop, save the wole elements in a text. Finally return combinList, username and nextId.            
In init() function,  

In lookupInit() function,    

In loadImage() function,   
