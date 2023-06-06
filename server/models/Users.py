from models.db import db

class Users(db.Model):
    username = db.Column(db.VARCHAR(50), primary_key=True)
    favorite_anime = db.Column(db.ARRAY(db.INTEGER))
    favorite_characters = db.Column(db.ARRAY(db.INTEGER))
    