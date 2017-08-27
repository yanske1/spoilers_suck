var HIDDEN = []

async function checkSpoiled(text) {
    if (!text || text.length < 5) return;
    
    return await $.ajax({
		url: API_URL + '/text',
		type:'POST',
        data: JSON.stringify({
            'content': text,
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

async function checkSpoiledImage(url){
    if (!url) return;

    return await $.ajax({
		url: API_URL + '/img',
		type:'POST',
        data: JSON.stringify({
            'url': url,
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

function addBlur(elem) {

	if(elem.spoil) {
		return;
    } 
    
    if($(elem).is("img")){
        checkSpoiledImage(elem.src.replace(/^data:image\/(png|jpg);base64,/, ''))
            .then((result) => {
                if (result) {
                    elem.spoil = {};

                    elem.style.webkitFilter = "blur(10px)";
                    elem.addEventListener("click", removeBlur, false);

                }
                else return;
            })
            .catch((err) => {
                console.error(err);
                return false;
            })
    } else {
        checkSpoiled(elem.textContent||elem.innerText)
        .then((result) => {
            if (result) {
                elem.spoil = {};

                var targetDiv = elem;

                if (targetDiv.tagName == "B" || targetDiv.tagName == "I" ) {
            
                    targetDiv = targetDiv.parentNode;

                }

                targetDiv.style.webkitFilter =  "blur(10px)";
                targetDiv.addEventListener("click", removeBlur, false);

                elem.spoil.div = targetDiv;
                HIDDEN.push(targetDiv);
            }
            else return;
        })
        .catch((err) => {
            console.error(err);
            return;
        })	    
    }
}


function removeBlur(){
	// Find index of offensive div
	var pos = HIDDEN.indexOf(this.parentNode);
	HIDDEN.splice(pos, 1);

	this.style.webkitFilter =  "blur(0px)";
	this.soothe = null;
}