from models.db import db

class Characters(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    image = db.Column(db.VARCHAR)
    name = db.Column(db.VARCHAR(255), nullable=False)
    name_kanji = db.Column(db.VARCHAR(255))
    nicknames = db.Column(db.ARRAY(db.VARCHAR))
    about = db.Column(db.VARCHAR)
    anime = db.Column(db.ARRAY(db.INTEGER))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'name': self.name,
            'name_kanji': self.name_kanji,
            'nicknames': self.nicknames,
            'about': self.about,
            'anime': self.anime
        }