from sqlalchemy import (
    create_engine, Column, Integer, String
)
# from sqlalchemy.ext.declarative import declarative_base <= This is deprecated; now available from sqlalchemy.orm, below
from sqlalchemy.orm import sessionmaker, declarative_base


# executing the instructions from the chinook database#
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the Programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

adam_turing = Programmer(
    first_name="Adam",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

gabe_eboreime = Programmer(
    first_name="Gabe",
    last_name="Eboreime",
    gender="M",
    nationality="Black British",
    famous_for="Nothing yet"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(adam_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(gabe_e)

# commit our session to the database
# session.commit()


# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.last_name = "Eboreime"

#... and commit session
# session.commit()


#updating multiple records
people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted.")
# else:
#     print("No records found.")


# delete all entries
# all_entries = session.query(Programmer)
# wipe_check = input("This will delete EVERYTHING. Are you SURE you want to do this? (y/n) ")
# if wipe_check.lower() == "y":
#     for entry in all_entries:
#         session.delete(entry)
#     print("The database has been wiped.")
# else:
#     print("Alright, good. Here's the table you asked for.")

# query database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
