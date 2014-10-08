$(document).on('click','#activateButton',function(){
	var parent = $( this ).parent( ".subControl" )
	var numberOfInstructions = $('.subText',parent).length
	parent.attr("index",1)
	parent.attr("numberOfInstructions",numberOfInstructions)
   $("#wellText",parent).show()
  // $.post("api/planeCut");
  $(this).hide()
  $("#backFowardCancel",parent).show()
  changeProgressBar(0, parent)
});

$(document).on('click',"#cancelButton",function(){
	var parent = $( this ).parents( ".subControl" )
	reset(parent)
});

$(document).on('click',"#fowardButton",function(){	
	var parent = $( this ).parents( ".subControl" )

	var currentIndex =parseInt(parent.attr("index")) 

	var txtToHide = 'subText' +currentIndex
	currentIndex = currentIndex+1
	parent.attr("index",currentIndex)
	var txtToShow = 'subText' +currentIndex

	var hiddenElement = $("#"+txtToHide,parent)
	var shownElement = $("#"+txtToShow,parent)
	shownElement.show()
	hiddenElement.hide()


	var attr = hiddenElement.attr('apiFunc');
	if (typeof attr !== typeof undefined && attr !== false) {
    	eval(hiddenElement.attr("apiFunc"))
	}
	var attr = shownElement.attr('apiFuncStart');
	if (typeof attr !== typeof undefined && attr !== false) {
    	eval(shownElement.attr("apiFuncStart"))
	}
	
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

var subControlTemplate = "<br>\
                    <br>\
                    <br>\
                    <hr>\
                    <h5> {{mainStep}}</h5>\
                   	<div class='row' >\
                   		<div class='col-xs-8'>\
							<div class='progress progress-striped'>\
								<div id= 'step3ProgressBar' class='progress-bar' role='progressbar' data-transitiongoal='0'></div>\
							</div>\
						</div>\
						<div class='col-xs-4'>\
							<div id = 'backFowardCancel' class='btn-group' style='display: none;'' >\
								<button type='button' id='backButton' class='btn btn-default'><span class='glyphicon glyphicon-chevron-left'></span></button>\
								<button type='button' id='fowardButton' class='btn btn-default'><span class='glyphicon glyphicon-chevron-right'></span></button>\
								<button type='button' id='cancelButton' class='btn btn-default'>Cancel</button>\
							</div>\
						</div>\
					</div>"
var subControlValuesPage2 = {mainStep: "Step 2 Progress"};
var subControlValuesPage3 = {mainStep: "Step 3 Progress"};
var subControlValuesPage4 = {mainStep: "Step 4 Progress"};
var subControlValuesPage5 = {mainStep: "Step 5 Progress"};
var subControlValuesPage61 = {mainStep: "Step 6 part 1 Progress"};
var subControlValuesPage62 = {mainStep: "Step 6 part 2 Progress"};
var subControlValuesPage63 = {mainStep: "Step 6 part 3 Progress"};
var subControlValuesPage7 = {mainStep: "Step 7 Progress"};
