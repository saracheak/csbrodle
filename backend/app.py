from flask import Flask, render_template, session, request, jsonify
import query_db

app = Flask(__name__)
app.secret_key = "csbro"

@app.route("/api/start")
def index():
    """
    Picks target character and save in session
    """
    target = query_db.get_random_character()
    # target = query_db.get_character_by_name('Conrad Fisher')
    session['target_name'] = target[0]
    session['target_age'] = target[1]
    session['target_height'] = target[2]
    session['target_hair'] = target[3]
    session['target_sex'] = target[4]
    session['target_series'] = target[5]
    return jsonify({"status": "Game started"})

@app.route("/api/characters")
def search():
    """
    Gets full list of characters
    """
    all_characters = query_db.get_all_characters()
    return jsonify(all_characters)
    

@app.route("/api/guess", methods=['POST'])
def guess():
    """
    Triggers when user guesses a character name
    """
    target_attr = [session.get('target_name'), session.get('target_age'), session.get('target_height'), session.get('target_hair'), session.get('target_sex'), session.get('target_series')]
    print(f"/api/guess {target_attr}")
    user_guess = request.json.get('name')
    return query_db.compare_characters(user_guess, target_attr)

if __name__ == '__main__':
    app.run()