from models.db import db

class Anime(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.VARCHAR(255), nullable=False)
    title_english = db.Column(db.VARCHAR(255))
    title_japanese = db.Column(db.VARCHAR(255))
    image = db.Column(db.VARCHAR)
    episodes = db.Column(db.INTEGER)
    type = db.Column(db.VARCHAR(50))
    source = db.Column(db.VARCHAR(50))
    status = db.Column(db.VARCHAR(50))
    duration = db.Column(db.VARCHAR(255))
    rating = db.Column(db.VARCHAR(100))
    score = db.Column(db.INTEGER)
    synopsis = db.Column(db.VARCHAR)
    year = db.Column(db.INTEGER)
    genres = db.Column(db.ARRAY(db.INTEGER))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'title_english': self.title_english,
            'title_japanese': self.title_japanese,
            'image': self.image,
            'episodes': self.episodes,
            'type': self.type,
            'source': self.source,
            'status': self.status,
            'duration': self.duration,
            'rating': self.rating,
            'score': self.score,
            'synopsis': self.synopsis,
            'year': self.year,
            'genres': self.genres,
        }