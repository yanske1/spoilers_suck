document.addEventListener('DOMContentLoaded', function() {
  chrome.storage.sync.get('got', function(items){
    if(items.got == true){
      document.getElementById('got').setAttribute("style","opacity: 0.5; filter: alpha(opacity=40);background-color: #000;");
      document.getElementById('got_check').setAttribute("style","display: inline;");
    }
  });

  document.getElementById('got').addEventListener('click', function(){
    var active = false;
    chrome.storage.sync.get('got', function(items){
      if(items.got == true){
        document.getElementById('got').setAttribute("style","opacity: 1;");
        document.getElementById('got_check').setAttribute("style","display: None;");
        chrome.storage.sync.set({'got': false}, function() {});
      } else {
        document.getElementById('got').setAttribute("style","opacity: 0.5; filter: alpha(opacity=40);background-color: #000;");
        document.getElementById('got_check').setAttribute("style","display: inline;");
        chrome.storage.sync.set({'got': true}, function() {});
      }
    });
  });
}, false);