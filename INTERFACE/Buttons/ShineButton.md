# Shine/Blink Buttons      
Hover button, show shine effect.   
https://codepen.io/iamvdo/pen/maJhu    
http://cssdeck.com/labs/glossy-button-with-shine      
https://jsfiddle.net/AntonTrollback/nqQc7/   

# Shake the button    
https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_shake   

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    #click:hover {
      animation: shake 0.5s;
      animation-iteration-count: infinite;
    }

    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      20% { transform: translate(-3px, 0px) rotate(1deg); }
      30% { transform: translate(3px, 2px) rotate(0deg); }
      40% { transform: translate(1px, -1px) rotate(1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      60% { transform: translate(-3px, 1px) rotate(0deg); }
      70% { transform: translate(3px, 1px) rotate(-1deg); }
      80% { transform: translate(-1px, -1px) rotate(1deg); }
      90% { transform: translate(1px, 2px) rotate(0deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    </style>
    </head>
    <body>
    <p>Hover over the button:</p>
    <button id = "click" type="button">Click Me!</button>
    <button type="button">Click Me!!!!</button>
    </body>
    </html>
      
