$(document).on("change",".fineNumber",function() {
  $(this).parent().children('.rangeSlider').val($(this).val())
});

$(document).on("change",".rangeSlider",function() {
  $(this).parent().children('.fineNumber').val($(this).val()).change()
});


var template = "<div class='row' style='margin-left:3px;'>\
 <h3 id='controlHeaderText'> {{mainControlName}}</h3>\
  {{#sliders}}\
 <div class='col-xs-right'>\
         <h5> {{sectionName}}</h5>\
 </div>\
	<div class='col-xs-left'>\
		<input class='fineNumber' onchange={{onchange}}  value={{value}} step = '{{step}}' name='quantity' min='{{min}}' max='{{max}}' type='number'>\
		<input class='rangeSlider' value={{value}} step = '{{step}}' min='{{min}}' max='{{max}}' type='range'>\
	</div>\
{{/sliders}} </div>";

 var OffsetValues = {
 	mainControlName:"Offset",
 	sliders:[{
 		value:4.0,
 		sectionName:"Distance",
 		max: 10,
		min: 0,
		step:0.05,
		onchange: "$.post('api/offsetDistance('+$(this).val()+',True)',apiReturnParser)"
 	},
 	{
 		value:1.24,
 		sectionName:"Soft Transition",
 		max: 1.9,
		min: 0,
		step:0.05,
		onchange: "$.post('api/softTransition('+$(this).val()+')',apiReturnParser)"
 	}]
	};

 var OffsetValues2 = {
	mainControlName:"Offset",
	sliders:[{
		value:4.0,
		sectionName:"Distance",
		max: 10,
	min: 0,
	step:0.05,
	onchange: "$.post('api/offsetDistance('+$(this).val()+',False)',apiReturnParser)"
	},
	{
		value:1.24,
		sectionName:"Soft Transition",
		max: 1.9,
	min: 0,
	step:0.05,
	onchange: "$.post('api/softTransition('+$(this).val()+')',apiReturnParser)"
	}]
};


 var SmoothValues = {
 	mainControlName:"Smooth",
 	sliders:[{
 		value:0.5,
 		sectionName:"Select Size",
 		max: 1.0,
		min: 0,
		step:0.05,
		onchange: "$.post('api/deformSmooth('+$(this).val()+')',apiReturnParser)"
 	}]
	};

 var SelectValues = {
 	mainControlName:"Select Size",
 	sliders:[{
 		value:7,
 		sectionName:"Select Size",
 		max: 13.1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/selectTool('+$(this).val()+')',apiReturnParser)"
 	}]
	};


 var RemeshValues = {
 	mainControlName:"Remesh",
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




