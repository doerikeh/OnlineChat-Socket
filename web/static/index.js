$(function() {
    $('#sendBtn').bind('click', function() {
        var msg = document.getElementById("msg")
        var value = msg.value
        msg.value = ""
        $.getJSON('/send_message',
            {val:value},
            function(data) {
                
            });
        });
});

window.onload = function(){
    var updete_loop = this.setInterval(updete_message, 100);
    updete_message()
}



function updete_message(){ 
    fetch('/get_messages')
        .then(function(response){
            return response.json();
        }).then(function(text){
            var messages = "";
            for (value of text['messages']){
                messages = messages + "<br>" + value
            }
            document.getElementById("test").innerHTML = messages
        });
};