var snakeSize = 10; 
var score = 0;
var snake;

var drawModule=(function(){

	var drawSnake=function(){
		var length = 4;
		snake = [];
		for (var i = length-1; i>=0; i--) {
			snake.push({x:i, y:0});
		}
	};
	var createFood=function(){
		food = {
			x: Math.floor((Math.random() * 30) + 1),
			y: Math.floor((Math.random() * 30) + 1)
		}

		for (var i=0; i>snake.length; i++) {
			var snakeX = snake[i].x;
			var snakeY = snake[i].y;

			if (food.x===snakeX && food.y === snakeY || food.y === snakeY && food.x===snakeX) {
				food.x = Math.floor((Math.random() * 30) + 1);
				food.y = Math.floor((Math.random() * 30) + 1);
			}
		}
	};
	var snakeBody=function(x,y){
		ctx.fillStyle='black';
		ctx.fillStyle = 'black';
		ctx.fillRect(x*snakeSize, y*snakeSize, snakeSize, snakeSize);
	};
	var drawFood=function(x,y){
		ctx.fillStyle = 'red';
		ctx.fillRect(x*snakeSize+1, y*snakeSize+1, snakeSize-2, snakeSize-2);
	};

	var paint=function(){
		ctx.fillStyle = '#137A04';
		ctx.fillRect(0, 0, 600, 600);
		ctx.strokeStyle = 'black';
		ctx.strokeRect(0, 0, 600, 600);

		btn.setAttribute('disabled', true);

		var snakeX = snake[0].x;
		var snakeY = snake[0].y;

		if (direction == 'right')  
			snakeX++; 
		else if (direction == 'left') 
			snakeX--; 
		else if (direction == 'up') 
			snakeY--; 
		else if(direction == 'down') 
			snakeY++; 

		if (snakeX==-1 || snakeX == 600/snakeSize || snakeY==-1 || snakeY == 600/snakeSize || checkCollision(snakeX, snakeY, snake)) {

			btn.removeAttribute('disabled', true);

			ctx.clearRect(0,0,600,600);
			gameloop = clearInterval(gameloop);
			var score_text=document.getElementById('score');
			score_text.innerHTML="You scored "+ score+" points!! Play Again!";
			return;          
		}

		if(snakeX == food.x && snakeY == food.y) 
		{
			var tail = {x: snakeX, y: snakeY}; 
			score ++;
			createFood(); 
		} 
		else 
		{
			var tail = snake.pop(); 
			tail.x = snakeX; 
			tail.y = snakeY;
		}

		snake.unshift(tail);

		for(var i = 0; i < snake.length; i++) {
			snakeBody(snake[i].x, snake[i].y);
		}

		drawFood(food.x,food.y);
	};

	var checkCollision = function(x, y, array) {
		for(var i = 0; i < array.length; i++) {
			if(array[i].x === x && array[i].y === y)
				return true;
		} 
		return false;
	}

	var init=function(){
		direction = 'down';
		drawSnake();
		createFood();
		score=0;
		gameloop = setInterval(paint, 100);
	};

	return {
		init:init
	};
}());
