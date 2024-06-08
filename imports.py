from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "TASKS"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

def get_tables_db(db):
    tables = []
    for table in db.metadata.sorted_tables:
        tables.append(str(table))
    return tables

def get_tasks_db(db):
    tasks = []
    for t in db.session.query(Task).all():
        tasks.append([t.id, t.name])
    return tasks

def add_task_db(db, name):
    db.add(Task(name='task1'))
    db.commit()