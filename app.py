from flask import Flask, render_template, session, request
import query_db

app = Flask(__name__)
app.secret_key = "csbro"

@app.route("/")
def index():
    target = query_db.get_random_character()
    session['target_name'] = target[0]
    session['target_age'] = target[1]
    session['target_height'] = target[2]
    session['target_hair'] = target[3]
    session['target_sex'] = target[4]
    session['target_series'] = target[5]
    return render_template("index.html")

@app.route("/api/search")
def search():
    return
    

@app.route("/api/guess")
def guess():
    target_attr = [session.get('target_name'), session.get('target_age'), session.get('target_height'), session.get('target_hair'), session.get('target_sex'), session.get('target_series')]
    # user_guess = request.json.get('guess')
    user_guess = "Meredith Palmer"
    return query_db.compare_characters(user_guess, target_attr)

if __name__ == '__main__':
    app.run()