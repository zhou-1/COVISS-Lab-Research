# step 1. get data from user side (x,y coordinates)   
1. send form data, but not for variables we have for x and y, pass    
2. web storage/DOM storage, is not automatically transmitted to the server in every HTTP request, and a web server can't directly write to Web storage, pass    
3. cookies. session cookies are enough to use. but hard to analysis and use. pass     
4. send back variables in javaScript while updating values in HTML. did not find a way doing this.      
5. collect all data together in user's web storage and then send back to server with click button  


send form data: https://www.w3schools.com/jsref/met_form_submit.asp      
HTML web storage (session storage object): https://www.w3schools.com/Html/html5_webstorage.asp    



# step 2. collect all data user have dynamaticlaly   


