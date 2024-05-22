from flask import Flask
from dbinit import db, db_reload
from dbconnector import DBConnector

perform_db_reload = False

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoo.db'
db.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return 'Witaj w mojej aplikacji Zoo!'

@app.route('/tables', methods=['GET'])
def tables():
    return db_connector.get_tables()

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test_current():
    return db_connector.get_animals()

if perform_db_reload:
    db_reload(app.app_context())
    print('DB restored to default state')

db_connector = DBConnector(db)
db_connector.get_tables()
app.run(host='127.0.0.1', port=443)
