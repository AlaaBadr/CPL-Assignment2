import pymysql
from Musicly.Band import BandController

class ArtistController:
    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT artist.name FROM artist;")

        artists = cur.fetchall()

        cur.close()
        conn.close()

        return artists

    def addArtist(self):
        name = input("Enter the artist name: ")
        dateOfBirth = input("Enter his date of birth: ")

        bc = BandController()
        print(bc.getAll())
        choice = input("Enter the number of band the artist belongs to or 0 to create new one: ")
        if choice == 0:
            bandId = bc.addBand(name)
        else:
            bandId = choice

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''INSERT INTO `artist`(`id`, `name`, `dateOfBirth`) VALUES(NULL, "'''+name+'''", "'''+dateOfBirth+'''");''')

        conn.commit()
        cur.close()
        conn.close()

        self.addArtistToBand(str(bandId), str(cur.lastrowid))

        return cur.lastrowid

    def removeArtist(self):
        artistId = input("Enter the artist number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `artist` WHERE `artist`.`id` = '"+artistId+"';")

        conn.commit()
        cur.close()
        conn.close()

    def addArtistToBand(self, bandId, artistId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("INSERT INTO `artist_band`(`artistId`, `bandId`) VALUES("+artistId+","+bandId+");")

        conn.commit()
        cur.close()
        conn.close()