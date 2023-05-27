from flask import Flask

app = Flask(__name__)

@app.route("/genres")
def genres():
    return {
        "genres": [
            {
            "name": "Action",
            "slug": "action"
            },
            {
            "name": "Adventure",
            "slug": "adventure"
            },
            {
            "name": "Comedy",
            "slug": "comedy"
            },
            {
            "name": "Drama",
            "slug": "drama"
            },
            {
            "name": "Fantasy",
            "slug": "fantasy"
            },
            {
            "name": "Horror",
            "slug": "horror"
            },
            {
            "name": "Mystery",
            "slug": "mystery"
            },
            {
            "name": "Romance",
            "slug": "romance"
            },
            {
            "name": "Sci-Fi",
            "slug": "sci-fi"
            },
            {
            "name": "Slice of Life",
            "slug": "slice-of-life"
            }
        ]
    }

@app.route("/anime")
def anime():
    return {
        "anime": [
            {
            "title": "One Piece",
            "slug": "one-piece",
            "genres": [
                {"name": "Action", "slug": "action"},
                {"name": "Adventure", "slug": "adventure"},
                {"name": "Comedy", "slug": "comedy"},
                {"name": "Fantasy", "slug": "fantasy"}
            ],
            "rating": 8.56,
            "episode_count": 1000,
            "release_year": 1999,
            "image_url": "https://example.com/one_piece.jpg"
            },
            {
            "title": "Naruto",
            "slug": "naruto",
            "genres": [
                {"name": "Action", "slug": "action"},
                {"name": "Adventure", "slug": "adventure"},
                {"name": "Comedy", "slug": "comedy"}
            ],
            "rating": 8.3,
            "episode_count": 720,
            "release_year": 2002,
            "image_url": "https://example.com/naruto.jpg"
            },
            {
            "title": "Attack on Titan",
            "slug": "attack-on-titan",
            "genres": [
                {"name": "Action", "slug": "action"},
                {"name": "Drama", "slug": "drama"},
                {"name": "Fantasy", "slug": "fantasy"},
                {"name": "Mystery", "slug": "mystery"}
            ],
            "rating": 9.0,
            "episode_count": 75,
            "release_year": 2013,
            "image_url": "https://example.com/attack_on_titan.jpg"
            },
            {
            "title": "One Punch Man",
            "slug": "one-punch-man",
            "genres": [
                {"name": "Action", "slug": "action"},
                {"name": "Comedy", "slug": "comedy"},
                {"name": "Sci-Fi", "slug": "sci-fi"}
            ],
            "rating": 8.6,
            "episode_count": 24,
            "release_year": 2015,
            "image_url": "https://example.com/one_punch_man.jpg"
            },
            {
            "title": "Your Lie in April",
            "slug": "your-lie-in-april",
            "genres": [
                {"name": "Drama", "slug": "drama"},
                {"name": "Music", "slug": "music"},
                {"name": "Romance", "slug": "romance"}
            ],
            "rating": 8.8,
            "episode_count": 22,
            "release_year": 2014,
            "image_url": "https://example.com/your_lie_in_april.jpg"
            }
        ]
    }

if __name__ == "__main__":
    app.run(debug=True,host="localhost", port=8000)