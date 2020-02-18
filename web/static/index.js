$(function() {
    $('#sendBtn').bind('click', function() {
        var value = document.getElementById("msg").value
        $.getJSON('/send_message',
            {val:value},
            function(data) {
                
            });
        
    
});


window.addEventListener("load", function(){
    var updete_loop = this.setInterval(updete_message, 100);
    updete_message()
});



function updete_message(){ 
    fetch('/get_messages')
        .then(function(response){
            return response.text();
        }).then(function(text){
            console.log(' GET response text: ');
            document.getElementById("test").innerHTML = text; 
        });
       return false;
    });
};