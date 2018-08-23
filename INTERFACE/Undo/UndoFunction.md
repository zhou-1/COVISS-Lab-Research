# Undo button   
Created 

# Interface part
clear last trace, invisible   
replace category's ID by eraser's ID    


# Backend part    

get information for last trace in 
var undoArr = new Array() // array of previous traces, to guide undo, up to 5; in finish function, clear all traces      


pushundo() function     
everytime use eraser, pencil or line tool, push the latest trace
