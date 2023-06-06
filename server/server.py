# Imports
from flask import Flask, request
from os import environ, path
from dotenv import load_dotenv
from models.db import db
from services.AnimeService import AnimeService
from services.CharacterService import CharacterService
from services.DatabaseService import DatabaseService

# Load environment variables
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Define application
app = Flask(__name__)
app.url_map.strict_slashes = False

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)

# /
@app.route('/')
def index():
    return 'Server is running UWU'

# /anime
@app.route('/anime', methods=['GET'])
def getAnime():
    args = request.args
    return AnimeService.getAnime(args)

# /anime/<slug> 
@app.route('/anime/<id>', methods=['GET'])
def getAnimeById(id):
    return AnimeService.getAnimeById(id)

# /characters
@app.route('/characters', methods=['GET'])
def getCharacters():
    args = request.args
    return CharacterService.getCharacters(args)

# /characters/<slug>
@app.route('/characters/<slug>', methods=['GET'])
def getAllCharactersByAnime(slug):
    return AnimeService.getAllAnimeCharacters(slug)

# /character/<id>
@app.route('/character/<id>', methods=['GET'])
def getCharacter(id):
    return CharacterService.getCharacter(id)

@app.route('/search/anime', methods=['GET'])
def searchAnime():
    args = request.args.to_dict()
    return AnimeService.searchAnime(args)

@app.route('/initGenres', methods=['GET'])
def initGenres():
    return DatabaseService.initGenres()

@app.route('/initAnime', methods=['GET'])
def initAnime():
    return DatabaseService.initAnime()

@app.route('/gatherUsernames/<upper>/<lower>', methods=['GET'])
def gatherUsernames(upper, lower):
    return DatabaseService.gatherUsernames(upper, lower)

@app.route('/getUserFavorites', methods=['GET'])
def getUserFavorites():
    return DatabaseService.getUserFavorites()

@app.route('/initCharacters/<page>', methods=['GET'])
def initCharacters(page):
    return DatabaseService.initCharacters(page)

@app.route('/retryFailedCharacters', methods=['GET'])
def retryFailedCharacters():
    return DatabaseService.retryFailedCharacters()

# Run application
if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)