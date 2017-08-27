
    
var button = document.getElementById("view-source");
button.addEventListener("click", function(tab) {

    console.log('Turning ' + tab.url + ' red!');
      chrome.tabs.executeScript(null, {file: "content.js"}, function() {
      });

}, false);


