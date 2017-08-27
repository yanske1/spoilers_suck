// Attach event listeners to buttons

$(document).ready(function() {
    $('#view-source').click(function() {
        
        // load intensive background script on event
    chrome.tabs.executeScript(null, { file: "background.js"
  })
    console.log("hello");
})
    
    
    
});



