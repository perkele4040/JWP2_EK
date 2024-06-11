from dbinit import Animals, Employees, Enclosures, Users
from werkzeug.security import check_password_hash


class DBConnector:
    def __init__(self, db):
        self.db = db

    def get_tables(self):
        tables = []
        for table in self.db.metadata.sorted_tables:
            tables.append(str(table))
        return tables

    def get_animals(self):
        return self.db.session.query(Animals).all()

    def get_enclosures(self):
        return self.db.session.query(Enclosures).all()

    def get_employees(self):
        return self.db.session.query(Employees).all()

    def authenticate(self, username, password):
        users = self.get_users()
        for u in users:
            if username == u.email and check_password_hash(u.password, password):
                return True
        return False

    def get_users(self):
        return self.db.session.query(Users).all()
