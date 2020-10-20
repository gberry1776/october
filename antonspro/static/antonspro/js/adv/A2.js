var cptop=700
var cpleft=360
var obj1 = [367,417,112,162]
var speed=5
var bwalll=[0,355,740,800]
var bwallr=[419,800,740,800]

document.addEventListener("keydown", runspeed);

function runspeed() {
  var i;
  for (i=0; i < speed; i++) {myFunction()}}

function myFunction(e) {
  e = e || window.event;
  if (e.keyCode == '38'){
    document.getElementById("hero").style.transform="rotate(180deg)";
    if (cptop>70){
      if (cptop===obj1[3] && cpleft>(obj1[0]-50) && cpleft<obj1[1]){}
      else {
        document.getElementById("hero").style.top= (cptop-1).toString()+"px" ;
        cptop-=1}}}
  else if (e.keyCode == '37'){
    document.getElementById("hero").style.transform="rotate(90deg)";
    if (cpleft>10){
      if (cpleft===obj1[1] && cptop>(obj1[2]-50) && cptop<obj1[3]){}
      else {
        document.getElementById("hero").style.left= (cpleft-1).toString()+"px" ;
        cpleft-=1}}}
  else if (e.keyCode == '39'){
    document.getElementById("hero").style.transform="rotate(270deg)"
    if (cpleft<750){
      if (cpleft===(obj1[0]-50) && cptop>(obj1[2]-50) && cptop<obj1[3]){}
      else {
        document.getElementById("hero").style.left= (cpleft+1).toString()+"px" ;
        cpleft+=1}}}
  else if (e.keyCode == '40'){
    document.getElementById("hero").style.transform="rotate(0deg)"
    if (cptop<750){
      if (cptop===(obj1[2]-50) && cpleft>(obj1[0]-50) && cpleft<obj1[1]||
          cptop===(bwalll[2]-50) && cpleft>(bwalll[0]-50) && cpleft<bwalll[1]||
          cptop===(bwallr[2]-50) && cpleft>(bwallr[0]-50) && cpleft<bwallr[1]){}
      else {
        document.getElementById("hero").style.top= (cptop+1).toString()+"px" ;
        cptop+=1}}
    if (cptop>715 && 415>cpleft && cpleft>355){
        tostart1()}}
}



document.addEventListener("keydown", cloak);
function cloak(e) {
  e = e || window.event;
  if (e.keyCode == '32'){
    document.getElementById("hero").style.backgroundColor= "red" ;}}
document.addEventListener("keyup", uncloak);
function uncloak(e) {
  e = e || window.event;
  if (e.keyCode == '32'){
    document.getElementById("hero").style.backgroundColor= "purple" ;}}


function tostart1() {
  window.location.replace("/adventure")
}

document.addEventListener("keydown", removetext);
function removetext(e) {
  e = e || window.event;
  if (e.keyCode == '13'){
    document.getElementById('text').parentNode.removeChild(document.getElementById('text'));}}
