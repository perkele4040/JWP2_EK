from sqlalchemy import create_engine, inspect, text, select, func, MetaData, Table
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
inspector = inspect(engine)
#table_names = inspector.get_table_names()
#print(table_names)

print(connection.execute(text('Select * from census')))
metadata = MetaData()
state_fact_t = Table('state_fact', metadata, autoload_with=engine)
census_t = Table('census', metadata, autoload_with=engine)

#get all states from table
states = connection.execute(text("SELECT DISTINCT state FROM census")).all()

#display state names
for state in states:
    print(state)

#load population from all Alaska records
population = connection.execute(text("SELECT pop2000, pop2008 FROM census where state = 'Alaska'")).all()

# Separate the values from each tuple
pop2000_values = [tup[0] for tup in population]
pop2008_values = [tup[1] for tup in population]

# Calculate the sums
pop2000 = sum(pop2000_values)
pop2008 = sum(pop2008_values)

print("Alaska population in\n2000: ", pop2000, "\n2008: ", pop2008)

#same method for New York
population = connection.execute(text("SELECT pop2000, pop2008, sex FROM census where state = 'New York'")).all()

pop2000_values = [tup[0] for tup in population]
pop2008_values = [tup[1] for tup in population]


pop2000 = sum(pop2000_values)
pop2008 = sum(pop2008_values)

print("New York population in\n2000: ", pop2000, "\n2008: ", pop2008)

#calculate number of men
population = connection.execute(text("SELECT pop2008 FROM census where state = 'New York' AND sex = 'M'")).all()
pop2008_values = [tup[0] for tup in population]
pop2008 = sum(pop2008_values)
print("New York population in 2008\nMen:\n", pop2008, "\nWomen: ")

#calculate number of women
population = connection.execute(text("SELECT pop2008 FROM census where state = 'New York' AND sex = 'F'")).all()
pop2008_values = [tup[0] for tup in population]
pop2008 = sum(pop2008_values)
print(pop2008)

columns = inspector.get_columns('census')
print(f"Columns for table state_fact:")
for column in columns:
    print(f"  - {column['name']}")