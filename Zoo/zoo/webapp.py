from flask import Flask, render_template
from dbinit import db, db_reload
from dbconnector import DBConnector
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

# THINGS TO DO
# hello page
# JS scripts for actions
# expand pages to for logged in users
# dedicated buttons for editing/removing/adding

perform_db_reload = True
auth = HTTPBasicAuth()
app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoo.db'
db.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/tables', methods=['GET'])
def get_tables():
    return render_template('tables.html', tables=db_connector.get_tables())


@app.route('/animals', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_animals_details():
    return render_template('animals.html', animals=db_connector.get_animals())


@app.route('/enclosures', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_enclosures_details():
    return render_template('enclosures.html', enclosures=db_connector.get_enclosures())


@app.route('/employees', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_employees_details():
    return render_template('employees.html', employees=db_connector.get_employees())


users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
    if db_connector.authenticate(username, password):
        return True


@app.route('/login', methods=['GET'])
@auth.login_required
def get_login_page():
    return render_template('login.html', user=auth.current_user())


if perform_db_reload:
    db_reload(app.app_context())
    print('DB restored to default state')

db_connector = DBConnector(db)
app.run(host='127.0.0.1', port=443)
