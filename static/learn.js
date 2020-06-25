

$(document).ready(function(){
    var titles = data['titles']
    $.each(titles, function(i, title){
        var link = '/view/'+ Number(i+1)
        var song = $('<a>').addClass('list-group-item list-group-item-action').text(title).attr('href',link)
        
        $('#title_list').append(song)
    })

})