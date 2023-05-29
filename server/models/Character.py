from models.db import db

class Character(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    anime_id = db.Column(db.INTEGER, db.ForeignKey('anime.id'))
    gender = db.Column(db.VARCHAR(20))
    characteristics = db.Column(db.VARCHAR(255))
    age = db.Column(db.INTEGER)
    hair_color = db.Column(db.VARCHAR(50))
    image = db.Column(db.VARCHAR(255))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'anime_id': self.anime_id,
            'gender': self.gender,
            'characteristics': self.characteristics,
            'age': self.age,
            'hair_color': self.hair_color,
            'image': self.image
        }