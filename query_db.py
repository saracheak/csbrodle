from flask import session
import sqlite3

def connect_to_db():
    conn = sqlite3.connect("data/characters.sqlite")
    return conn

def get_all_characters():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM characters")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(row)

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
    comparison = [0, 0, 0, 0, 0, 0]

    #name
    comparison[0] = "match" if guess_attr[0] == target_attr[0] else "not_match"
    
    #age
    if guess_attr[1] == target_attr[1]:
        comparison[1] = "match"
    elif guess_attr[1] < target_attr[1]:
        comparison[1] = "younger"
    else:
        comparison[1] = "older"

    #height
    if guess_attr[2] == target_attr[2]:
        comparison[2] = "match"
    elif guess_attr[2] < target_attr[2]:
        comparison[2] = "shorter"
    else:
        comparison[2] = "taller"

    #hair
    comparison[3] = "match" if guess_attr[3] == target_attr[3] else "not_match"

    #sex
    comparison[4] = "match" if guess_attr[4] == target_attr[4] else "not_match"
    
    #series
    comparison[5] = "match" if guess_attr[5] == target_attr[5] else "not_match"
    
    return comparison