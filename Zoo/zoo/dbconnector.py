from flask_sqlalchemy import SQLAlchemy
from dbinit import Animals

from dbinit import db


class DBConnector:
    def __init__(self, db):
        self.db = db

    def get_tables(self):
        tables = []
        for table in self.db.metadata.sorted_tables:
            tables.append(str(table))
        return tables

    def get_animals(self):
        print(db.session.query(Animals, id).all)
        return 'in progress'

