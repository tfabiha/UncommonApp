// <!--
// # UncommonApp
// # Dennis Chen, T Fabiha, Addison Huang, Michelle Tang
// # P#02: The End
// -->
// Handles puzzles created by the user.
var color = [[], [], [], []];

window.onload = function()
{
    var preview_table = document.getElementById("preview-tiles");

    console.log(preview_table);

    var button = document.getElementsByName("preview")[0];
    button.addEventListener("click", function(e)
			    {
				preview();
			    }, false);
    console.log(button);

    var refresh = document.getElementById("randpal");
    console.log("refresh")
    refresh.addEventListener("click", function()
                             {
				 reloaded();
				 //location.reload();
				 //console.log("reloaded");
                             })

    var preview = function(e)
    {
	preview_table.innerHTML = "";

	if (checked())
	{
	    var puzzle = [];

	    var size = document.getElementsByName("size")[0].value;
	    console.log(size);
	    size = size.split("x");

	    var row = parseInt( size[0], 10 );
	    var column = parseInt( size[1], 10);

	    for (var i = 0; i < color.length; i++)
	    {
		console.log(color[i])
		color[i] = color[i].value;
		color[i] = color[i].substring(4, color[i].length - 1);

		console.log(color[i]);

		color[i] = color[i].split(",");

		temp = [];

		for (var j = 0; j < 3; j++)
		{
		    temp.push( parseInt( color[i][j], 10 ) );
		}

		color[i] = temp;
	    }

	    for (var i = 0; i < color.length; i++)
	    {
		console.log(color[i]);
	    }

	    for (var r = 0; r < row; r++)
	    {
		var one_row = [];

		for (var c = 0; c < column; c++)
		{
		    one_row.push( [] );
		}

		puzzle.push( one_row );
		console.log()
	    }

	    var upper_change = []
	    var lower_change = []

	    for (var i = 0; i < 3; i++)
	    {
     		upper_change.push( (color[1][i] - color[0][i]) / (column - 1) );
		lower_change.push( (color[3][i] - color[2][i]) / (column - 1) );
	    }

	    for (var c = 0; c < column; c++)
	    {
     		for (var i = 0; i < 3; i++)
		{
		    puzzle[0][c].push( color[0][i] + upper_change[i] * c );
		    puzzle[row - 1][c]. push( color[2][i] + lower_change[i] * c );
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

	    }//end for

	    var table = document.createElement("table");
	    table.style.style = "cellpadding: 0; cellspacing: 0; border: 0; border-collapse: collapse;"

	    for (var i = 0; i < row; i++)
	    {
		var tr = document.createElement("tr");

		for (var j = 0; j < column; j++)
		{
		    var td = document.createElement("td");
		    td.style = "padding: 0; margin: 0";

		    var div = document.createElement("div");
		    div.style = "width: 70px; height: 70px; background-color: rgb(" + puzzle[i][j][0] + "," + puzzle[i][j][1]  + "," + puzzle[i][j][2] + "); padding: 10px; box-sizing: border-box; vertical-align: middle; text-align: center; font-size: 40px";

		    td.appendChild( div );
		    tr.appendChild( td );
		}

		table.appendChild( tr );
	    }

	    preview_table.appendChild( table );

	}
    };

    var checked = function(e)
    {
	var ul = document.getElementsByName("tlcolor");
	var ur = document.getElementsByName("trcolor");
	var ll = document.getElementsByName("blcolor");
	var lr = document.getElementsByName("brcolor");

	var checked = true;

	for (var i = 0; i < ul.length; i++)
	{
	    if (ul[i].checked)
	    {
		checked = checked && true;
		color[0] = ul[i];
		break;
	    }
	}

	for (var i = 0; i < ur.length; i++)
	{
	    if (ur[i].checked)
	    {
		checked = checked && true;
		color[1] = ur[i];
		break;
	    }
	}

	for (var i = 0; i < ll.length; i++)
	{
	    if (ll[i].checked)
	    {
		checked = checked && true;
		color[2] = ll[i];
		break;
	    }
	}

	for (var i = 0; i < ll.length; i++)
	{
	    if (lr[i].checked)
	    {
		checked = checked && true;
		color[3] = lr[i];
		break;
	    }
	}

	if (!checked)
	{
	    alert("Please choose a color for each corner.");
	}

	return checked;
    }
}


var reloaded = function(e)
{
    location.reload();
    console.log("reloaded");
}
