$(document).ready(function(){
    var txt = "Congrats! You've completed " + data['total_num_question'] + " questions!"
    $('#msg').text(txt)
    $('#redo').click(function(e){
        e.preventDefault()
        window.location = '/quiz'
    })
})