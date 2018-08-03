# Show item in category dynamically according to list of objects in current image    

# Show items in first page   
1. Give ID for all items in category   

2. Create an array to store all option IDs     

3. Get rid of related elements in current image with first for loop   

4. Get rid of background solo   

5. We have array with unrelated elements now. Get rid of them.  

Refer: Remove an element from an array, https://stackoverflow.com/questions/5767325/how-do-i-remove-a-particular-element-from-an-array-in-javascript    
Array length Property, https://www.w3schools.com/jsref/jsref_length_array.asp   

Problem: We deleted the items, we need to recreate all of the items now.    

# Show items in next pages   
1. In nextImage() function, delete all remaining elements in previous image    

2. Create a new full list for category in javascript including recover optionArray with 1 to 21       

3. give correct value to items in category list: Select a dropdown option by value   
refer from: http://www.imranulhoque.com/javascript/javascript-beginners-select-a-dropdown-option-by-value/    

4. delete unrelated elements   
