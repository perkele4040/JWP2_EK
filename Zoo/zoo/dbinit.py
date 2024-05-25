from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def db_reload(context):
    with context:
        db.drop_all()
        db.create_all()
        db.session.add_all([a1, a2, e1, e2, em1, em2])
        db.session.commit()


class Animals(db.Model):
    __tablename__ = "ANIMALS"
    id = db.Column(db.Integer, primary_key=True)
    enclosure = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String(255), nullable=False)


class Enclosures(db.Model):
    __tablename__ = "ENCLOSURES"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    inhabitant = db.Column(db.Integer, nullable=False)


class Employees(db.Model):
    __tablename__ = "EMPLOYEES"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)


a1 = Animals(id=0, enclosure=1, species='Iguana')
a2 = Animals(id=1, enclosure=2, species='Kangaroo')
e1 = Enclosures(id=0, location='here', inhabitant=0)
e2 = Enclosures(id=1, location='there', inhabitant=1)
em1 = Employees(id=0, first_name='Mike', last_name='Wazowski')
em2 = Employees(id=1, first_name='Steve', last_name='Jobs')


