import requests, time
from models.db import db
from models.Genre import Genre
from models.Anime import Anime
from models.Users import Users
from models.Characters import Characters
from models.Failed import Failedanime, Failedcharacters


allAnime = []
allCharacters = []

class DatabaseService:
    ## ANIME DATA ###

    def initAnime():
        hasNextPage = True
        page = 1

        while hasNextPage:
            requestString = "https://api.jikan.moe/v4/anime/?page={}".format(page)
            response = requests.get(requestString)
            while (response.status_code == 429):
                print("Sleeping...")
                time.sleep(3)
                response = requests.get(requestString)
            else:
                print("current page: {}".format(response.json()["pagination"]["current_page"]))
                hasNextPage = response.json()["pagination"]["has_next_page"]
                print("hasNextPage: {}".format(hasNextPage))
                anime = response.json()["data"]
                allAnime.extend(anime)
                page = response.json()["pagination"]["current_page"] + 1

        return DatabaseService.addAnime()

    def addAnime():
        print("starting anime insertions")
        count = 0
        for i in allAnime:
            count += 1
            allGenres = []
            for j in i["genres"]:
                allGenres.append(j["mal_id"])
            for k in i["explicit_genres"]:
                allGenres.append(k["mal_id"])
            for l in i["themes"]:
                allGenres.append(l["mal_id"])
            for h in i["demographics"]:
                allGenres.append(h["mal_id"])
            newAnime = Anime(
                id=i["mal_id"], 
                title=i['title'],
                title_english=i["title_english"],
                title_japanese=i["title_japanese"],
                image=i["images"]["jpg"]["image_url"],
                episodes=i["episodes"],
                type=i["type"],
                source=i["source"],
                status=i["status"],
                duration=i["duration"],
                rating=i["rating"],
                score=i["score"],
                synopsis=i["synopsis"],
                year=i["year"],
                genres=allGenres,
            )
            db.session.add(newAnime)
            print("Added anime #{}".format(count))

            try:
                db.session.commit()
                print("Added anime #{}".format(count))
            except:
                db.session.rollback()
                print("Anime with mal_id {} failed to commit".format(i["mal_id"]))
                DatabaseService.insertFailedAnime(i["mal_id"])
        
        return "added {} anime".format(count)

    def insertFailedAnime(id):
        failedanime = Failedanime(id=id)
        db.session.add(failedanime)
        db.session.commit()

    ### GENRES DATA ###
    def initGenres():
        response = requests.get("https://api.jikan.moe/v4/genres/anime")
        myDic = response.json()["data"]
        count = 0
        for dic in myDic:
            newGenre = Genre(id=dic["mal_id"], name=dic["name"])
            db.session.add(newGenre)
            count += 1
        
        try:
            db.session.commit()
        except:
            return 'failed to add genres'

        return 'added {} genres'.format(count)

    ### USERNAMES ###
    def gatherUsernames(upper, lower):
        count = 0
        failedCount = 0
        for i in range(int(upper), int(lower)+1):
            requestString = "https://api.jikan.moe/v4/users?page={}".format(i)
            try:
                response = requests.get(requestString,timeout=5)
            except:
                print("timed out... continuing")
                i -= 1
                continue
            if (response.status_code == 429):
                print("Sleeping...")
                time.sleep(3)
                i -= 1
                continue
            else:
                print("current page: {}".format(i))
                if "data" in response.json(): 
                    users = response.json()["data"]
                    for user in users:
                        newUser = Users(
                            username=user['username'],
                            favorite_anime=[],
                            favorite_characters=[]
                        )
                
                        db.session.add(newUser)
                        try:
                            db.session.commit()
                            count += 1
                        except:
                            failedCount += 1
                            db.session.rollback()
                else:
                    print("data does not exist")

        return "successfully added {} users. {} users failed to be added".format(count, failedCount)


    ### USER FAVORITES ###
    def getUserFavorites():
        users = Users.query.filter(Users.favorite_anime == "{}" and Users.favorite_characters == "{}")
        for user in users:
            requestString = "https://api.jikan.moe/v4/users/{}/favorites".format(user.username)
            try:
                response = requests.get(requestString,timeout=5)
            except:
                print("timed out... continuing")
                continue
            if (response.status_code == 429):
                print("Sleeping...")
                time.sleep(3)
                continue
            elif "data" in response.json(): 
                favAnime = response.json()['data']['anime']
                favCharacters = response.json()['data']['characters']

                favAnimeIds = []
                for anime in favAnime:
                    favAnimeIds.append(anime['mal_id'])

                favCharacterIds = []
                for character in favCharacters:
                    favCharacterIds.append(character['mal_id'])

                if len(favAnimeIds) == 0 and len(favCharacterIds) == 0: 
                    db.session.delete(user)

                else:
                    user.favorite_anime = favAnimeIds
                    user.favorite_characters = favCharacterIds
                    db.session.add(user)
                
                try:
                    db.session.commit()
                    print("updated user: {}".format(user.username))
                except:
                    db.session.rollback()
                    print("failed to update user: {}".format(user.username))
            
        return "finished updating favorites"

    ### CHARACTERS ###
    def initCharacters(page):
        page = int(page)
        hasNextPage = True
        maxPage = page + 1000

        while hasNextPage and page < maxPage:
            requestString = "https://api.jikan.moe/v4/characters?page={}".format(page)
            response = requests.get(requestString)
            while (response.status_code == 429):
                print("Sleeping...")
                time.sleep(3)
                response = requests.get(requestString)
            
            print("current page: {}".format(response.json()["pagination"]["current_page"]))
            hasNextPage = response.json()["pagination"]["has_next_page"]
            characters = response.json()["data"]
            allCharacters.extend(characters)
            page = response.json()["pagination"]["current_page"] + 1

        return DatabaseService.addCharacters()
    
    def addCharacters():
        print("starting character insertions")
        count = 0
        for i in allCharacters:
            count += 1
            newCharacter = Characters(
                id=i["mal_id"], 
                image=i["images"]["jpg"]["image_url"],
                name=i["name"],
                name_kanji=i["name_kanji"],
                nicknames=i["nicknames"],
                about=i["about"],
                anime=[],
            )
            db.session.add(newCharacter)

            try:
                db.session.commit()
                print("Added character #{}".format(count))
            except:
                db.session.rollback()
                print("Character with mal_id {} failed to commit".format(i["mal_id"]))
                DatabaseService.insertFailedCharacter(i["mal_id"])
        
        return "added {} characters".format(count)
    
    def insertFailedCharacter(id):
        failedChar = Failedcharacters(id=id)
        db.session.add(failedChar)
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def retryFailedCharacters():
        failedCharacters = Failedcharacters.query.all()
        charIds = []

        for failedChar in failedCharacters:
            char = db.session.query(Characters.id).filter(Characters.id == failedChar.id)

            if char != None:
                db.session.delete(failedChar)
                try:
                    db.session.commit()
                    print("deleted failed user: {}".format(failedChar.id))
                except:
                    db.session.rollback()
                    print("failed to delete failed user: {}".format(failedChar.id))
            else:
                charIds.append(failedChar.id)
        
        count = 0

        for charId in charIds:
            requestString = "https://api.jikan.moe/v4/characters/{}".format(charId)
            response = requests.get(requestString)
            while (response.status_code == 429):
                print("Sleeping...")
                time.sleep(3)
                response = requests.get(requestString)
            
            currentChar = response['data']

            count += 1
            newCharacter = Characters(
                id=currentChar["mal_id"], 
                image=currentChar["images"]["jpg"]["image_url"],
                name=currentChar["name"],
                name_kanji=currentChar["name_kanji"],
                nicknames=currentChar["nicknames"],
                about=currentChar["about"],
                anime=[],
            )
            db.session.add(newCharacter)

            try:
                db.session.commit()
                print("Added character #{}".format(count))
            except:
                db.session.rollback()
                print("Character with mal_id {} failed to commit".format(currentChar["mal_id"]))

        return 'done'
    
    def updateCharacterAnime():
        characters = Characters.query.filter(Characters.anime == "{}")

        for character in characters:
            requestString = "https://api.jikan.moe/v4/characters/{}/anime".format(character.id)
            try:
                response = requests.get(requestString,timeout=5)
            except:
                print("timed out... continuing")
                continue
            while (response.status_code == 429):
                print("Sleeping...")
                time.sleep(3)
                response = requests.get(requestString)
            
            try:
                currentCharAnime = response.json()['data']
            except:
                continue
            animeIds = []

            for currentAnime in currentCharAnime:
                animeIds.append(currentAnime['anime']['mal_id'])

            character.anime = animeIds

            db.session.add(character)

            try:
                db.session.commit()
                print("Updated character #{}".format(character.id))
            except:
                db.session.rollback()
                print("Character with mal_id {} failed to commit".format(character.id))

        return 'finished'

            
            