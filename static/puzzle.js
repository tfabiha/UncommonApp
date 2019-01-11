// obtains list of all tiles that are in play
var sq = document.getElementsByClassName('box');

var clicked = []; // will contain list of currently clicked boxes

// for each tile adds in an eventlistener to handle swaping
for (var i = 0; i < sq.length; i++)
{
    sq[i].addEventListener('click', function()
			   {
			       clicked.push(this); // appends to array clicked
			       swap(); // handles swaping if applicable
			   })
};

// will handle swaping two clicked tiles
var swap = function(e)
{
    // ADD OPTION TO UNCLICK TILES

    // makes clicked tile visible to the user
    clicked[0].style.border = '5px solid white'

    // swap the two tiles
    if (clicked.length == 2)
    {
	     console.log(clicked);
	     var color = clicked[0].style.backgroundColor;

	     clicked[0].style.backgroundColor = clicked[1].style.backgroundColor;
	     clicked[1].style.backgroundColor = color;
	     clicked[0].style.border = '0px';
       clicked = [];
    }

}
