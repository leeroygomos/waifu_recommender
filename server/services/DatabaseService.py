import requests, time, math, asyncio
from models.db import db
from models.Genre import Genre
from models.Anime import Anime


class DatabaseService:
    ## ANIME DATA ###

    def initAnime():
        hasNextPage = True
        page = 1
        count = 0

        while hasNextPage:
            requestString = "https://api.jikan.moe/v4/anime/?page{}".format(page)
            response = requests.get(requestString)
            if (response.status_code == 429):
                time.sleep(3)
                continue
            else:
                print("current page: {}".format(page))
                hasNextPage = response.json()["pagination"]["has_next_page"]
                anime = response.json()["data"]
                page += 1

                for i in anime:
                    count += 1
                    allGenres = []
                    for i in i["genres"]:
                        allGenres.append(i["mal_id"])
                    if "explicit_genres" in i:
                        for i in i["explicit_genres"]:
                            allGenres.append(i["mal_id"])
                    if "themes" in i:
                        for i in i["themes"]:
                            allGenres.append(i["mal_id"])
                    if "demographics" in i:
                        for i in i["demographics"]:
                            allGenres.append(i["mal_id"])
                    newAnime = Anime(
                        id=i["mal_id"], 
                        title=i["title"],
                        title_english=i["title_english"],
                        title_japanese=i["title_japanese"],
                        image_url=i["images"]["jpg"]["image_url"],
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
                
                try:
                    db.session.commit()
                except:
                    return "failed to add at page {}".format(math.floor(page/25))
                
        return "added {} anime".format(count)

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
