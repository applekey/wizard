function step_process(from, to, dir) {
    if (typeof(dir) === 'undefined') dir = 'asc';
    var old_move = '';
    var new_start = '';

    var speed = 500;

    if (dir == 'asc') {
        old_move = '-';
        new_start = '';
    } else if (dir == 'desc') {
        old_move = '';
        new_start = '-';
    }

    $('#block'+from).animate({left: old_move+'100%'}, speed, function() {
        $(this).css({left: '100%', 'background-color':'transparent', 'z-index':'2'}); 
    });
    $('#block'+to).css({'z-index': '3', left:new_start+'100%'}).animate({left: '0%'}, speed, function() {
        $(this).css({'z-index':'2'}); 
    });

    if (Math.abs(from-to) === 1) {
        // Next Step
        if (from < to) $("#step"+from).addClass('complete').removeClass('current');
        else $("#step"+from).removeClass('complete').removeClass('current');
        var width = (parseInt(to) - 1) * 20;
        $(".progress_bar").find('.current_steps').animate({'width': width+'%'}, speed, function() {
            $("#step"+to).removeClass('complete').addClass('current');
        });
    } else {
        // Move to Step
        var steps = Math.abs(from-to);
        var step_speed = speed / steps;
        if (from < to) {
            move_to_step(from, to, 'asc', step_speed);
        } else {
            move_to_step(from, to, 'desc', step_speed);
        }
    }
}
    
function move_to_step(step, end, dir, step_speed) {
    if (dir == 'asc') {
        $("#step"+step).addClass('complete').removeClass('current');
        var width = (parseInt(step+1) - 1) * 20;
        $(".progress_bar").find('.current_steps').animate({'width': width+'%'}, step_speed, function() {
            $("#step"+(step+1)).removeClass('complete').addClass('current');
            if (step+1 < end) move_to_step((step+1), end, dir, step_speed);
        });
    } else {
        $("#step"+step).removeClass('complete').removeClass('current');
        var width = (parseInt(step-1) - 1) * 20;
        $(".progress_bar").find('.current_steps').animate({'width': width+'%'}, step_speed, function() {
            $("#step"+(step-1)).removeClass('complete').addClass('current');
            if (step-1 > end) move_to_step((step-1), end, dir, step_speed);
        });
    }
}

$(document).ready(function() {
    $("body").on("click", ".progress_bar .step.complete", function() {
        var from = $(this).parent().find('.current').data('step');
        var to = $(this).data('step');
        var dir = "desc";
        if (from < to) dir = "asc";

        step_process(from, to, dir);
    });
});