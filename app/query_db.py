from flask import session
import sqlite3

def connect_to_db():
    conn = sqlite3.connect("./../data/characters.sqlite") 
    return conn

def get_all_characters():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM characters")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_random_character():
    """
    Gets a random character from database

    @return: A random character=
    @rtype: tuple
    """
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM characters ORDER BY RANDOM() LIMIT 1")
    random_character = cur.fetchone()
    conn.close()
    return random_character

def get_character_by_name(name):
    """
    Gets a character tuple from database based on name

    @return: 
    @rtype: tuple
    """
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM characters WHERE Name = ?", (name,))
    guess_character = cur.fetchone()
    conn.close()
    return guess_character

def compare_characters(guess, target_attr):
    """
    Compares name to target attributes
    """
    print(target_attr)
    guess_attr = get_character_by_name(guess)
    comparison = {}

    #name
    name_result = "match" if guess_attr[0] == target_attr[0] else "not_match"
    comparison['name'] = {"value":guess_attr[0], "status": name_result}
    
    #age
    age_result = ""
    if guess_attr[1] == target_attr[1]:
        age_result = "match"
    elif guess_attr[1] < target_attr[1]:
        age_result = "younger"
    else:
        age_result = "older"
    comparison['age'] = {"value":guess_attr[1], "status": age_result}

    #height
    height_result = ""
    if guess_attr[2] == target_attr[2]:
        height_result = "match"
    elif guess_attr[2] < target_attr[2]:
        height_result = "shorter"
    else:
        height_result = "taller"
    comparison['height'] = {"value":guess_attr[2], "status": height_result}

    #hair
    hair_result = "match" if guess_attr[3] == target_attr[3] else "not_match"
    comparison['hair'] = {"value":guess_attr[3], "status": hair_result}

    #sex
    sex_result = "match" if guess_attr[4] == target_attr[4] else "not_match"
    comparison['sex'] = {"value":guess_attr[4], "status": sex_result}
    
    #series
    series_result = "match" if guess_attr[5] == target_attr[5] else "not_match"
    comparison['series'] = {"value":guess_attr[5], "status": series_result}
    
    print(comparison)
    return comparison