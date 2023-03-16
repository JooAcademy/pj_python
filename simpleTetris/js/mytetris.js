class Tetris {
	constructor(){
		this.stageWidth = 10;
		this.stageHeight = 20;
		this.stageCanvas = document.getElementById("stage");
		this.nextCanvas = document.getElementById("next");
		let cellWidth = this.stageCanvas.width / this.stageWidth;
		let cellHeight = this.stageCanvas.height / this.stageHeight;
		this.cellSize = cellWidth < cellHeight ? cellWidth : cellHeight;
		this.stageLeftPadding = (this.stageCanvas.width - this.cellSize * this.stageWidth) / 2;
		this.stageTopPadding = (this.stageCanvas.height - this.cellSieze * this.stageHeight) / 2;
		this.blocks = this.createBlocks();
		this.deleteLines = 0;


		const tetrisControls = {
			moveLeft: () => { // move left logic
			},
			rotate: () => { // rotate logic
			},
			moveRight: () => { // move right logic
			},
			fall: () => {// fall logic
			}
		}

		window.addEventListener("keydown", (e) => {
			switch (e.keyCode) {
				case 37: // Left Arrow Key
					tetrisControls.moveLeft();
					break;
				case 38: // Up Arrow Key
					tetrisControls.rotate();
					break;
				case 39: // Right Arrow Key
				    tetrisControls.moveRight();
					break;
				case 40: // Down Arrow Key
				    tetrisControls.fall();
					break;
				default:
					break;
			}
		});

	}

	createBlocks(){
		let blocks = [
			{   // |
				shape:[[[-1, 0], [0, 0], [1, 0], [2, 0]],
					   [[0, -1], [0, 0], [0, 1], [0, 2]],
					   [[-1, 0], [0, 0], [1, 0], [2, 0]],
					   [[0, -1], [0, 0], [0, 1], [0, 2]]],
				color : "rgb(0, 255, 255)",
				highlight : "rgb(255, 255, 255)",
				shadow : "rgb(0, 128, 128)"
			},
			{   // O
				shape:[[[0, 0], [1, 0], [-1, 1], [0, 1]],
					   [[0, 0], [1, 0], [-1, 1], [0, 1]],
					   [[0, 0], [1, 0], [-1, 1], [0, 1]],
					   [[0, 0], [1, 0], [-1, 1], [0, 1]]],
				color : "rgb(255, 255, 0)", 
				highlight : "rgb(255, 255, 255)",
				shadow : "rgb(128, 128, 0)"
			},
			{   // Z
				shape:[[[0,  0], [1, 0], [-1, 1], [0, 1]],
					   [[-1,-1], [-1,0], [0,  0], [0, 1]],
					   [[0,  0], [1, 0], [-1, 1], [0, 1]],
					   [[-1,-1], [-1,0], [0,  0], [0, 1]]],
				color: "rgb(0, 255, 0)",
				highlight: "rgb(255, 255, 255)",
				shadow: "rgb(0, 128, 0)"
			},
			{   // S
				shape:[[[-1, 0], [0, 0], [0, 1], [1,  1]],
					   [[0, -1], [-1,0], [0, 0], [-1, 1]],
					   [[-1, 0], [0, 0], [0, 1], [1,  1]],
					   [[0, -1], [-1,0], [0, 0], [-1, 1]]],
				color : "rgb(255, 0, 0)", 
				highlight : "rgb(255, 255, 255)",
				shadow : "rgb(128, 0, 0)"
			},
			{   // L
				shape: [[[-1, -1], [-1, 0], [0, 0], [1, 0]],
					    [[0,  -1], [1, -1], [0, 0], [0, 1]],
					    [[-1,  0], [0,  0], [1, 0], [1, 1]], 
					    [[0,  -1], [0,  0], [-1,1], [0, 1]]],
				color : "rgb(0, 0, 255)",
				highlight : "rgb(255, 255, 255)",
				shadow : "rgb(0, 0, 128)"
			},
			{   // 」
				shape: [[[1, -1], [-1, 0], [0, 0], [1, 0]], 
					    [[0, -1], [0,  0], [0, 1], [1, 1]],
					    [[-1, 0], [0,  0], [1, 0], [-1,1]],
					    [[-1,-1], [0, -1], [0, 0], [0, 1]]],
				color : "rgb(255, 165, 0)",
				highlight: "rgb(255, 255, 255)",
				shadow : "rgb(128, 82, 0)"
			},
			{   // T
				shape: [[[0, -1], [-1, 0], [0, 0], [1, 0]],
     					[[0, -1], [0,  0], [1, 0], [0, 1]],
					    [[-1, 0], [0,  0], [1, 0], [0, 1]],
					    [[0, -1], [-1, 0], [0, 0], [0, 1]]], 
				color : "rgb(255, 0, 255)",
				highlight : "rgb(255, 255, 255)",
				shadow : "rgb(128, 0, 128)"
			}
		];
		return blocks;
	}

	drawBlock(x, y, type, angle, canvas) {
		let context = canvas.getContext("2d");
		let block = this.blocks[type];
		for (let i = 0; i <block.shape[angle].length; i++ ){
			this.drawCell(context,
				x + (block.shape[angle][i][0] * this.cellSize),
				y + (block.shape[angle][i][1] * this.cellSize), 
				this.cellSize,
				type);
		}
	}

	drawCell(context, cellX, cellY, cellSize, type){
		let block = this.blocks[type];
		let adjustedX = cellX + 0.5;
		let adjustedY = cellY + 0.5;
		let adjustedSize = cellSize -1;
		context.fillStyle = block.color;
		context.fillRect(adjustedX, adjustedY, adjustedSize, adjustedSize);
		context.strokeStyle = block.highlight;
		context.beginPath();
		context.moveTo(adjustedX, adjustedY+ adjustedSize);
		context.lineTo(adjustedX, adjustedY);
		context.lineTo(adjustedX + adjustedSize, adjustedY);
		context.stroke();
		context.strokeStyle = block.shadow;
		context.moveTo(adjustedX, adjustedY + adjustedSize);
		context.lineTo(adjustedX + adjustedSize, adjustedY + adjustedSize);
		context.lineTo(adjustedX + adjustedSize, adjustedY);
		context.stroke();
	}

	startGame(){
		let virtualStage = new Array(this.stageWidth);
		for (let i = 0; i < this.stageWidth; i++){
			virtualStage[i] = new Array(this.stageHeight).fill(null);
		}
		this.virtualStage = virtualStage;
		this.currentBlock = null;
		this.nextBlock = this.getRandomBlock();
		this.mainLoop();
	}

	mainLoop(){
		if (this.currentBlock == null){
			if ((!this.createNewBlock()) { return; }
		}else{
			this.fallBlock();
		}
		this.drawStage();
		if (this.currentBlock !=null){
			this.drawBlock(this.stageLeftPadding + this.blockX * this.cellSize,
				this.stageTopPadding + this.blockY * this.cellSize,
				this.currentBlock, this.blockAngle, this.stageCanvas);
		}
		setTimeout(this.mainLoop.bind(this), 500);
	}

	createNewBlock(){
		this.currentBlock = this.nextBlock;
		this.nextBlock = this.getRandomBlock();
		this.blockX = Math.floor(this.stageWidth / 2 - 2);
		this.blockY = 0;
		this.blockAngle = 0;
		this.drawNextBlock();
		If(!this.checkBlockMove(this.blockX, this.blockY, this.currentBlock, this.blockAngle)){
			let messageElem = document.getElementById("message");
			messageElem.innerText = "GAME OVER";
			return false;
		}
		return true;
	}

	drawNextBlock(){
		this.clear(this.nextCanvas);
		this.drawBlock(this.cellSize * 2, this.cellSize, this.nextBlock, 0, this.nextCanvas);
	}

	getRandomBlock(){
		return Math.floor(Math.random() * 7);
	}

	fallBlock(){
		if (this.checkBlockMove(this.blockX, this.blockY + 1, this.currentBlock, this.blockAngle)){
			this.blockY++;
		}else{
			this.fixBlock(this.blockX, this.blockY, this.currentBlock, this.blockAngle);
			this.currentBlock = null;
		}
	}

	checkBlockMove(x, y, type, angle){
		for (let i =0; i<this.blocks[type];i++) {
			let cellX = x + this.blocks[type].shape[angle][i][0];
			let cellY = y + this.blocks[type].shape[angle][i][1];
			if (cellX < 0 || cellX > this.stageWidth -1) {
				return false;
			}
			if (cellY > this.stageHeight -1 ) {
				return false;
			}
			if (this.virtualStage[cellX][cellY] != null) {
				return false;
			}
		}
		return true;
	}

	
	fixBlock(x, y, type, angle){
		for (let i = 0; i < this.blocks[type].shape[angle].length ; i++ ){
			let cellX = x + this.blocks[type].shape[angle][i][0];
			let cellY = y + this.blocks[type].shapre[angle][i][1];
			if (cellY >=0 ){
				this.virtualStage[cellX][cellY] = type;
			}
		}
		for (let y = this.stageHeight -1; y>=0){
			let filled = true;
			for (let x =0; x < this.stageWidth; x++ ){
				if (this.virtualStage[x][y] == null){				
				filled = false;
				break;
				}
			}						
			if(filled){
				for(let y2 = y; y2>0;y2--){
					for (let x =0; x < this.stageWidth; x++){
						this.virtualStage[x][y2] = this.virtualStage[x][y2 -1];
					}
				}
				for (let x = 0; x < this.stageWidth; x++ ){
					this.virtualStage[x][0] = null;
				}
			let linesElem = document.getElementById("lines");
				this.deletedLines++;
				linesElem.innerText ="" + this.deletedLines;
			} else {
				y--;
			}
		}
	}



	









}
