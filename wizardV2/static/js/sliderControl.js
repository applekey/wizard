$(document).on("change",".fineNumber",function() {
  $(this).parent().children('.rangeSlider').val($(this).val())
});

$(document).on("change",".rangeSlider",function() {
  $(this).parent().children('.fineNumber').val($(this).val()).change()
});



 var template = "<div class='inputContainer'>\
<input class='fineNumber' step = '{{step}}' name='quantity' min='{{min}}' max='{{max}}' type='number'>\
<input class='rangeSlider' step = '{{step}}' min='{{min}}' max='{{max}}' type='range'></div>";

 var tmpValues = {
	max: 10,
	min: 0,
	step:0.1
	};

	// var html = Mustache.to_html(template, person);
 //      $('#sampleArea').html(html);



