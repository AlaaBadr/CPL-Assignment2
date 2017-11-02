import sqlite3

class DatabaseCreator:
    def __init__(self):
        conn = sqlite3.connect('musicly.db')

        conn.execute('''CREATE TABLE IF NOT EXISTS `band`
                                        (
                                          id INTEGER PRIMARY KEY,
                                          name VARCHAR(100)
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


        conn.execute('''CREATE TABLE IF NOT EXISTS `album`
                                (
                                  id INTEGER PRIMARY KEY,
                                  title VARCHAR(100),
                                  release_date DATE,
                                  band INTEGER,
                                  FOREIGN KEY(band) REFERENCES band(id) ON DELETE CASCADE ON UPDATE CASCADE 
                                );
                             ''')

        conn.execute('''CREATE TABLE IF NOT EXISTS `song` 
                        (
                          id INTEGER PRIMARY KEY,
                          name VARCHAR(100),
                          lyrics TEXT,
                          length INTEGER,
                          album INTEGER,
                          FOREIGN KEY(album) REFERENCES album(id) ON DELETE CASCADE ON UPDATE CASCADE
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
                          bandId INTEGER,
                          songId INTEGER,
                          FOREIGN KEY(bandId) REFERENCES band(id) ON DELETE CASCADE ON UPDATE CASCADE,
                          FOREIGN KEY(songId) REFERENCES song(id) ON DELETE CASCADE ON UPDATE CASCADE,
                          PRIMARY KEY(bandId,songId)
                        )
                     ''')
        conn.execute('''CREATE TABLE IF NOT EXISTS `genre_song`
                        (
                          songId INTEGER,
                          genreId INTEGER,
                          FOREIGN KEY (songId) REFERENCES song(id) ON DELETE CASCADE ON UPDATE CASCADE,
                          FOREIGN KEY (genreId) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE,
                          PRIMARY KEY (songId,genreId)
                        )
                      ''')
        conn.execute('''CREATE TABLE IF NOT EXISTS `playlist_song`
                                (
                                  playlistId INTEGER,
                                  songId INTEGER,
                                  FOREIGN KEY (playlistId) REFERENCES playlist(id) ON DELETE CASCADE ON UPDATE CASCADE,
                                  FOREIGN KEY (songId) REFERENCES song(id) ON DELETE CASCADE ON UPDATE CASCADE,
                                  PRIMARY KEY (playlistId,songId) 
                                )
                              ''')
        conn.execute('''CREATE TABLE IF NOT EXISTS `artist_band`
                                (
                                  artistId INTEGER,
                                  bandId INTEGER,
                                  FOREIGN KEY (artistId) REFERENCES artist(id) ON DELETE CASCADE ON UPDATE CASCADE,
                                  FOREIGN KEY (bandId) REFERENCES band(id) ON DELETE CASCADE ON UPDATE CASCADE,
                                  PRIMARY KEY (artistId,bandId)
                                )
                              ''')
        conn.close()

