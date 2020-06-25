$(document).ready(function(){
    var song = data['song_info']
    var all_completed = data['all_completed']
    if (all_completed){
        window.location = '/complete'
    }
    var composers = data['composers']
    var eras = data['eras']
    var titles = data['titles']
    $.each(composers, function(i, composer){
        var option = $('<option>').text(composer)
        $('#composer').append(option)
    })
    $.each(eras, function(i, era){
        var option = $('<option>').text(era)
        $('#era').append(option)
    })
    $.each(titles, function(i, title){
        var option = $('<option>').text(title)
        $('#title').append(option)
    })
    $('#number').text(data['progress_str'])
    $('#question').after(song['audio'])
    $('#next').click(function(){
        window.location = '/quiz'
    })

    $('#progressbar').css('width',data['progress']+'%').attr('aria-valuenow',data['progress'])
    
    $('#submit').click(function(e){
        e.preventDefault()
        $('#view_correct').remove()
        $('#wrong_alert').remove()
        var composer = $('#composer').find(":selected").text()
        var era = $('#era').find(":selected").text();
        var title = $('#title').find(":selected").text();
        if (composer == song['composer'] && era == song['era'] && title == song['title']){
            $('#submit').hide()
            $('#submit').after('<div class="alert alert-success" role="alert">Your answer is correct!</div>')
        }else{
            var wrong_alert = '<div class="alert alert-danger" role="alert" id = "wrong_alert">Wrong Answer</div>'
            
            var view_correct = $('<button>').addClass('btn btn-outline-info').attr({type:'submit', id:'view_correct'}).text('View Correct Answer')
            $('#submit').before(wrong_alert).after(view_correct)
            view_correct.click(function(e2){
                e2.preventDefault()
                $('#view_correct').hide()
                $('#wrong_alert').remove()
                $('#submit').hide()
                var correct_answer = 'Correct Answer: '+ song['title'] + '; ' + song['composer'] + '; ' + song['era']
                var answer_alert = $('<div>').addClass('alert alert-success').text(correct_answer)
                $('#submit').after(answer_alert)
            })
        }
    })
})