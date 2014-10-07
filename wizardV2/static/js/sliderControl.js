$(document).on("change",".fineNumber",function() {
  $(this).closest(".row").find('.rangeSlider').val($(this).val())
});

$(document).on("change",".rangeSlider",function() {
  $(this).closest(".row").find('.fineNumber').val($(this).val()).change()
});


var template = "<div class='row' style='margin-left:3px;margin-right:3px;'>\
					<div class='row' >\
						<div class='col-xs-10'>\
					  		<h3 id='controlHeaderText'> {{mainControlName}}</h3>\
					  	</div>\
					  	<div class='col-xs-2'>\
					  		<span class='glyphicon glyphicon-question-sign' style='horizontal-align:right'></span>\
					  	</div>\
					</div>\
					<hr>\
					  	{{#sliders}}\
						    <h5> {{sectionName}}</h5>\
							<div class='row' style='margin-left:3px;margin-right:3px;'>\
								<div class='col-xs-10'>\
									<input class='rangeSlider' value={{value}} step = '{{step}}' min='{{min}}' max='{{max}}' type='range'>\
								</div>\
								<div class='col-xs-1'>\
									<input class='fineNumber' onchange={{onchange}}  value={{value}} step = '{{step}}' name='quantity' min='{{min}}' max='{{max}}' type='number'>\
								</div>\
								<div class='col-xs-1'>\
									mm\
								</div>\
							</div>\
						{{/sliders}} \
					</div>";

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
 		value:31,
 		sectionName:"Soft Transition",
 		max: 50,
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
		value:31,
		sectionName:"Soft Transition",
		max: 50,
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




