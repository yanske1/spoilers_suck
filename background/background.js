var once = false;
window.addEventListener("load", function () {
    if ( once == true ) { return; }

    if (chrome.storage.sync.get('got', function(items){
        if(items.got == true){
            return;
        }
    }));

    setTimeout(function(){
        if(confirm( 'A new episode of Game of Thrones aired on August 20, 2017! Add spoilers protection to Game of Thrones now?' )){
            chrome.storage.sync.set({'got': true}, function() {
                alert("saved t");
              });
        } else {
            chrome.storage.sync.set({'got': false}, function() {
                alert("saved f");
              })
        }
    }, 2000);
    once = true;
}, false);