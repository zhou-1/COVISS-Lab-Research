# Save a file with click "next image" button    

When you click "Next image", automatically save a file (.txt, .xls or whatever you prefer) with:    

- image id (that "i" variable in the HTML code); solved   
- time spend on the image; solved     
- number of traces; solved    


- number of pixels traced (accumulate the length of all traces)    


- number of clicks on "Refine"   solved    
- the average accuracy obtained    solved    

# Use POST to get the needed data    
create file and append data inside    
https://www.guru99.com/reading-and-writing-files-in-python.html     

# Write data for int in file with python       
a.write(str(num))     
https://stackoverflow.com/questions/11160939/writing-integer-values-to-a-file-using-out-write     

# Writing to a new file if it doesn't exist, and appending to a file if it does   
https://stackoverflow.com/questions/20432912/writing-to-a-new-file-if-it-doesnt-exist-and-appending-to-a-file-if-it-does      


# Calling a variable from one function to another function in Python    
actually any programming language can use this way   

    def get_email_address():
    #the code to open up a window that gets the email address
    Email = input
    return Email

    def get_email_username():
    #the code to open up a window that gets email username
    Email_Username = input
    return Email_Username

    #same for the email recipient and email password

    def send_email():
    # variables from the other def's
    email_address = get_email_address()
    email_username = get_email_username()

    #code to send email
    
   
   
# Elements   
writeFile()    
id: id_image, i     
time: final_seconds, seconds      
trace number: trace_number, trace_number     
length of trace；   
number of click refine: refine_number, callCnt2     
accuracy of average results: avg_accuracy, strAvg    






