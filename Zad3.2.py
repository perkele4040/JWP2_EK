from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from imports import Task, add_task_db, get_tasks_db, get_tables_db

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zad3_2.db'
db.init_app(app)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('main.html', tasks=get_tasks_db(db))


@app.route('/back/add-task', methods=['POST'])
def add_task_db():
    return request.get_data()


@app.route('/back/remove-task', methods=['POST'])
def remove_task_db():
    print(int(request.get_data(as_text=True)))
    with app.app_context():
        t = db.session.query(Task).filter_by(id=int(request.get_data(as_text=True)))
        print(t)
        db.session.delete(t)
        db.session.commit()
    return 'task removed'


t1 = Task(name='task1')
t2 = Task(name='task2')
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.query(Task).delete()
    db.session.add_all([t1, t2])
    db.session.commit()
    print(get_tasks_db(db))
app.run(host='127.0.0.1', port=443, debug=True)
