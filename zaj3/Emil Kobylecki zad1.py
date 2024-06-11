from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zaj3.db'


@app.route('/teachers', methods=['GET'])
def get_teachers():
    ts = []
    for t in db.session.query(Teacher).all():
        ts.append([t.name, t.subject, t.time])
    return ts


@app.route('/html_test', methods=['GET'])
def html_test():
    return render_template('form1.html')


@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        teacherName = request.form['teacherName']
        teacherSubject = request.form['teacherSubject']
        teacherTime = request.form['teacherTime']
        print(teacherName)
    return render_template('form2.html')

class Teacher(db.Model):
    __tablename__ = "ANIMALS"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    subject = db.Column(db.String(255), nullable=True)
    time = db.Column(db.String(255), nullable=True)


t1 = Teacher(name='teacher1', subject='maths', time='today')
t2 = Teacher(name='teacher2', subject='physics', time='tomorrow')
t3 = Teacher(name='teacher3', subject='biology', time='yesterday')

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all([t1, t2, t3])
    db.session.commit()
app.run(host='127.0.0.1', port=443)
