$(document).on('click','#activateButton',function(){
	debugger;
	var parent = $( this ).parent( ".subControl" )
	var numberOfInstructions = $('.subText',parent).length
	parent.attr("index",1)
	parent.attr("numberOfInstructions",numberOfInstructions)
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
	debugger;
	var parent = $( this ).parents( ".subControl" )

	var currentIndex =parseInt(parent.attr("index")) 

	var txtToHide = 'subText' +currentIndex
	currentIndex = currentIndex+1
	parent.attr("index",currentIndex)
	var txtToShow = 'subText' +currentIndex

	$("#"+txtToShow,parent).show()
	$("#"+txtToHide,parent).hide()
	checkControlValid(parent)
	changeProgressBar((currentIndex-1)/(parent.attr("numberOfInstructions")-1),parent)
});

$(document).on('click',"#backButton",function(){
	var parent = $( this ).parents( ".subControl" )

	var currentIndex =parseInt(parent.attr("index")) 

	var txtToHide = 'subText' +currentIndex
	currentIndex = currentIndex-1
	parent.attr("index",currentIndex)
	var txtToShow = 'subText' +currentIndex

	$("#"+txtToShow,parent).show()
	$("#"+txtToHide,parent).hide()
	checkControlValid(parent)
	changeProgressBar((currentIndex-1)/(parent.attr("numberOfInstructions")-1),parent)
		
});

function reset(parent)
{
	$("#wellText",parent).hide('fast')
	$("#activateButton",parent).show('fast')
	$("#backFowardCancel",parent).hide('fast')
	$(".subText",parent).hide('fast')
	$("#subText1",parent).show('fast')
	parent.attr("index",1)
	checkControlValid(parent)
	changeProgressBar(0,parent)
}
function changeProgressBar(newPercentage,parent)
{
	
	newPercentage = newPercentage*100
	var $pb = $('.progress .progress-bar',parent);
	$pb.attr('data-transitiongoal', newPercentage).progressbar({display_text: 'center',use_percentage: false,
		amount_format: function(p, t) {return parent.attr("index") + ' of ' + parent.attr("numberOfInstructions");}});
}

function checkControlValid(parent) {
    var numberOfInstructions = parseInt(parent.attr("numberOfInstructions"))
    var currentIndex = parseInt(parent.attr("index")) 
    if(currentIndex==numberOfInstructions)
    {
    	$('#fowardButton',parent).attr("disabled", true);
    	$("#cancelButton",parent).hide('slow')
    	$('#backButton',parent).attr("disabled", true);
    	setTimeout(reset,2000,parent)
    	return
    }
    else
    {
    	$('#fowardButton',parent).attr("disabled", false);
    	$("#cancelButton",parent).show();
    }

    if(currentIndex==1)
    {
    	$('#backButton',parent).attr("disabled", true);
    }
    else
    {
    	$('#backButton',parent).attr("disabled", false);
    }
}