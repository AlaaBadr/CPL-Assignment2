import sqlite3

class DatabaseCreator:
    def __init__(self):
        conn = sqlite3.connect('musicly.db')

        conn.execute('''CREATE TABLE IF NOT EXISTS `song` 
                        (
                          id INTEGER PRIMARY KEY,
                          name VARCHAR(100),
                          lyrics TEXT,
                          length INTEGER,
                          FOREIGN KEY(album) REFERENCES album(id)
                        );
                     ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `album`
                        (
                          id INTEGER PRIMARY KEY,
                          title VARCHAR(100),
                          release_date DATE,
                          FOREIGN KEY(band) REFERENCES band(id)
                        );
                     ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `genre`
                        (
                          id INTEGER PRIMARY KEY,
                          name VARCHAR(100)
                        );
                     ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `artist`
                        (
                          id INTEGER PRIMARY KEY,
                          name VARCHAR(100),
                          dateOfBirth DATE
                        );
                     ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `band`
                        (
                          id INTEGER PRIMARY KEY,
                          name VARCHAR(100)
                        );
                     ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `playlist`
                        (
                          id INTEGER PRIMARY KEY,
                          name VARCHAR(100),
                          description TEXT
                        );
                     ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `featuring`
                        (
                          id INTEGER PRIMARY KEY,
                          FOREIGN KEY(bandId) REFERENCES band(id),
                          FOREIGN KEY(songId) REFERENCES song(id)
                        )
                     ''')