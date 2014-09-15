

var page3InstructionIndex = 1
var numberOfInstructions = $('.subText').length



// // add some extra controls
// $('#wellText').append("<div class='progress progress-striped'>\
// <div id= 'step3ProgressBar' class='progress-bar' role='progressbar' data-transitiongoal='0'></div>\
// </div>")

// $('.subControl').append("\
// <!-- controls for subinstructions -->\
// <div id = 'backFowardCancel' class='btn-group'>\
// 	<button type='button' id='backButton' class='btn btn-default'><span class='glyphicon glyphicon-chevron-left'></span></button>\
// 	<button type='button' id='fowardButton' class='btn btn-default'><span class='glyphicon glyphicon-chevron-right'></span></button>\
// 	<button type='button' id='cancelButton' class='btn btn-default'>Cancel</button>\
// </div>\
// ")

$(document).on('click','#activateButton',function(){
	debugger;
	var parent = $( this ).parent( ".subControl" )

   $("#wellText",parent).show()
  // $.post("api/planeCut");
  $(this).hide()
  $("#backFowardCancel",parent).show()
	
});

$(document).on('click',"#cancelButton",function(){
	var parent = $( this ).parents( ".subControl" )
	reset(parent)
});

$(document).on('click',"#fowardButton",function(){	
	var parent = $( this ).parents( ".subControl" )

	var txtToHide = 'subText' +page3InstructionIndex
	page3InstructionIndex = page3InstructionIndex+1;
	var txtToShow = 'subText' +page3InstructionIndex

	$("#"+txtToShow,parent).show()
	$("#"+txtToHide,parent).hide()
	checkControlValid(parent)
	changeProgressBar((page3InstructionIndex-1)/(numberOfInstructions-1),parent)
});
$(document).on('click',"#backButton",function(){
	var parent = $( this ).parents( ".subControl" )
	var txtToHide = 'subText' +page3InstructionIndex
	page3InstructionIndex = page3InstructionIndex-1;
	var txtToShow = 'subText' +page3InstructionIndex

	$("#"+txtToShow,parent).show()
	$("#"+txtToHide,parent).hide()
	checkControlValid(parent)
	changeProgressBar((page3InstructionIndex-1)/(numberOfInstructions-1),parent)
		
});

function reset(parent)
{
	$("#wellText",parent).hide('fast')
	$("#activateButton",parent).show('fast')
	$("#backFowardCancel",parent).hide('fast')
	$(".subText",parent).hide('fast')
	$("#subText1",parent).show('fast')
	page3InstructionIndex = 1
	checkControlValid()
	changeProgressBar(0)
}
function changeProgressBar(newPercentage,parent)
{
	
	newPercentage = newPercentage*100
	var $pb = $('.progress .progress-bar',parent);
	$pb.attr('data-transitiongoal', newPercentage).progressbar({display_text: 'center',use_percentage: false,
		amount_format: function(p, t) {return page3InstructionIndex + ' of ' + numberOfInstructions;}});
}

function checkControlValid(parent) {
    var numberOfInstructions = $('.subText',parent).length
    if(page3InstructionIndex==numberOfInstructions)
    {
    	$('#fowardButton',parent).attr("disabled", true);
    	$("#cancelButton",parent).hide('slow')
    	$('#backButton',parent).attr("disabled", true);
    	//setTimeout(reset,2000,parent)
    	return
    }
    else
    {
    	$('#fowardButton',parent).attr("disabled", false);
    	$("#cancelButton",parent).show();
    }

    if(page3InstructionIndex==1)
    {
    	$('#backButton',parent).attr("disabled", true);
    }
    else
    {
    	$('#backButton',parent).attr("disabled", false);
    }
}