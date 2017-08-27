const API_URL = "https://spoilers-suck.herokuapp.com";

var elements = document.getElementsByTagName('*'); // try to remove img

for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        // if the node is a text type
        if (node.nodeType === 3) {
            var text = node.nodeValue; // unclear if sentence of text
            if (shouldFilterText(text)) {
                // hide the css THIS SHOULD BE CONTENT SCRIPT ... everything else should be background
                
                // might need node.parentElement
                node.style.visibility =  "hidden";
			     node.addEventListener("click", makeVisible, false);
                
                // they added this to a hashmap with an index, so that when a user clicks on it again, it can keep track and unblur later
            }
            
            else if (shouldFilterImage(text)) {
                // images might be filterable because text also refers to text of attributes
                
            }


        }
        else if (node.nodeT)
    }
}
/** The following is fo rreference
function removeBlur(){
	// Find index of offensive div
	var pos = SOOTHE_ELEMS.indexOf(this.parentNode);
	SOOTHE_ELEMS.splice(pos, 1);

	this.style.webkitFilter =  "blur(0px)";
	this.soothe = null;
} **/

function makeVisible () {
    this.style.visibility = "visible"
}

var images = document.getElementsByTagName('img');
for (var i = 0, l = images.length; i < l; i++) {
    
    // only hide significantly sized images
  if (isSignificantSize(images[i]) && shouldFilterImage(images[i].src)) {
      
  }
}

function shouldFilterText(divText) {
    $.ajax({
		url: API_URL + '/text',
		type:'GET',
        data: {
            'content': divText
        }
		headers:{
            'Content-Type':'application/json',
        },
		success: function(data) {
			return data.should_censor; // i hate javascript why is this asyncronous
		},
		error: function() {
            console.log("Error making Get request");
        }
	});
    
}

function isSignificantSize(image) {
    return image.clientHeight > 50 && image.clientWidth > 50;
}

function shouldFilterImage(imgUrl){
    $.ajax({
		url: API_URL + '/img',
		type:'GET',
        data: {
            'url': imgUrl
        }
		headers:{
            'Content-Type':'application/json',
        },
		success: function(data) {
			return data.should_censor; // i hate javascript why is this asyncronous
		},
		error: function() {
            console.log("Error making Get request");
            return false;
        }
	});
}