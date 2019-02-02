var my_canvas=document.getElementById('SnakeGame');
var ctx=my_canvas.getContext('2d');

var btn = document.getElementById('start');
btn.addEventListener("click", function(){ drawModule.init();});

document.onkeydown = function(event) {

	keyCode = window.event.keyCode; 
	keyCode = event.keyCode;

	switch(keyCode) {
		
		case 37: if (direction != 'right') 
					direction = 'left';
				 break;

		case 39: if (direction != 'left') 
				 	direction = 'right';
				 break;

		case 38: if (direction != 'down') 
				 	direction = 'up';
				 break;

		case 40: if (direction != 'up')
				 	direction = 'down';
				 break;
	}
}
