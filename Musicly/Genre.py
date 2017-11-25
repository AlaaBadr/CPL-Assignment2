import pymysql
import re

class GenreController:
    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT * FROM `genre`;''')

        genres = cur.fetchall()

        cur.close()
        conn.close()

        return genres

    def getSongsOfGenre(self, genreId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT song.path FROM song JOIN genre_song ON song.id = genre_song.songId WHERE genre_song.genreId = "+str(genreId)+";")

        songs = cur.fetchall()

        cur.close()
        conn.close()

        return songs

    def getGenresOfSong(self, songId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT genre.name
                       FROM genre INNER JOIN genre_song INNER JOIN song
                       ON genre_song.songId = song.id AND genre_song.genreId = genre.id
                       WHERE song.id = 
                    '''+str(songId)+";")

        genres = cur.fetchall()

        cur.close()
        conn.close()

        return genres

    def addGenre(self, name):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute(
            '''INSERT INTO `genre` (`id`, `name`) VALUES (NULL,"''' + name + '''");''')

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeGenre(self):
        genreId = input("Enter the genre number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `genre` WHERE `genre`.`id` = '"+genreId+"';")

        conn.commit()
        cur.close()
        conn.close()

    def findOrNew(self, genre):
        genres = re.split("/|,", genre)
        genreIds = []

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        for g in genres:
            print(g)
            cur.execute('''SELECT genre.id FROM genre WHERE `name` = "'''+g+'''";''')

            nila = cur.fetchone()
            if nila is None:
                genreIds.append(self.addGenre(str(g)))
            else:
                genreIds.append(nila[0])

        cur.close()
        conn.close()

        return genreIds