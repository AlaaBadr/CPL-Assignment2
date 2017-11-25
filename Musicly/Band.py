import pymysql
import re

class BandController:
    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT * FROM `band`;")

        bands = cur.fetchall()

        cur.close()
        conn.close()

        return bands

    def getSongsOfBand(self, bandId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT song.path FROM song JOIN album ON song.album = album.id WHERE album.band = "+str(bandId)+" ;")

        songs = cur.fetchall()

        cur.close()
        conn.close()

        return songs

    def addBand(self, name):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''INSERT INTO `band` (`id`, `name`) VALUES (NULL, "'''+name+'''");''')

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeBand(self):
        bandId = input("Enter the band number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `band` WHERE `band`.`id` = '"+bandId+"';")

        conn.commit()
        cur.close()
        conn.close()

    def findOrNew(self, band):
        bands = re.split(" feat. | and | & |feat.|and|&", band)
        bandIds = []

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        for b in bands:
            cur.execute('''SELECT band.id FROM band WHERE `name` = "'''+b+'''";''')

            nila = cur.fetchone()
            if nila is None:
                bandIds.append(self.addBand(b))
            else:
                bandIds.append(nila[0])

        cur.close()
        conn.close()

        return bandIds