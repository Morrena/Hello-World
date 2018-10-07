var displayed = 0, height = menu_sum + 5, minHeight = 1.75, h, m;
document.getElementById('btn_menu_shower').onclick = function(){
	displayed = 1;
	if((document.body.clientWidth+17)<400){
		h = height - 0.55;
		m = minHeight - 0.55;
	}else{
		h = height;
		m = minHeight;
	}
	document.getElementById('menu').setAttribute('style', 'min-height: ' + h + 'cm;');
	var t;
	t += 'z-index: 4;';
	t += 'opacity: 0;';
	t += '-webkit-transform: rotate(10deg);';
	t += '-moz-transform: rotate(10deg);';
	t += '-o-transform: rotate(10deg);';
	t += 'transform: rotate(10deg);';
	document.getElementById('btn_menu_shower').setAttribute('style', t);
	t = '';
	t += 'z-index: 5;';
	t += 'opacity: 1;';
	t += '-webkit-transform: rotate(0deg);';
	t += '-moz-transform: rotate(0deg);';
	t += '-o-transform: rotate(0deg);';
	t += 'transform: rotate(0deg);';
	document.getElementById('btn_menu_hider').setAttribute('style', t);
}
document.getElementById('btn_menu_hider').onclick = function(){
	if((document.body.clientWidth+17)<400){
		h = height - 0.55;
		m = minHeight - 0.55;
	}else{
		h = height;
		m = minHeight;
	}
	displayed = 0;
	document.getElementById('menu').setAttribute('style', 'min-height: ' + m + 'cm;');
	var t;
	t += 'z-index: 4;';
	t += 'opacity: 0;';
	t += '-webkit-transform: rotate(10deg);';
	t += '-moz-transform: rotate(10deg);';
	t += '-o-transform: rotate(10deg);';
	t += 'transform: rotate(10deg);';
	document.getElementById('btn_menu_hider').setAttribute('style', t);
	t = '';
	t += 'z-index: 5;';
	t += 'opacity: 1;';
	t += '-webkit-transform: rotate(0deg);';
	t += '-moz-transform: rotate(0deg);';
	t += '-o-transform: rotate(0deg);';
	t += 'transform: rotate(0deg);';
	document.getElementById('btn_menu_shower').setAttribute('style', t);
}
window.onresize = function(event){
	if((document.body.clientWidth+17)<400){
		h = height - 0.55;
		m = minHeight - 0.55;
	}else{
		h = height;
		m = minHeight;
	}
	if(w_back == 1){
		document.getElementById('w_back').setAttribute('style', 'top: ' + (m-0.2) + 'cm;');
	}
	if((document.body.clientWidth+17) > 1000){ //17 gosanda window.innerWidth bn den bolya
		document.getElementById('menu').setAttribute('style', 'min-height: ' + m + 'cm;');
	}else if(displayed == 1){
		document.getElementById('menu').setAttribute('style', 'min-height: ' + h + 'cm;');
	}else{
		document.getElementById('menu').setAttribute('style', 'min-height: ' + m + 'cm;');
	}
}
window.onscroll = function(){
	if(document.body.scrollTop > 70 || document.documentElement.scrollTop > 70){
		document.getElementById('menu').setAttribute('class', 'menu_fixed');
		document.getElementById('menu-back-img').style.opacity = '0.3';
	}else{
		document.getElementById('menu').setAttribute('class', 'menu');
		document.getElementById('menu-back-img').style.opacity = '0';
	}
}