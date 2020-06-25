from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from random import randint 
import copy
app = Flask(__name__)


current_id = 7

music = [
    {'id': 1,
    'title': 'Ave Maria',
    'composer':'Josquin',
    'characteristics':['motet','imitative polyphony', 'Latin'],
    'year': 1485,
    'era':'Renaissance',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/qXMZoKofu7g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/Josquin des Prez, Ave Maria (virgo serena, motet).mp3" type="audio/mpeg"></audio>',
    'background':"A version of Josquin Desprez's Ave Maria, perhaps his most famous composition \
    and certainly his most often sung today, appears at the head of the first volume of motets ever \
    printed (1502); its composition occurred during the composer's service at one of several French \
    and North Italian courts. Apparently written some time between 1476 and 1497; this motet expounds \
    with classic elegance the stylistic ideals of the Italian Renaissance and provides one of the best \
    examples of its style, power, and beauty. The structure of Josquin's musical setting corresponds to \
    the text in a lucid way. Twentieth century theorists use the term syntactic imitation to describe \
    the characteristic musical structure of High Renaissance vocal pieces. Each musical phrase corresponds \
    to a phrase of text, and points of imitation frequently expose these phrases. Moments of structural \
    articulation arrive at cadences, where two or more voices rest on perfect intervals"
    },
    {'id': 2,
    'title': 'Brandenburg Concerto no. 5 - first movement',
    'composer':'Bach',
    'characteristics':['ritornello','polyphony', 'concerto grosso'],
    'year': 1715,
    'era':'Baroque',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/EGoDBkIyMC8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/Brandenburg Concerto No. 5 in D BWV1050 I. Allegro.mp3" type="audio/mpeg"></audio>',
    'background':
    "The organ was Bach's favorite instrument, and in his day, he was known more as a \
performer and improviser on it than as a composer-his fame as a composer came, \
ironically, years after his death. This piece is written for four voices, which we will refer to as \
soprano, alto, tenor, and bass, and it begins with the subject appearing first in the \
soprano"
    },
    {'id': 3,
    'title': 'Marriage of Figaro - Se vuol ballare',
    'composer':'Mozart',
    'characteristics':['opera aria','minuet'],
    'year': 1786,
    'era':'Classical',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/Z7NxN85AvHQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/Le nozze di Figaro Se vuol ballare, signor Contino.mp3" type="audio/mpeg"></audio>',
    'background':
    "Social tension is immediately apparent at the beginning of the opera. The main \
character is Figaro, a clever, mostly honest barber and valet, who outwits \
his lord, the philandering, mostly dishonest Count Almaviva. We first meet Figaro \
as he discovers that he and his betrothed, Susanna, have been assigned a bedroom \
next to the Count’s. The Count wishes to exercise his ancient droit du seigneur-a \
supposed law allowing the lord of the manor to claim sexual favors from a servant’s \
fiancée. Figaro responds with a short aria 'Se vuol ballare' (If you want to dance'). \
Here he calls the Count by the diminutive 'Contino,' translated roughly as 'Count, \
you little twerp,' and vows to outsmart his master."
    },
    {'id': 4,
    'title': "La Boheme - Musetta's Waltz",
    'composer':'Puccini',
    'characteristics':['opera aria'],
    'year': 1896,
    'era':'Romantic',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/6spsEkftJ7M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/Puccini - Musetta Waltz from La Bohème (Anna Netrebko, Yuri Temirkanov).mp3" type="audio/mpeg"></audio>',
    'background':
    "Puccini's best-known opera—indeed, the most famous of all \
verismo operas—is La bohème (Bohemian Life). The realism of La bohème \
rests in the setting and characters: The principals are bohemians—unconventional \
artists living in abject poverty. The hero, Rodolfo (a poet), and his pals \
Schaunard (a musician), Colline (a philosopher), and Marcello (a painter), inhabit \
an unheated attic on the Left Bank of Paris. The heroine, Mimi, their neighbor, \
is a poor, tubercular seamstress. Rodolfo and Mimi meet and fall in love. \
He grows obsessively jealous while she becomes progressively more ill. They \
separate for a time, only to return to each other’s arms immediately before Mimi's \
death."
    },
    {'id': 5,
    'title': 'Pierrot lunaire - Nacht',
    'composer':'Schonberg',
    'characteristics':['atonal','German','sprechstimme'],
    'year': 1912,
    'era':'Expressionism',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/J4v3dPG-hec" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/Arnold Schönberg Pierrot Lunaire - 8. Nacht.mp3" type="audio/mpeg"></audio>',
    'background':
    "Here we meet Pierrot, a sad clown from the world of traditional Italian pantomime \
    and puppet shows. Yet in this Expressionist poetry, the clown has fallen under the sway of the moon\
and changed into an alienated modern artist. Pierrot projects his inner anxiety\
by means of Sprechstimme (speech-voice), a vocal technique that requires the\
vocalist to declaim the text more than to sing it. The voice is to execute the rhythmic values \
exactly; but once it hits a pitch, it is to quit the tone immediately, sliding away in \
either a downward or an upward direction. This creates exaggerated declamation \
of the sort one might hear from a lunatic, which is appropriate for Pierrot, given \
the lunar spell cast upon him."
    },
    {'id': 6,
    'title': 'Afro American Symphony - first movement',
    'composer':'Still',
    'characteristics':['European classics mixed with Jazz'],
    'year': 1930,
    'era':'Jazz',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/2OXmKehGDmE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/William Grant Still Afro-American Symphony - I. Moderato Assai.mp3" type="audio/mpeg"></audio>',
    'background':
    "It is the first symphony written by an African American and performed for a \
    United States audience by a leading orchestra. It combines a fairly traditional \
    symphonic form with blues progressions and rhythms that were characteristic \
    of popular African-American music at the time. This combination expressed Still's \
    integration of black culture into the classical forms. Still used a traditional tonal \
    idiom in the Afro-American Symphony, infused with blues-inspired melodic lines and harmonic colorings."
    },
    {'id': 7,
    'title': 'Tehillim',
    'composer':'Reich',
    'characteristics':['imitative polyphony'],
    'year': 1981,
    'era':'Post-modernism',
    'video':'<iframe width="560" height="315" src="https://www.youtube.com/embed/fYn0Wexoa4k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    'audio':'<audio controls><source src="static/Tehillim Illuminated - Synergy Vocals with AskoSchönberg conducted by Clark Rundell.mp3" type="audio/mpeg"></audio>',
    'background':
    "Typically, Reich's music is characterised by a steady pulse and the repetition of \
    a comparatively small amount of melodic material emanating from a clear tonal centre \
    (a style of writing which is called 'minimalist'). Both aspects are certainly to be \
    identified in Tehillim (the composition in no way marks a complete aesthetic break for \
    Reich), for example in the quick, unchanging tempo of the first two parts, which are \
    played one after another without a break, and the close four-part canons of the \
    first and fourth parts. However, these aspects together constitute only the broad \
    outlines of the work; how they are presented is markedly different from his early work."
    },
    ]

eras = []
composers = []
titles = []
for song in music:
    eras.append(song['era'])
    composers.append(song['composer'])
    titles.append(song['title'])
titles_unsorted = copy.deepcopy(titles)
titles.sort()
eras.sort()
composers.sort()
completed_quiz = []

@app.route('/')
def home():
    return render_template('home.html')    


@app.route('/learn')
def learn():
    data = {'titles':titles_unsorted }
    return render_template('learn.html', data = data) 

@app.route('/view/<id>')
def view(id=None):
    data = {'total':current_id}
    for song in music:
        if int(song['id']) == int(id):
            data['song_info'] = song
            return render_template('view.html', data=data)   
    return render_template('view.html', data=data)   

@app.route('/quiz')
def quiz():
    data = {'titles':titles, 'composers':composers, 'eras':eras}
    r = randint(1, current_id)
    while r in completed_quiz and len(completed_quiz) != current_id:
        r = randint(1,current_id)
    completed_quiz.append(r)
    data['progress'] = 100*len(completed_quiz)/current_id
    data['progress_str'] = f'{len(completed_quiz)}/{current_id}'
    for song in music:
        if int(song['id']) == int(r):
            data['song_info'] = song
            data['all_completed'] = False
            if len(completed_quiz) == current_id +1 :
                data['all_completed'] = True
            return render_template('quiz.html', data=data)   
    return render_template('quiz.html', data=data)   

@app.route('/complete')
def complete():
    completed_quiz.clear() 
    data = {'total_num_question': current_id} 
    return render_template('complete.html', data=data)   
    

if __name__ == '__main__':
   app.run(debug = True)




