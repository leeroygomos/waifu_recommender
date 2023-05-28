from flask import jsonify
from models.Anime import Anime
from models.Character import Character

class AnimeService:
    def getAnime(slug):
        anime = Anime.query.filter_by(slug=slug).first_or_404()
        return jsonify(anime.serialize)
    
    def getAllAnime():
        animes = Anime.query.all()
        return jsonify({'anime':[anime.serialize for anime in animes]})
        
    def getAllAnimeCharacters(slug):
        anime = Anime.query.filter_by(slug=slug).first()
        characters = Character.query.filter_by(anime_id=anime.id).all()
        return jsonify([character.serialize for character in characters])