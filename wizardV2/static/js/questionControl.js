var questionTemplate = "	<div class='row' >\
						<div class='col-xs-10'>\
					  		<h3 id='controlHeaderText'> {{mainControlName}}</h3>\
					  	</div>\
					  	<div class='col-xs-2'>\
					  		<span class='glyphicon glyphicon-question-sign' style='horizontal-align:right'></span>\
					  	</div>\
					</div>\
					<hr>";


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