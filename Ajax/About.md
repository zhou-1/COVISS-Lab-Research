# About Ajax & Intoduction    
https://www.w3schools.com/xml/ajax_intro.asp    

# Format    

    $.ajax({
      url: 'load/',
      type: 'POST',
      tryCount : 0,
      retryLimit : 3,      
      success: function(resp){
    }
    error : function(xhr, textStatus, errorThrown ) {
    },
      timeout: 10000
    }); 
    
