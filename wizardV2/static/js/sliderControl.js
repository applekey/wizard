$(document).on("change",".fineNumber",function() {
  $(this).closest(".row").find('.rangeSlider').val($(this).val())
});

$(document).on("change",".rangeSlider",function() {
  $(this).closest(".row").find('.fineNumber').val($(this).val()).change()
});


function callAccept() {
    $(event.target).parent().closest('.subControl').find('.subText').filter(':visible').find('button').click()
}

function OffsetValuesAllowNegativeAcceptFunction(id) {
    debugger;
    var softTransitionValue = $(id).parent().find('#Smooth')
    $.post('api/softTransition(' + $(this).val() + ')', function (data) {
        if(apiReturnParser(data) ==false)
        {
            return;
        }

        $.post('api/offsetDistance(' + $(this).val() + ',True)', function (data) {
            if (apiReturnParser(data) == false) {
                return;
            }
            $.post('api/accept()')
        })
    })
    $(id).parent().find('#Distance')
}

var template = "<div class='row' style='margin-left:3px;margin-right:3px;'>\
                        <button style='display: none;' id='hiddenAcceptButton' type='button' onclick={{acceptFunction}}>You should not able to see me</button>\
					  	{{#sliders}}\
						    <h5> {{sectionName}}</h5>\
							<div  class='row' style='margin-left:3px;margin-right:3px;'>\
								<div class='col-xs-9'>\
									<input class='rangeSlider' value={{value}} step = '{{step}}' min='{{min}}' max='{{max}}' type='range'>\
								</div>\
								<div class='col-xs-2' >\
									<input id = {{sectionName}} class='fineNumber' onchange={{onchange}} value={{value}} step = '{{step}}' name='quantity' min='{{min}}' max='{{max}}' type='number'>\
								</div>\
								<div class='col-xs-1'>\
									<p align='left'>mm </p>\
								</div>\
							</div>\
						{{/sliders}} \
					</div>";

	var OffsetValuesAllowNegative = {
 	mainControlName:"Offset",
 	sliders:[{
 		value:4.0,
 		sectionName:"Distance",
 		max: 10,
		min: -10,
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
 	}],
 	acceptFunction: "OffsetValuesAllowNegativeAcceptFunction(this)"
	};


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
     , acceptFunction: "OffsetValuesAllowNegativeAcceptFunction(this)"
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
	, acceptFunction: "OffsetValuesAllowNegativeAcceptFunction(this)"
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
     , acceptFunction: "OffsetValuesAllowNegativeAcceptFunction(this)"
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
     , acceptFunction: "OffsetValuesAllowNegativeAcceptFunction(this)"
	};


 var RemeshValues = {
 	mainControlName:"Remesh",
 	sliders:[{
 		value:0,
 		sectionName:"Remesh",
 		max: 1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/remesh(1,'+$(this).val()+')',apiReturnParser)"
 	},
 	{
 		value:0,
 		sectionName:"Smooth",
 		max: 1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/remesh(2,'+$(this).val()+')',apiReturnParser)"
 	},
 	{
 		value:0,
 		sectionName:"Threshold",
 		max: 1,
		min: 0,
		step:0.05,
		onchange: "$.post('api/remesh(3,'+$(this).val()+')',apiReturnParser)"	
 	}
 	]
     , acceptFunction: "OffsetValuesAllowNegativeAcceptFunction(this)"
	};




