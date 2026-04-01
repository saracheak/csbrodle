# TV Character Game

## Wordle-like game for TV show characters 
csbrodle is a game that starts with TV show characters that my friends and I have watched, but has easy customization for any TV shows you have watched.

## Characters from the following TV shows:
<li>New Girl</li>
<li>The Summer I Turned Pretty</li>
<li>The Office</li>
<li>Parks and Recreation</li>
<li>Brooklyn 99</li>
<li>The Good Place</li>
<br>

Only main or secondary characters were chosen.

## Customize!
These customizations only works when running app on localhost!

#### Customize TV Characters
The app takes in TV characters from `csbrodle_data.csv `. You can add/delete TV characters into this csv as long as the attributes **exactly** match according to name, age, height, hair, sex, series. 

#### Choose Target Character
If users would like to decide the target character, they can hard code the character name **exactly** as in the `csbrodle_data.csv`. 
1. Comment out `target = query_db.get_random_character()` in `backend/app.py`'s `index()`
2. Add your own target using this format `target = query_db.get_character_by_name('Your target here')`
3. E.g. `target = query_db.get_character_by_name('Conrad Fisher')`

## Tech Stack
<li>Backend - Python, Flask</li>
<li>Frontend - JavaScript, HTML, Tailwind, Vite</li>
