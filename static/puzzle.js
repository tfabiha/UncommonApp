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
			   })
};

// SETUP FOR FINDING SOLVED STATE
var row = 0;
var column = 0;
var UL = [];
var UR = [];
var LL = [];
var LR = [];

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
}

setup();

"""
console.log(UL);
console.log(UR);
console.log(LL);
console.log(LR);
"""

var solvedstate = function(e)
{
    var solved = true;
    
    var upper_change = []
    var bottom_change = []
    
    for (var i = 0; i < 3; i++)
    {
	upper_change.push( (UR[i] - UL[i]) / column );
	bottom_change.push( (LR[i] - LL[i]) / column );
    }

    for (var c = 0; c < columns; c++)
    {
	// get the stuff done :((((
	
	if (!solved)
	{
	    break;
	}
    }
    
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
       clicked = [];
    }

}
