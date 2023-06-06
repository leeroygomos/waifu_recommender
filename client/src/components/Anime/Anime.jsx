import { useState } from 'react';
import './Anime.css';

export default function Anime(){
    const [searchTerm, setSearchTerm] = useState('');
    const [anime, setAnime] = useState(null);

    const searchAnime = () => {
        fetch(`/anime?title=${searchTerm}`)
        .then((response) => response.json())
        .then((json) => setAnime(json.data))
    }

    return (
        <div>
            <input type="text" placeholder='search for anime' onChange={evt => setSearchTerm(evt.target.value)}/>
            <input type='submit' value='Search' onClick={() => searchAnime()}></input>
            {anime !== null ? anime.map((ani) => {
                return (
                    <div key={ani.id}>
                        <img src={ani.image} alt={ani.title}/>
                        <h1>{ani.title}</h1>
                        <h2>{ani.title_japanese}</h2>
                        <h3>Rating</h3>
                        <p>{ani.rating}</p>
                        <h3># Episodes: </h3>
                        <p>{ani.episodes}</p>
                        <h3>Duration</h3>
                        <p>{ani.duration}</p>
                        <h3>Released</h3>
                        <p>{ani.season} {ani.year}</p>
                        <h3>Status</h3>
                        <p>{ani.status}</p>
                        <h3>Type</h3>
                        <p>{ani.type}</p>
                        <h3>Synopsis</h3>
                        <p>{ani.synopsis}</p>
                    </div>
                )
            }) : <></>}

        </div>
    );
}