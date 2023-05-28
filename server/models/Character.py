from models.db import db
from models.Enums import trait, gender, role

class Character(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    anime_id = db.Column(db.INTEGER, db.ForeignKey('anime.id'))
    role = db.Column(role)
    gender = db.Column(gender)
    traits = db.Column(db.ARRAY(trait))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'anime_id': self.anime_id,
            'role': self.role,
            'gender': self.gender,
            'traits': self.traits
        }