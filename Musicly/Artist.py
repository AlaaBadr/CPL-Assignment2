import pymysql

class Artist:
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

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("INSERT INTO `artist`(`id`, `name`, `dateOfBirth`) VALUES(NULL, '"+name+"', '"+dateOfBirth+"');")

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeArtist(self):
        artistId = input("Enter the artist number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `artist` WHERE `artist`.`id` = "+artistId)

        conn.commit()
        cur.close()
        conn.close()