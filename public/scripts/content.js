const API_URL = "https://spoilers-suck.herokuapp.com";

debugger;

var elements = document.getElementsByTagName('*'); // try to remove img
let textElements = getTextNodesIn(document);

for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    // for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        // if the node is a text type
        if (node.nodeType === 3) {
            var text = node.nodeValue; // unclear if sentence of text

            if ($.trim(text).split(' ').length < 3) {
                console.log(`skipped ${text}`);
                continue;
            }
            if (shouldFilterText(text)) {
                // hide the css THIS SHOULD BE CONTENT SCRIPT ... everything else should be background
                if (node.tagName == "B" || node.tagName == "I") {
                    node = node.parentNode;
                }
                // might need node.parentElement
                node.style.webkitFilter =  "blur(10px)";
			    node.addEventListener("click", makeVisible, false);
                
                // they added this to a hashmap with an index, so that when a user clicks on it again, it can keep track and unblur later
            }
            
            // else if (shouldFilterImage(text)) {
            //     // images might be filterable because text also refers to text of attributes
                
            // }

        } else if ($(node).is('img')) {
            console.log("img" + node.src);
        }
    // }
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
    this.style.webkitFilter = "blur(0px)";
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
		type:'POST',
        data: JSON.stringify({
            'content': divText,
        }),
        dataType: 'json',
		headers:{
            'Content-Type':'application/json',
        },
		success: function(data) {
			return data.should_censor; // i hate javascript why is this asyncronous
		},
		error: function() {
            console.log("Error making post request");
            return false;
        }
	});
}

function isSignificantSize(image) {
    return image.clientHeight > 50 && image.clientWidth > 50;
}

function shouldFilterImage(imgUrl){
    $.ajax({
		url: API_URL + '/img',
		type:'POST',
        data: JSON.stringify({
            'url': imgUrl
        }),
        dataType: 'json',
		headers:{
            'Content-Type':'application/json',
        },
		success: function(data) {
			return data.should_censor; // i hate javascript why is this asyncronous
		},
		error: function() {
            console.log("Error making post request");
            return false;
        }
	});
}

function getTextNodesIn(elem, opt_fnFilter) {
    var textNodes = [];
    if (elem) {
        for (var nodes = elem.childNodes; i = nodes.length; i-- ) {
            var node = nodes[i]
            if (node) {
                var nodeType = node.nodeType;
                if (nodeType ==3) {
                    if (!opt_fnFilter || opt_fnFilter(node, elem)) {
                        textNodes.push(node);
                    }
                }
                else if (nodeType == 1 || nodeType == 0 || nodeType == 11) {
                    textNodes = textNode.concat(getTextNodesIn(node, opt_fnFilter));
                }
                }
        }
    }
    return textNodes;
}