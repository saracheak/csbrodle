import './style.css'

const guess = document.getElementById('guess-input');
const guessBtn = document.getElementById('guess-btn');
const results = document.getElementById('results-container');
const characterList = document.getElementById('character-list');

let guessCount = 0;
let allCharacterNames = [];

document.addEventListener('DOMContentLoaded', async (event) => {
    //Get target character
    const target = await fetch('/api/start');

    //Get all characters for autocomplete
    const response = await fetch('/api/characters');
    const characters = await response.json();
    allCharacterNames = characters.map(c => c[0]); 
});

guess.addEventListener('input', () => {
    const val = guess.value;

    if (val.length === 0) {
        characterList.innerHTML = '';
        return;
    }

    if (characterList.children.length === 0) {
        allCharacterNames.forEach(name => {
            const opt = document.createElement('option');
            opt.value = name;
            characterList.appendChild(opt);
        });
    }
});

async function handleGuess() {
    console.log("User inputted a guess");
    const input = document.getElementById('guess-input');
    const resultsContainer = document.getElementById('results-container');
    const name = input.value;

    if (!name) return;

    const response = await fetch('/api/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name })
    });

    const data = await response.json();
    console.log(data);
    if (data.error) {
        alert(data.error);
        return;
    }

    //Increment guess count for row number and reset input
    guessCount++;
    input.value = '';

    //Create row
    const row = document.createElement('div');
    row.className = "grid grid-cols-8 gap-2 text-center text-sm items-center mb-2 animate-slide-in";

    //Get color of box depending on status
    const getBoxClass = (status) => {
        if (status === 'match') return 'box-correct text-black font-bold';
        if (status === 'younger' || status === 'older') return 'box-partial';
        if (status === 'taller' || status === 'shorter') return 'box-partial';
        return 'box-wrong';
    };

    //Get arrow for age and height depending on status
    const getArrow = (status) => {
        if (status === 'taller' || status === 'older') return ' ↓';
        if (status === 'shorter' || status === 'younger') return ' ↑';
        return '';
    };

    //Add boxes to row
    row.innerHTML = `
        <div class="text-gray-500">${guessCount}</div>
        <div class="${getBoxClass(data.name.status)} p-4 rounded-lg h-16 flex items-center justify-center">${data.name.value}</div>
        <div class="${getBoxClass(data.age.status)} p-4 rounded-lg h-16 flex items-center justify-center">${data.age.value}${getArrow(data.age.status)}</div>
        <div class="${getBoxClass(data.height.status)} p-4 rounded-lg h-16 flex items-center justify-center">${data.height.value}${getArrow(data.height.status)}</div>
        <div class="${getBoxClass(data.hair.status)} p-4 rounded-lg h-16 flex items-center justify-center">${data.hair.value}</div>
        <div class="${getBoxClass(data.sex.status)} p-4 rounded-lg h-16 flex items-center justify-center">${data.sex.value}</div>
        <div class="${getBoxClass(data.series.status)} p-4 rounded-lg h-16 flex items-center justify-center">${data.series.value}</div>
    `;

    //Add row to results container
    resultsContainer.prepend(row);

    characterList.innerHTML = '';
}

//User presses Guess button
guessBtn.addEventListener('click', handleGuess);

//User presses 'Enter' on keyboard
guess.addEventListener('keydown', (event) => {
    if(event.key == 'Enter'){
        handleGuess();
    }
});