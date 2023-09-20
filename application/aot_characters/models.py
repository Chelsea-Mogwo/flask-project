from application import db, app

app.app_context().push()

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f"Character(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {"id": self.id, "name": self.name, "age": self.age, "occupation": self.occupation}