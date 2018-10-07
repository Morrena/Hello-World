var text = document.getElementById('w-text').innerText;
var k = -1;
var interval = setInterval(function(){
	k++;
	if(k<text.length){
		var s = '';
		for(var i=0; i<=k; i++){ s += text[i]; }
		document.getElementById('w-text').innerText = s;
	}else if(k >= text.length*3){
		k = 0;
	}
}, 100);