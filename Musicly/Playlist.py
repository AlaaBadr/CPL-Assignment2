# import sqlite3
import pymysql

class PlaylistController:

    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT playlist.id, playlist.name, COUNT(playlist_song.songId) AS tracks
                                    FROM playlist LEFT JOIN playlist_song
                                    ON playlist.id = playlist_song.playlistId
                                    GROUP BY playlist.name
                                ''')
        playlists = cur.fetchall()

        cur.close()
        conn.close()

        return playlists

    def addPlaylist(self):
        name = input("Enter the playlist name: ")
        description = input("Enter the playlist description: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("INSERT INTO `playlist` (`id`, `name`, `description`) VALUES (NULL,'"+name+"', '"+description+"');")

        conn.commit()
        cur.close()
        conn.close()

        return cur.lastrowid

    def removePlaylist(self):
        playlistId = input("Enter the playlist number: ")

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `playlist` WHERE `playlist`.`id` = "+playlistId)

        conn.commit()
        cur.close()
        conn.close()

