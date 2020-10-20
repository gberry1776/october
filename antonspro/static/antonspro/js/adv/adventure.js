
var cptop=700
var cpleft=350
var obj1 = [614,664,555,605]
var pausetog=0
var housel= [215,340,0,230]
var house2= [440,559,0,230]
var speed=5

document.addEventListener("keydown", runspeed);

function runspeed() {
  var i;
  for (i=0; i < speed; i++) {
    myFunction()
  }
}


function myFunction(e) {
  e = e || window.event;
  if (e.keyCode == '38'){
    document.getElementById("hero").style.transform="rotate(180deg)";
    if (cptop>11){
      if ((cptop===obj1[3] && cpleft>(obj1[0]-50) && cpleft<obj1[1])||
         (cptop===housel[3] && cpleft>(housel[0]-50) && cpleft<housel[1])||
         (cptop===house2[3] && cpleft>(house2[0]-50) && cpleft<house2[1])){}
      else {
        document.getElementById("hero").style.top= (cptop-1).toString()+"px" ;
        cptop-=1}}
    if (cptop<200 && 412>cpleft && cpleft>335){
      toA2()}}
  else if (e.keyCode == '37'){
    document.getElementById("hero").style.transform="rotate(90deg)";
    if (cpleft>10){
      if ((cpleft===obj1[1] && cptop>(obj1[2]-50) && cptop<obj1[3])||
          (cpleft===house2[1] && cptop>(house2[2]-50) && cptop<house2[3])){}
      else {
        document.getElementById("hero").style.left= (cpleft-1).toString()+"px" ;
        cpleft-=1}}}
  else if (e.keyCode == '39'){
    document.getElementById("hero").style.transform="rotate(270deg)"
    if (cpleft<750){
      if ((cpleft===(obj1[0]-50) && cptop>(obj1[2]-50) && cptop<obj1[3])||
          (cpleft===(housel[0]-50) && cptop>(housel[2]-50) && cptop<housel[3])){}
      else {
        document.getElementById("hero").style.left= (cpleft+1).toString()+"px" ;
        cpleft+=1}}}
  else if (e.keyCode == '40'){
    document.getElementById("hero").style.transform="rotate(0deg)"
    if (cptop<750){
      if (cptop===(obj1[2]-50) && cpleft>(obj1[0]-50) && cpleft<obj1[1]){}
      else {
        document.getElementById("hero").style.top= (cptop+1).toString()+"px" ;
        cptop+=1}}}
}

document.addEventListener("keydown", cloak);
function cloak(e) {
  e = e || window.event;
  if (e.keyCode == '32'){
    if (pausetog===0){
    clearInterval(enemyMove);
    pausetog+=1}
    else {pausetog-=1
    window.setInterval(aniEnemy, 500)}
    }}

// document.addEventListener("keyup", uncloak);
// function uncloak(e) {
//   e = e || window.event;
//   if (e.keyCode == '32'){
//     document.getElementById("hero").style.backgroundColor= "purple" ;}}


function toA2() {
  window.location.replace("A2/")
}



// function loop() {
//     $('div.enemy1').css({  'left':'100'});
//     $('div.enemy1').animate ({'left':'280'}, 5000, 'linear',);
//   $('div.enemy1').animate ({'left':'100'}, 5000, 'linear',function() {loop()});
// }
// loop()
//
var eleft=220
var etop=250
var enemyMove=window.setInterval(aniEnemy, 50);

var LR = 1
function aniEnemy() {
  if (LR===1){
    document.getElementById("enemy1").style.transform="rotate(0deg)"
    if (eleft <=440){
      document.getElementById("enemy1").style.left= (eleft+1).toString()+"px" ;
      eleft+=1}
    else{LR=0}}
  else{
    document.getElementById("enemy1").style.transform="rotate(180deg)"
    if (eleft >=220){
      document.getElementById("enemy1").style.left= (eleft-1).toString()+"px" ;
      eleft-=1}
    else{LR=1}}
  if (cpleft>eleft && cpleft<(eleft+50) && ((cptop>etop && cptop<(etop+50))||((cptop+50)>etop && (cptop+50)<(etop+50)))){
    document.getElementById('hero').parentNode.removeChild(document.getElementById('hero'));}
  if ((cpleft+50)>eleft && (cpleft+50)<(eleft+50) && ((cptop>etop && cptop<(etop+50))||((cptop+50)>etop && (cptop+50)<(etop+50)))){
    document.getElementById('hero').parentNode.removeChild(document.getElementById('hero'));}
;}
