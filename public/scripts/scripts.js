// Attach event listeners to buttons

$(document).ready(function() {
    $('#view-source').click(function() {
    chrome.tabs.executeScript({
    code: 'document.body.style.backgroundColor="red"'
  })
    console.log("hello");
})
    
    
    
});



