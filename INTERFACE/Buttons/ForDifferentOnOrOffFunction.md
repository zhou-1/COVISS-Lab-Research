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

# TAB for toggle between flower and background in category list     
ASCII value for tab is 9 (decimal or hex)    

      else if (e.which == 9){//tab
      e.preventDefault(); // Prevent the default action
      var element = document.getElementById('dcolor');
      if(element.value == 1)
        element.value = 2;
      else if(element.value == 2)
        element.value = 1;
      var event = new Event('change');
      element.dispatchEvent(event);
    }
  };
