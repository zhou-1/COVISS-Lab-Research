# Different button on keyboard controls one on/off button  

# M for mask
M is 77 in ASCII values.      

# B for bounding box   
B is 66 in ASCII values.     

# T for trace    
T is 84 in ADCII values.     


      document.onkeyup = function(e) {
      if (e.which == 77) {  //M
      //alert("M key was pressed");
      maskOnTraces();
      } else if (e.which == 66){  //B
      //alert("B");
      boundingBoxOn();
      } else if (e.which == 84){  //B
      //alert("T");
      TraceOnTempCanvas();
      }
      //else if (e.ctrlKey && e.which == 66) {   //ctrl + B
      //alert("Ctrl + B shortcut combination was pressed");
      //} 
      };
