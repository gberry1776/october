

$( "div.sudiv" ).hover(function() {
  $("div.move").animate({
    'background-position-x':"0"
  },200,
);
  $("div.move").animate({
    'background-position-x':"280"
  },1,
);
  $("div.move").animate({
    'background-position-x':"280"
  },500,
);
  $("div.move").animate({
    'background-position-x':"239"
  },1,
);
$("div.move").animate({
  'background-position-x':"239"
},500,
);
$("div.move").animate({
  'background-position-x':"198"
},1,
);
$("div.move").animate({
  'background-position-x':"198"
},500,
);
$("div.move").animate({
  'background-position-x':"157"
},1,
);
$("div.move").animate({
  'background-position-x':"157"
},500,
);
$("div.move").animate({
  'background-position-x':"40"
},4000,function() {
    // Animation complete.
  });
});

$( "a" ).hover(function() {
  $(this).animate({
    'background-position-x':"240"
  },1000,
)}, function(){
  $(this).animate({
  'background-position-x':'80'
},1000,
)})

// $("div.drivediv").animate({
//   'background-position-x':'-240'
// },5000,'linear',function() {
//   loop();
// }
// )

$(document).ready(function() {

    function loop() {
        $('div.drivediv').css({  'background-position-x':'0'});
        $('div.drivediv').animate ({
          'background-position-x':'280'
        }, 5000, 'linear', function() {
            loop();
        });
    }
    loop();
 });

 $(document).ready(function() {

     function loop() {
         $('div.magicmove').css({  'background-position-x':'0'});
         $('div.magicmove').animate ({
           'background-position-x':'0'
         },100,
       );
         $('div.magicmove').animate ({
           'background-position-x':'300'
         },1,
       );
       $('div.magicmove').animate ({
         'background-position-x':'300'
       },100,
     );
     $('div.magicmove').animate ({
       'background-position-x':'200'
     },1,
   );
   $('div.magicmove').animate ({
     'background-position-x':'200'
   },100,
 );
 $('div.magicmove').animate ({
   'background-position-x':'100'
 },1,
);
$('div.magicmove').animate ({
 'background-position-x':'100'
},100,

         function() {
             loop();
         });
     }
     loop();
  });

  var cptop=650
  var cpleft=219
  var obj1 = [614,664,555,605]
  var housel= [215,340,0,230]
  var house2= [440,559,0,230]
  var speed=5

  document.addEventListener("keydown", runspeed);

  function runspeed() {
    var i;
    for (i=0; i < speed; i++) {
      myFunction()
    }
  };

  function tostart1() {
    window.location.replace("/adventure")
  };

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
          cptop-=1}}}
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
    if (cpleft>429 && cpleft<459 && cptop>670 && cptop<700 ){
      tostart1();}
  };




  $(document).ready(function() {
      function loop() {
          $('div.warpportal').css({  'background-position-x':'0'});
          $('div.warpportal').animate ({
            'background-position-x':'0'
          }, 500,);
          $('div.warpportal').animate ({
            'background-position-x':'100'
          }, 1,);
          $('div.warpportal').animate ({
            'background-position-x':'100'
          }, 500,
          function() {
              loop();
          });
      }
      loop();
   });
