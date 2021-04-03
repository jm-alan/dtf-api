from app.models import db, User
from faker.providers.person.en import Provider
from random import shuffle, seed

first_names = list(set(Provider.first_names))

seed(4321)
shuffle(first_names)

# Adds a demo user, you can add other users here if you want
def seed_users():

  users = []

  demo = User(
    first_name='Demo',
    email='demo@aa.io',
    password='password',
    max_pins=25,
  )

  users.append(demo)

  for i in range(99):
    users.append(User(
      first_name=first_names[i],
      password='password',
      email=f'{first_names[i]}@fakeuser.com',
      max_pins=25
    ))

  db.session.add(users)

  db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()
