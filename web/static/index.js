$(function() {
    $('a#test').bind('click', function() {
        $.getJSON('/run', // << HERE
            function(data) {
                // do nothing
            });
        return false;
    });
});


function validate(name){
    if(name.legnth >= 2){
        return true;
    };
    return false;
};