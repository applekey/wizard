$(document).on("change",".fineNumber",function() {
  $(this).parent().children('.rangeSlider').val($(this).val())
});

$(document).on("change",".rangeSlider",function() {
  $(this).parent().children('.fineNumber').val($(this).val()).change()
});


var template = " <div class='row' style='margin-left:3px;'> \
  {{#sliders}}\
 <div class='col-xs-right'>\
         <h5> {{sectionName}}</h5>\
 </div>\
	<div class='col-xs-left'>\
		<input class='fineNumber' onchange={{onchange}}  value={{value}} step = '{{step}}' name='quantity' min='{{min}}' max='{{max}}' type='number'>\
		<input class='rangeSlider' value={{value}} step = '{{step}}' min='{{min}}' max='{{max}}' type='range'>\
	</div>\
{{/sliders}} </div>";

 var tmpValues = {
 	sliders:[{
 		value:0.5,
 		sectionName:"remesh",
 		max: 1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/remesh(1,'+$(this).val()+')',apiReturnParser)"
 	},
 	{
 		value:0.5,
 		sectionName:"smooth",
 		max: 1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/remesh(2,'+$(this).val()+')',apiReturnParser)"
 	},
 	{
 		value:0.5,
 		sectionName:"threshold",
 		max: 1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/remesh(3,'+$(this).val()+')',apiReturnParser)"	
 	}
 	]
	};




