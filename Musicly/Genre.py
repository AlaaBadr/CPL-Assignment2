import pymysql

class Genre:
    def getGenresOfSong(self, songId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT genre.name
                       FROM genre INNER JOIN genre_song INNER JOIN song
                       ON genre_song.songId = song.id AND genre_song.genreId = genre.id
                       WHERE song.id = 
                    '''+songId+";")

        genres = cur.fetchall()

        cur.close()
        conn.close()

        return genres

    def addGenre(self):
        name = input("Enter the genre name: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO `genre` (`id`, `name`) VALUES (NULL,'" + name + "');")

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeGenre(self):
        genreId = input("Enter the genre number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `genre` WHERE `genre`.`id` = " + genreId)

        conn.commit()
        cur.close()
        conn.close()
