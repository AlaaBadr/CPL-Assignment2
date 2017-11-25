import pymysql

class BandController:
    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT * FROM `band`;")

        bands = cur.fetchall()

        cur.close()
        conn.close()

        return bands

    def addBand(self):
        name = input("Enter the band name: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("INSERT INTO `band` (`id`, `name`) VALUES (NULL, '"+name+"');")

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removeBand(self):
        bandId = input("Enter the band number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `band` WHERE `band`.`id` = "+bandId)

        conn.commit()
        cur.close()
        conn.close()