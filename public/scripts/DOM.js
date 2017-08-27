const API_URL = "https://spoilers-suck.herokuapp.com";




/*
-----------------------------------------
FILTERING FUNCTIONS ARE BELOW...
-----------------------------------------
*/
function findOffensiveNodes(node, avoidRecurse) {

    if($(node).is('img')){
        console.log("Img " + node.src.replace(/^data:image\/(png|jpg);base64,/, ''));
        return NodeFilter.FILTER_ACCEPT;
    }

	// validate node
	if(!node || !node.parentElement){
		return NodeFilter.FILTER_REJECT;
	}

	// check if inside a script elements
	var ignoreElemTypes = ['SCRIPT', 'INPUT', 'TEXTAREA'];
	if(ignoreElemTypes.indexOf(node.parentElement.nodeName) !== -1) {
		return NodeFilter.FILTER_REJECT;
	}

	// validate that its not editableElems
	if(node.isContentEditable) {
		return NodeFilter.FILTER_REJECT;
	}

	// check that it's not hidden
	var hiddenDisp = ['hidden', 'none'];
	if(hiddenDisp.indexOf(window.getComputedStyle(node.parentElement).display) != -1) {
		return NodeFilter.FILTER_REJECT;
	}

	if(!avoidRecurse) {
		var hasEncChild = Array.prototype.reduce.call(node.childNodes, function (bool, childElem) {
			var filtVal = findOffensiveNodes(childElem, true);
			var validChild = (filtVal === NodeFilter.FILTER_ACCEPT && childElem.childElementCount);
			return bool || validChild;
		}, false);
		if(hasEncChild) {
			return NodeFilter.FILTER_SKIP;
        }
    }
    return NodeFilter.FILTER_ACCEPT;
}


function iterateOffensiveNodes(startElem, handler) {
	if(!(startElem instanceof Node)) return;
	var walker = document.createTreeWalker(startElem, NodeFilter.SHOW_ELEMENT, {
		acceptNode : findOffensiveNodes
	}, true);
	while(walker.nextNode()) {
        while(walker.firstChild()){}
        debugger;
		handler(walker.currentNode);
	}
}