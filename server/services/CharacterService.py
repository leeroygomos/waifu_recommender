from flask import jsonify
from models.Character import Character

class CharacterService:
    def getCharacter(id):
        character = Character.query.filter_by(id=id).first()
        return jsonify({'character': [character.serialize]})
    
    def getAllCharacters():
        characters = Character.query.all()
        return jsonify({'character': [character.serialize for character in characters]})
