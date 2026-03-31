import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, db_filename, table_name):
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_filename)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

csv_to_sqlite("data/csbrodle_data.csv", "data/characters.sqlite", "characters")