from models.db import db

class Failedanime(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Failedcharacters(db.Model):
    id = db.Column(db.Integer, primary_key=True)