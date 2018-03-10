from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///adaptCntr.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories 
session.query(Category).delete()
# Delete User 
session.query(User).delete()
# Delete Items  
session.query(Items).delete()

# Create users
User1 = User(name="Animal Lover", email="olga.novgorodsky@gmail.com", picture="https://lh3.googleusercontent.com/-VHx5tZibLbs/AAAAAAAAAAI/AAAAAAAABZ4/zoGhcR-krIo/s60-p-no/photo.jpg")
session.add(User1)
session.commit()

# Create some categories
Category1 = Category(name="Dogs",user = User1)
session.add(Category1)
session.commit()

Category2 = Category(name="Cats",user = User1)
session.add(Category2)
session.commit

Category3 = Category(name="Rabbits",user = User1)
session.add(Category3)
session.commit()

Category4 = Category(name="Birds",user = User1)
session.add(Category4)
session.commit()

Category5 = Category(name="Fish",user = User1)
session.add(Category5)
session.commit()

# Populate some category with items 

Item1 = Items(name = "Pete", description = "Adopt Pete", color = "Brown/White", gender = "Male", age="2 years 1 month",date=datetime.datetime.now(),picture="https://media.petango.com/sms/photos/626/994aea0d-36b6-4d16-b48e-4e7d3266f7a4.jpg", category = Category1, user = User1)
session.add(Item1)
session.commit()
Item2 = Items(name = "Bristol", description = "Adopt Bristol", color = "Black/White", gender = "Female", age="5 years",date=datetime.datetime.now(),picture="https://media.petango.com/sms/photos/626/0451b8a2-9664-45f1-bb98-ba760e20b347.jpg", category = Category1, user = User1)
session.add(Item2)
session.commit()
Item3 = Items(name = "Cindy", description = "Adopt Cindy", color = "Gray", gender = "Female", age="9 months",date=datetime.datetime.now(),picture="https://media.petango.com/sms/photos/626/a4ce7cd1-1fbf-4ee9-b7e1-da2bf9950af7.jpg" ,category = Category2, user = User1)
session.add(Item2)
session.commit()
print "Your database has been populated with data!"
