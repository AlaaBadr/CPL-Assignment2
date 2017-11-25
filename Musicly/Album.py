import pymysql
from Musicly.Band import BandController

class AlbumController:
    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT album.title, COUNT(*) AS tracks
                       FROM album JOIN song
                       ON album.id = song.album
                       GROUP BY album.title;
                    ''')

        albums = cur.fetchall()

        cur.close()
        conn.close()

        return albums

    def addAlbum(self, title, bandId, release_date):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''INSERT INTO `album` (`id`, `title`, `release_date`, `band`) VALUES (NULL,"''' + title + '''", "''' + release_date + '''", "'''+str(bandId)+'''");''')

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeAlbum(self):
        albumId = input("Enter the album number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `album` WHERE `album`.`id` = '"+albumId+"';")

        conn.commit()
        cur.close()
        conn.close()

    def findOrNew(self, album, bandId, date = None):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT album.id FROM album WHERE `title` = "'''+album+'''" AND `band` = '''+str(bandId)+''';''')

        nila = cur.fetchone()
        if nila is None:
            albumId = self.addAlbum(album, bandId, str(date))
        else:
            albumId = nila[0]

        cur.close()
        conn.close()

        return albumId