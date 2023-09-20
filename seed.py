from application import db
from application.aot_characters.models import Character

db.drop_all()
print("dropping db")

db.create_all()
print("creating db")

print("seeding db")
e1 = Character(name="Levi Ackermann", age="30", occupation="soldier")
e2 = Character(name="Mikasa Ackermann", age="19", occupation="soldier")
e3 = Character(name="Armin Arlelt", age="19", occupation="soldier")
e4 = Character(name="Hange Zoe", age="unknown", occupation="soldier")
e5 = Character(name="Sasha Braus", age="20", occupation="soldier")


db.session.add_all({e1,e2,e3,e4,e5})

db.session.commit()