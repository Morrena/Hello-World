function view_image(urls, default_url, root_url){
	var prev = 0, next = 0, default_order = 0, sum=0;
	for(var key in urls){
		sum++;
		if(urls[key] == default_url){
			default_order = sum;
		}
	}
	if(default_order > 0 && default_order <= sum){
		//Create Element.remove() function if not exist
		if( !('remove' in Element.prototype) ){
			Element.prototype.remove = function(){
				if(this.parentNode){
					this.parentNode.removeChild(this);
				}
			}
		}
		var element = document.getElementById('view_image_field');
		if(typeof(element) != 'undefined' && element != null){
			element.remove();
		}

		var view_image_field = document.createElement('div');
		var elements = '';
		elements += '<div id="btn_close_img">x</div>';
		if(default_order>1){
			elements += '<div id="btn_prev"><</div>';
		}
		if(default_order<sum){
			elements += '<div id="btn_next">></div>';
		}
		elements += '<img src="' + default_url + '" id="vi_image"/>';
		
		view_image_field.innerHTML = elements;	//Setting the inner_elements of the view_img_field
		view_image_field.setAttribute('id', 'view_image_field');
		document.body.appendChild(view_image_field);//AFTER ALL, ADDING THE ELEMENTS TO THE BODY
		
		//STYLING-------------------------------------------------------------------------------------------------------------------------------------------------
		//window.scrollTo(0,0);

		var element = document.getElementById('vi_style');
		if(typeof(element) != 'undefined' && element != null){
			element.remove();
		}
		
		//OPERATIONS-------------------------------------------------------------------------------------------------------------------------------------------------
		//Closing the image player
		document.getElementById('btn_close_img').onclick = function(){
			view_image_field.remove();
		}
		//Getting the previous image
		if(default_order>1){
			document.getElementById('btn_prev').onclick = function(){
				view_image(urls, urls[default_order-1], root_url);
			}
		}
		//Getting the next image
		if(default_order<sum){
			document.getElementById('btn_next').onclick = function(){
				view_image(urls, urls[default_order+1], root_url);
			}
		}

		document.onkeydown = checkKey;

		function checkKey(e) {

		    e = e || window.event;

		   // if (e.keyCode == '38') {
		        // up arrow
		  //  }
		   // else if (e.keyCode == '40') {
		        // down arrow
		   // }
			if (e.keyCode == '37') {
				// left arrow
				if(default_order>1){
					view_image(urls, urls[default_order-1], root_url);
				}
			}
			else if (e.keyCode == '39') {
				// right arrow
				if(default_order<sum){
					view_image(urls, urls[default_order+1], root_url);
				}
			}

		}
	}
}