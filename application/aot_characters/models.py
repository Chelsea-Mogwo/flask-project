from application import db, app

app.app_context().push()

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    def __init__(self, firstname, lastname, age, occupation):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f"Character(id: {self.id}, firstname: {self.firstname})"
    
    @property
    def json(self):
        separator = " "
        return {"id": self.id, "name": separator.join([self.firstname, self.lastname]), "age": self.age, "occupation": self.occupation}