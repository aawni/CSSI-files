$(document).ready(function(){

$("h1").mouseover(function(){
  $("h1").slideUp(1000).slideDown(1000);
});

$("p").click(function(){
  $("p").fadeOut().fadeIn();
});

$("img").click(function(){
  $("img").slideUp(1000, function() {
    $("img").slideDown(1000)
  });
});
});
