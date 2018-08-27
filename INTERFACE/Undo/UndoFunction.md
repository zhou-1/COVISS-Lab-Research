# Undo button   
Created 

In undoTrace(), first check length of traces array. If it is empty, remove a trace drawn before last refine call, get last trace from global variable lastTrace, and convert into integer, get rid of trace in canvas side and erase from canvas, then replace last trace by eraser trace/ID so that next time click refine, python side will get last trace with eraser ID; else, if length of traces is not 0, just delete the last trace from the array.    

# Interface part
clear last trace, invisible   
replace category's ID by eraser's ID   
convert a trace into a eraser trace    

    var trace_ = [];
    for (j = 0; j < trace.length; j++) {
      trace_[j] = trace[j];
    }
    // replace category ID by eraser ID
    for (j = 3; j < trace_.length; j=j+4) {
      trace_[j] = 0;
    }

    traces.push(trace_)


# Backend part    
In callRefine() function, use a global variable in ajax to get the last trace before click refine     

    // backup/save the last trace: traces[traces.length-1]
    lastTrace = traces[traces.length-1];

get information for last trace in 
var undoArr = new Array() // array of previous traces, to guide undo, up to 5; in finish function, clear all traces      


pushundo() function     
everytime use eraser, pencil or line tool, push the latest trace
