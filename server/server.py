# Imports
from flask import Flask, request
from os import environ, path
from dotenv import load_dotenv
from models.db import db
from services.AnimeService import AnimeService
from services.CharacterService import CharacterService

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
def getAllAnime():
    return AnimeService.getAllAnime()

# /anime/<slug> 
@app.route('/anime/<slug>', methods=['GET'])
def getAnime(slug):
    return AnimeService.getAnime(slug)

# /characters
@app.route('/characters', methods=['GET'])
def getAllCharacters():
    return CharacterService.getAllCharacters()

# /characters/
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

# Run application
if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)