import { useState } from 'react';
import './Characters.css';

export default function Characters(){
    const [searchTerm, setSearchTerm] = useState('');
    const [character, setCharacter] = useState(null);

    const searchAnime = () => {
        fetch(`/characters?name=${searchTerm}`)
        .then((response) => response.json())
        .then((json) => setCharacter(json.data))
    }

    return (
        <div>
            <input type="text" placeholder='search for a character' onChange={evt => setSearchTerm(evt.target.value)}/>
            <input type='submit' value='Search' onClick={() => searchAnime()}></input>
            {character !== null ? character.map(char => {
                return (
                    <div key={char.id}>
                        <img src={char.image} alt={char.name}/>
                        <h1>{char.name}</h1>
                        <h2>{char.name_kanji}</h2>
                        <h3>Nicknames</h3>
                        <p>{char.nicknames}</p>
                        <h3>About </h3>
                        <p>{char.about}</p>
                    </div>
                )
            }) : <></>}
        </div>
    );
}