// obtains list of all tiles that are in play
var sq = document.getElementsByClassName("box");

var clicked = []; // will contain list of currently clicked boxes

// for each tile adds in an eventlistener to handle swaping
for (var i = 0; i < sq.length; i++)
{
    sq[i].addEventListener("click", function()
			   {
			       clicked.push(this); // appends to array clicked
			       swap(); // handles swaping if applicable
			   });
};

var resp = document.getElementsByClassName("response")[0];

sq = document.getElementsByClassName("rand")[0];
sq.addEventListener("click", function(e)
		    {
			resp.innerHTML = "";
			randomize();
		    });

sq = document.getElementsByClassName("check")[0];
sq.addEventListener("click", function(e)
		    {
			solvedstate();
		    });

var moves = 0;

// SETUP FOR FINDING SOLVED STATE
var row = 0;
var column = 0;

var UL = [];
var UR = [];
var LL = [];
var LR = [];

var puzzle = [];

var upper_change = []
var lower_change = []

var setup = function(e)
{
    // meta = [ROWxCOLUMN, UL, UR, LL, LR]
    var meta = document.getElementsByTagName("TABLE")[0].className.split(" ");

    // declare the rows and columns
    var temp = meta[0].split("x");
    row = parseInt( temp[0], 10 );
    column = parseInt( temp[1], 10 );

    for (var i = 1; i < meta.length; i++)
    {
	console.log(meta[i]);
	meta[i] = meta[i].split(",");

	temp = [];
	for (var j = 0; j < 3; j++)
	{
	    temp.push( parseInt( meta[i][j], 10 ) );
	}
	
	meta[i] = temp;
    }

    UL = meta[1];
    UR = meta[2];
    LL = meta[3];
    LR = meta[4];

    for (var r = 0; r < row; r++)
    {
	var one_row = [];

	for (var c = 0; c < column; c++)
	{
	    one_row.push( [] );
	}
	
	puzzle.push( one_row );
    }
        
    for (var i = 0; i < 3; i++)
    {
	upper_change.push( (UR[i] - UL[i]) / (column - 1) );
	lower_change.push( (LR[i] - LL[i]) / (column - 1) );
    }

    for (var c = 0; c < column; c++)
    {
	for (var i = 0; i < 3; i++)
	{
	    puzzle[0][c].push( UL[i] + upper_change[i] * c );
	    puzzle[row - 1][c]. push( LL[i] + lower_change[i] * c );
	}
    }

    for (var c = 0; c < column; c++)
    {
	var change = [];

	for (var i = 0; i < 3; i++)
	{
	    change.push( (puzzle[row - 1][c][i] - puzzle[0][c][i]) / (row - 1) );
	}

	for (var r = 0; r < row; r++)
	{
	    if (puzzle[r][c].length == 0)
	    { 
		
		for (var i = 0; i < 3; i++)
		{
		    puzzle[r][c].push( puzzle[0][c][i] + change[i] * r );
		}
		
	    }
	}
	
    }
}

setup();
console.log(puzzle);

var solvedstate = function(e)
{
    var solved = true;

    out:
    for (var r = 0; r < row; r++)
    {
	for (var c = 0; c < column; c++)
	{
	    var tile_class = "row_" + r + " column_" + c;
	    var tile = document.getElementsByClassName( tile_class )[0];
	    tile = tile.style.backgroundColor;

	    tile = tile.substring(4, tile.length - 1);
	    tile = tile.split(", ");

	    for (var i = 0; i < 3; i++)
	    {
		tile[i] = parseInt( tile[i], 10 );
	    }
	    
	    // console.log(tile);

	    for (var i = 0; i < 3; i++)
	    {
		// console.log(tile[i]);
		// console.log(Math.round(puzzle[r][c][i]));
		
		solved = solved & tile[i] == Math.round(puzzle[r][c][i]);
	    }
	    
	    if (!solved)
	    {
		break out;
	    }
	}
    }

    
    if (solved)
    {
	resp.innerHTML = "it's solved!";
	console.log("true");
    }
    else
    {
	resp.innerHTML = "wrong! try again";
	console.log("false");
    }

    return solved
}

// will handle swaping two clicked tiles
var swap = function(e)
{
    // ADD OPTION TO UNCLICK TILES

    // makes clicked tile visible to the user
    clicked[0].style.border = "5px solid white";

    // swap the two tiles
    if (clicked.length == 2)
    {
	console.log(clicked);
	var color = clicked[0].style.backgroundColor;
	
	clicked[0].style.backgroundColor = clicked[1].style.backgroundColor;
	clicked[1].style.backgroundColor = color;
	clicked[0].style.border = "0px";

	if ( clicked[0].style.backgroundColor != clicked[1].style.backgroundColor)
	{
	    moves += 1;
	}
	
	clicked = [];
    }

}

var randint = function(e)
{
    return Math.floor( Math.random() * e )
}

var randomize = function(e)
{
    for (var i = 0; i < 1000; i ++)
    {
	var tile0_coor = [randint(row), randint(column)];
	var tile1_coor = [randint(row), randint(column)];

	var tile0 = "row_" + tile0_coor[0] + " column_" + tile0_coor[1];
	tile0 = document.getElementsByClassName( tile0 )[0];

	var tile1 = "row_" + tile1_coor[0] + " column_" + tile1_coor[1];
	tile1 = document.getElementsByClassName( tile1 )[0];

	var color = tile0.style.backgroundColor;
	
	tile0.style.backgroundColor = tile1.style.backgroundColor;
	tile1.style.backgroundColor = color;
    }
}
