from flask import jsonify
from models.Anime import Anime
from models.Characters import Characters

class AnimeService:
    def getAnime(args):
        title = args.get('title')
        animes = Anime.query.filter(Anime.title == title)
        return jsonify({'data':[anime.serialize for anime in animes]})
    
    def getAnimeById(id):
        anime = Anime.query.filter_by(id=id).first_or_404()
        return jsonify({'data': [anime.serialize]})
        
    def getAllAnimeCharacters(slug):
        anime = Anime.query.filter_by(slug=slug).first()
        characters = Characters.query.filter_by(anime_id=anime.id).all()
        return jsonify({'data': [character.serialize for character in characters]})