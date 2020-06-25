$(document).ready(function(){
    var song = data['song_info']
    $('#title').text(song['title']).append(song['video'])
    $('#composer').text(song['composer'])
    $('#year').text(song['year'])
    $('#era').text(song['era'])
    $('#background').text(song['background'])
    
    var total = Number(data['total'])
    if (Number(song['id'])==1){
        $('#prev').addClass('disabled')
    }else{
        var link = '/view/'+ Number(Number(song['id'])-1)
        $('#prev_link').attr('href',link)
    }

    if (Number(song['id'])==total){
        $('#next').addClass('disabled')
    }else{
        var link = '/view/'+ Number(Number(song['id'])+1)
        $('#next_link').attr('href',link)
    }

    for (let page = total; page >0; page--) {
        var li = $('<li>').addClass('page-item')
        var link = '/view/'+ page
        if (page == Number(song['id'])){
            li.addClass('active')
        }
        var a = $('<a>').addClass('page-link').attr('href',link).text(page)
        li.append(a)
        $('#prev').after(li)
        
      }
})