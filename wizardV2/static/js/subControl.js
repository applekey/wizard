$(".page3Well").hide()

var page3InstructionIndex = 1
var numberOfInstructions = $('.subText').length
$('#backButton').attr("disabled", true);

$('#wellText').append("<div class='progress progress-striped'>\
<div id= 'step3ProgressBar' class='progress-bar' role='progressbar' data-transitiongoal='0'></div>\
</div>")

$('.subControl').append("\
<!-- controls for subinstructions -->\
<div id = 'backFowardCancel' class='btn-group'>\
	<button type='button' id='backButton' class='btn btn-default'><span class='glyphicon glyphicon-chevron-left'></span></button>\
	<button type='button' id='fowardButton' class='btn btn-default'><span class='glyphicon glyphicon-chevron-right'></span></button>\
	<button type='button' id='cancelButton' class='btn btn-default'>Cancel</button>\
</div>\
")
$("#backFowardCancel").hide()

$("#cleanUpBT").click(function(){
	var parent = $( this ).parent( ".subControl" )

   $("#wellText",parent).show()
  // $.post("api/planeCut");
  $(this).hide()
  $("#backFowardCancel",parent).show()
	
});

$("#cancelButton").click(function(){
	reset()
});

$("#fowardButton").click(function(){	
	var txtToHide = 'subText' +page3InstructionIndex
	page3InstructionIndex = page3InstructionIndex+1;
	var txtToShow = 'subText' +page3InstructionIndex

	$("#"+txtToShow).first().show()
	$("#"+txtToHide).first().hide()
	checkControlValid()
	changeProgressBar((page3InstructionIndex-1)/(numberOfInstructions-1))
		
		

});
$("#backButton").click(function(){
	
	var txtToHide = 'subText' +page3InstructionIndex
	page3InstructionIndex = page3InstructionIndex-1;
	var txtToShow = 'subText' +page3InstructionIndex

	$("#"+txtToShow).first().show()
	$("#"+txtToHide).first().hide()
	checkControlValid()
	changeProgressBar((page3InstructionIndex-1)/(numberOfInstructions-1))
	

	
});

function reset()
{
	$("#wellText").first().hide('fast')
	$("#cleanUpBT").first().show('fast')
	$("#backFowardCancel").first().hide('fast')
	$(".subText").first().hide('fast')
	$("#subText1").first().show('fast')
	page3InstructionIndex = 1
	checkControlValid()
	changeProgressBar(0)
}
function changeProgressBar(newPercentage)
{
	
	newPercentage = newPercentage*100
	var $pb = $('.progress .progress-bar');
	$pb.attr('data-transitiongoal', newPercentage).progressbar({display_text: 'center',use_percentage: false,
		amount_format: function(p, t) {return page3InstructionIndex + ' of ' + numberOfInstructions;}});
}

function checkControlValid() {
    var numberOfInstructions = $('.subText').length
    if(page3InstructionIndex==numberOfInstructions)
    {
    	$('#fowardButton').first().attr("disabled", true);
    	$("#cancelButton").first().hide('slow')
    	$('#backButton').first().attr("disabled", true);
    	setTimeout(reset,2000)
    	return
    }
    else
    {
    	$('#fowardButton').first().attr("disabled", false);
    	$("#cancelButton").first().show();
    }

    if(page3InstructionIndex==1)
    {
    	$('#backButton').first().attr("disabled", true);
    }
    else
    {
    	$('#backButton').first().attr("disabled", false);
    }
}