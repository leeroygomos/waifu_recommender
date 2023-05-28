from models.db import db
from models.Enums import genre

class Anime(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.VARCHAR(255))
    slug = db.Column(db.VARCHAR(255))
    rating = db.Column(db.DECIMAL(3,2))
    episode_count = db.Column(db.INTEGER)
    release_year = db.Column(db.INTEGER)
    image_url = db.Column(db.VARCHAR(255))
    genre = db.Column(db.ARRAY(genre))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'rating': self.rating,
            'episode_count': self.episode_count,
            'release_year': self.release_year,
            'image_url': self.image_url,
            'genre': self.genre
        }