import pymysql

class Genre:
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
