from flask import jsonify
from models.Characters import Characters

class CharacterService:
    def getCharacter(id):
        character = Characters.query.filter_by(id=id).first()
        return jsonify({'character': [character.serialize]})
    
    def getCharacters(args):
        name = args.get('name')
        print(name)
        characters = Characters.query.filter(Characters.name == name)
        return jsonify({'data':[character.serialize for character in characters]})
    
    def getAllCharacters():
        characters = Characters.query.all()
        return jsonify({'character': [character.serialize for character in characters]})
