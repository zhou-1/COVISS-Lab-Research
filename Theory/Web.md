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

Refine button.   



<b> When you load the webpage at first time </b>   
1.assign global variables pointing to the "definitive" (img) upper canvas    
2.use current time to define the name of the results (log) file (for example Results_{ID}.txt)    
3.initialize mouse cursor as pencil by default, load imag into cursor   
4.AJAX call to loadBatches() in views.py to get list of images and ids, call init() function, lookupInit() and loadImage();once error, try call ajax again and after retrylimit times, reload whole webpage.          
In <b>loadBatches()</b> function, open and save four lists for ApA, ApB, Peach and Pear, another four lists for corresponding ground truth. get username information and create a file for corresponding user. Shuffle once for the 4 no-GT lists. combine required information in single file, append elements in required order. After the loop, save the wole elements in a text. Finally return combinList, username and nextId.            
In <b>init()</b> function, find the canvas elements, get the 2D canvas context; add the temporary canvas that will contain the traces above the image canvas (give this temporary canvas id, width and height); get the tool, color, size select input and add event listener to changes; activate the default tool, color, size; attach mouse events, touch events listerners.     
In <b>lookupInit()</b> function, in previous version, we need it to calculate the score. No need for final version.           
In <b>loadImage()</b> function, save current cursor (pencil/line/erase) and then update to loading symbol-'wait'; clear previous traces upper canvas; clear URL of mask image on bottom canvas; get image URL according to index i and the randomly permuted list; 
set image URL to image element on bottom canvas; get selected transparency for image; img.onload to load image: display image ID to user..... until an ajax call (initFlAnns) to get size of image and create array with users' annotations (0 for initial, 1 for background later, 2 for flower later), using sessions allow us to keep updating and accessing this same variable back and forth in the views.py. Otherwise, if error, reload whole window page.     

<b> Refine button </b>    
1. save current state of cursor (pencil or line or eraser)     
2. switch mouse cursor to loading/wait symbol    
3. display "Refining.." icon    
4. hide Undo button and reactivate it only if traces.length > 0     
5. get pointer (like img, size of image) to image on bottom canvas     
6. increament counter of number of refinements performed    
7. 






# No need in flower AWS     
function lookupInit() //response to scores    
function getScore(acc)      
function getRandomColor()    
function drawBoundingBox()    




