from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Witaj w mojej aplikacji Flask!'

@app.route('/about')
def about():
    return 'Zaprogramowano przez Emil Kobylecki!'

@app.route('/contact')
def contact():
    return '''
        Email: emil@gmail.com
        Telefon: 123456789
    '''

app.run()
