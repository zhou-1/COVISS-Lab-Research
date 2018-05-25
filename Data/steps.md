# step 1. get data from user side (x,y coordinates)   
1. send form data, but not variables we have for x and y, pass    
2. web storage/DOM storage, is not automatically transmitted to the server in every HTTP request, and a web server can't directly write to Web storage, pass    
3. cookies. session cookies are enough to use. but hard to analysis. pass     
4. send back variables in javaScript while updating values in HTML. did not find a way doing this.      
5. collect all data together in user's web storage and then send back to server with click button   


# step 2. collect all data user have dynamaticlaly   


