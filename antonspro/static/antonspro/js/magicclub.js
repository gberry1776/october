$(document).ready(function() {
  $("div.front").animate({
    'opacity':"0.9"
  },5000,function() {
    $("div.back").animate({
      'opacity':"0.9"
    },10000,)
  });
});
