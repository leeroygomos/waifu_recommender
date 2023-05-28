import React, { useState, useEffect } from 'react';
import './App.css';

function App() {

  const [anime, setAnime] = useState([{}]);

  useEffect(() => {
      fetch("/anime")
      .then(response => response.json())
      .then(data => {
        console.log(data.anime);
        setAnime(data.anime);
      });
    }, []);

  return (
    <div>
        {anime.map(ani => {
          return (<div key={ani.slug}>
                    <h1>{ani.title}</h1>
                    <h3>Genres</h3>
                    <ul>
                      {ani.genre.map(genre => { return <li key={genre}>{genre}</li>})}
                    </ul>
                    <h3>Rating</h3>
                    <p>{ani.rating}</p>
                    <h3># Episodes: </h3>
                    <p>{ani.episode_count}</p>
                    <h3>Release Year</h3>
                    <p>{ani.release_year}</p>
                  </div>
              )
        })}
    </div>
  );
}

export default App;
