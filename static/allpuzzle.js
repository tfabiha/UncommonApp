// <!--
// # UncommonApp
// # Dennis Chen, T Fabiha, Addison Huang, Michelle Tang
// # P#02: The End
// -->
//This is the preview code. It goes along with customize so users know what their puzzles look
//   before they save it.

var color = [[], [], [], []];

window.onload = function()
{
    var preview_table = document.getElementsByClassName("preview-tiles");
    var preview = function(e)
    {
	preview_table.innerHTML = "";
	for (var puz = 0; puz < preview_table.length; puz++) {
	    var puzzle = [];
	    var row = parseInt(preview_table[puz].id.substring(0));
	    var column = parseInt(preview_table[puz].id.substring(2));
	    var tem = preview_table[puz].id;
	    for (var i = 0; i < color.length; i++)
	    {
		var colo=tem.substring(tem.indexOf("[")+1,tem.indexOf("]"));
		colo=colo.split(',');
		tem=tem.substring(tem.indexOf("]")+1,tem.length);
		color[i] = colo;
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
	    table.style.style = "cellpadding: 0; cellspacing: 0; border: 0; border-collapse: collapse; display:inline; float:left;"

	    for (var i = 0; i < row; i++)
	    {
		var tr = document.createElement("tr");

		for (var j = 0; j < column; j++)
		{
		    var td = document.createElement("td");
		    td.style = "padding: 0; margin: 0";

		    var div = document.createElement("div");
		    div.style = "width: 40px; height: 40px; background-color: rgb(" + puzzle[i][j][0] + "," + puzzle[i][j][1]  + "," + puzzle[i][j][2] + "); padding: 10px; box-sizing: border-box; vertical-align: middle; text-align: center; font-size: 40px;";

		    td.appendChild( div );
		    tr.appendChild( td );
		}

		table.appendChild( tr );
	    }

	    preview_table[puz].appendChild( table );
	    var br = document.createElement("br");
	    var play = document.createElement("button");
	    play.setAttribute("type","submit");
	    play.setAttribute("form","form");
	    play.setAttribute("value",preview_table[puz].id);
	    play.setAttribute("name","value");
	    play.innerHTML = "play";
	    play.setAttribute("class","btn btn-secondary");
	    preview_table[puz].appendChild(play);
	    preview_table[puz].appendChild(br);
	}
    };
    preview();
}
