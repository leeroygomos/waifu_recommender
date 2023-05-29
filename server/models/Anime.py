from models.db import db

class Anime(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.VARCHAR(255))
    slug = db.Column(db.VARCHAR(255))
    rating = db.Column(db.DECIMAL(3,1))
    episode_count = db.Column(db.INTEGER)
    release_year = db.Column(db.INTEGER)
    genre = db.Column(db.VARCHAR(255))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'rating': self.rating,
            'episode_count': self.episode_count,
            'release_year': self.release_year,
            'genre': self.genre
        }