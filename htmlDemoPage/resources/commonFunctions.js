  $( "#offsetFine" ).val($( "#offsetSlider" ).val());

  $( "#offsetSlider" ).change(function() {
      $( "#offsetFine" ).val($( "#offsetSlider" ).val());
  });

  $( "#offsetFine" ).change(function() {
      $( "#offsetSlider" ).val($( "#offsetFine" ).val());
  });

$(window).load(function()
{
  $( "#videoPlayer" ).width($(window).width())
  $( "#videoPlayer" ).height($(window).height()/2.0)
});

$(window).resize(function() {
  $( "#videoPlayer" ).width($(window).width())
  $( "#videoPlayer" ).height($(window).height()/2.0)
});