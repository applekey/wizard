$('.questionMarkPlaceHolder').each(function( ) {
  $(this).append("<span  class='glyphicon glyphicon-question-sign' style='horizontal-align:right'></span>")
});

$(document).on("click",".questionMarkPlaceHolder",function() {
	var width = screen.width
	var height = screen.height
	var args = "width=" + width / 5 + ", height=" + height * 0.5 + "top=0,left=0"
	window.open('www.reddit.com', "", args);
});