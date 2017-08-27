console.log("MONICA");
var elements = document.getElementsByTagName('*');

for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        if (node.nodeType === 3) {
            var text = node.nodeValue;
            var replacedText = text.replace('Facebook', 'Cool');

            if (replacedText !== text) {
                element.replaceChild(document.createTextNode(replacedText), node);
            }
        }
    }
}

var images = document.getElementsByTagName('img');
for (var i = 0, l = images.length; i < l; i++) {
  if (APICALL(images[i].src)) {
      
  }
}