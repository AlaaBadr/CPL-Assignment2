import pymysql

class SongController:
    def addSong(self):

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()



        cur.close()
        conn.close()