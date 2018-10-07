function slide(old, def){
	var left = (def-1)*(-100);
	document.getElementById('i-slide').style.marginLeft = (left) + '%';
	document.getElementById('indicator' + old).setAttribute('class', 'inline indicator');
	document.getElementById('indicator' + def).setAttribute('class', 'inline indicator_default');
	return def;
}
var def = 1, old = 1, sum = 3, j = 0;
document.getElementById('isc-right').onclick = function(){
	old = def;
	def += 1;
	if(def>sum){ def = 1; }
	slide(old, def);
	j = 0;		
}
document.getElementById('isc-left').onclick = function(){
	old = def;
	def -= 1;
	if(def<1){ def = sum; }
	slide(old, def);
	j = 0;
}
var interval = setInterval(function(){	
	j++;
	if(j==5){
		old = def;
		def += 1;
		if(def>sum){ def = 1; }
		slide(old, def);
		j = 0;
	}
}, 1000);