from flask import Flask, render_template

app = Flask(__name__)

albums = [{
    'artist': 'Madonna',
    'title': 'True Blue',
    'year': '1987'
},

    {
        'artist': 'Britney Spears',
        'title': 'Hit me baby one more time',
        'year': '1998'
    },

    {
        'artist': 'Pink Floyd',
        'title': 'The Wall',
        'year': 'Around 1976'
    }]

genres = ['rock', 'blues', 'pop']


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/albums')
def list_albums():
    return render_template('flaskindex.html', albums=albums, genres=genres)


if __name__ == '__main__':
    app.run()
