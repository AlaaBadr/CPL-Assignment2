import pymysql
from Musicly.Band import BandController

class Album:
    def addAlbum(self):
        bandController = BandController()
        bandController.getAll()

        band = input("Enter the number of the band chosen or 0 to create one: ")

        if(band == "0"):
            band = bandController.addBand()

        title = input("Enter the album title: ")
        release_date = input("Enter the playlist release date: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("INSERT INTO `album` (`id`, `title`, `release_date`, `band`) VALUES (NULL,'" + title + "', '" + release_date + "', '"+band+"');")

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeAlbum(self):
        albumId = input("Enter the album number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `album` WHERE `album`.`id` = " + albumId)

        conn.commit()
        cur.close()
        conn.close()