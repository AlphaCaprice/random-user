from app import db


class Person(db.Model):
    id = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    location = db.Column(db.String)
    email = db.Column(db.String)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'gender': self.gender,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'location': self.location,
            'email': self.email,
        }

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_data_base():
    db.create_all()
