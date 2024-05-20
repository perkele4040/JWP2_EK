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

engine = create_engine('sqlite:///EK2.sqlite')

# 1. create table
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)
Base.metadata.create_all(engine)

#2. add students
Session = sessionmaker(bind=engine)
session = Session()
new_students = [Student(name='Katarzyna Krasicka', age=30, grade=8.7), Student(name='Maciej Zawiasa', age=25, grade=7.6), Student(name='Damian Szczepaniak', age=28, grade=9.2)]
for new_student in new_students:
    session.add(new_student)
session.commit()

#3. read and print students
all_students = session.query(Student).all()
for student in all_students:
    print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

session.close()

