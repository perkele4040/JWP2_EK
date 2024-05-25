from sqlalchemy import create_engine, MetaData
from sqlalchemy import inspect
import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Table,
    Column,
    String,
    Integer,
    Float,
    Boolean,
    select,
    text,
    func
)
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)

def add_student(session, name, age, grade):
    new_student = Student(name=name, age=age, grade=grade)
    session.add(new_student)
    session.commit()
    return new_student.id


def read_student_by_id(session, student_id):
    return session.get(Student, student_id)


def update_student(session, student_id, name=None, age=None, grade=None):
    student = session.get(Student, student_id)
    if student:
        if name:
            student.name = name
        if age:
            student.age = age
        if grade:
            student.grade = grade
        session.commit()
        return True
    return False

def delete_student(session, student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        return True
    return False


engine = create_engine('sqlite:///EK2.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
#print(add_student(session, 'Monika Beskidzka', '33', '8.8'))
#print(read_student_by_id(session, 4).name)
#print(read_student_by_id(session, 7).name)
#update_student(session, 5, name='Natalia Ekneh')
#print(read_student_by_id(session, 5).name)
#delete_student(session, 7)