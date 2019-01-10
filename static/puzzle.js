var sq = document.getElementsByClassName('box');
var clicked = [];
for(var i = 0; i < sq.length;i++){
  sq[i].addEventListener('click',function(){
  clicked.push(this);
  swap()
})
};
var swap = function(e){
  clicked[0].style.border = '5px solid black'
  if(clicked.length == 2){
    console.log(clicked);
    var color = clicked[0].style.backgroundColor;
    clicked[0].style.backgroundColor = clicked[1].style.backgroundColor;
    clicked[1].style.backgroundColor = color;
    clicked[0].style.border = '0px'
    clicked = []
  }
}
