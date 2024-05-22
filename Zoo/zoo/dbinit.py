from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def db_reload(context):
    with context:
        db.drop_all()
        db.create_all()

class Animals(db.Model):
    __tablename__ = "ANIMALS"
    id = db.Column(db.Integer, primary_key=True)
    enclosure = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String(255), nullable=False)


class Enclosures(db.Model):
    __tablename__ = "ENCLOSURES"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    inhabitant = db.Column(db.String(255), nullable=False)


class Employees(db.Model):
    __tablename__ = "EMPLOYEES"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Integer, nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
