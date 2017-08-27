var once = false;
window.addEventListener("load", function () {
    if ( once == true ) { return; }
    setTimeout(function(){
        if(confirm( 'A new episode of Game of Thrones aired on August 20, 2017! Add spoilers protection?' )){
            alert("yes");
        } else {
            alert("no");
        }
    }, 2000);
    once = true;
}, false);