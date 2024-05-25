from dbinit import Animals, Employees, Enclosures


class DBConnector:
    def __init__(self, db):
        self.db = db

    def get_tables(self):
        tables = []
        for table in self.db.metadata.sorted_tables:
            tables.append(str(table))
        return tables

    def get_animals(self):
        animals = []
        for animal in self.db.session.query(Animals).all():
            animals.append([animal.species, animal.enclosure])
        return animals


