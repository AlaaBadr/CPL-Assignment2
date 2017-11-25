import mutagen
import pymysql
from mutagen.id3 import ID3
from mutagen.id3._frames import USLT
from mutagen import *

from Musicly.Album import AlbumController
from Musicly.Genre import GenreController
from Musicly.Band import BandController

from tkinter.filedialog import askopenfilename
from tkinter import Tk

class SongController:
    def getSongsOfPlaylist(self, playlistId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT playlist.description FROM playlist WHERE playlist.id = "+playlistId+";")

        description = cur.fetchone()[0]

        cur.execute('''SELECT result.*, band.name as ft
                       FROM (
                       SELECT song.id, song.name, song.lyrics, song.length, song.path,
                       album.release_date, album.title as album_name,
                       band.name as band_artist
                       FROM song JOIN album JOIN band JOIN playlist_song
                       ON song.album = album.id AND album.band = band.id AND song.id=playlist_song.songId
                       WHERE playlist_song.playlistId = '''+playlistId+''') AS result LEFT JOIN
                       (band INNER JOIN featuring)
                       ON result.id = featuring.songId AND band.id = featuring.bandId 
                    ''')

        songs = cur.fetchall()

        cur.close()
        conn.close()

        return description, songs

    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT result.*, band.name as ft
                       FROM (
                       SELECT song.id, song.name, song.lyrics, song.length, song.path,
                       album.release_date, album.title as album_name,
                       band.name as band_artist
                       FROM song JOIN album JOIN band
                       ON song.album = album.id AND album.band = band.id ) AS result LEFT JOIN 
                       (band INNER JOIN featuring)
                       ON result.id = featuring.songId AND band.id = featuring.bandId;
                    ''')

        songs = cur.fetchall()

        cur.close()
        conn.close()

        return songs

    def addSong(self):
        Tk().withdraw()
        path = askopenfilename(initialdir="/home/alaa/Documents/MP3")

        ac = AlbumController()
        gc = GenreController()
        bc = BandController()

        var = mutagen.File(path, easy=True)
        tags = ID3(path)
        lyc = tags.getall("USLT")

        name = var['title'][0]
        if len(lyc) == 0:
            lyrics = ""
        else:
            lyrics = lyc[0].text.replace('\"','\'')

        bands = bc.findOrNew(var['artist'][0])
        length = var.info.length
        date = var['date'][0]
        if var['musicbrainz_albumtype'][0] == "single":
            albumId = ac.findOrNew(album='singles', bandId=bands[0])
        else:
            albumId = ac.findOrNew(album=var['album'][0], bandId=bands[0], date=date)
        if 'genre' in tags.keys():
            genres = gc.findOrNew(var['genre'][0])
        else:
            genres = []

        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''INSERT INTO `song` (`id`, `name`, `lyrics`, `length`, `album`, `path`)
                       VALUES (NULL, "'''+name+'''", "'''+lyrics+'''", "'''+str(length)+'''", "'''+str(albumId)+'''", "'''+path+'''");''')
        songId = cur.lastrowid

        bands.pop(0)
        for b in bands:
            cur.execute("INSERT INTO featuring (`bandId`, `songId`) VALUES ('"+str(b)+"', '"+str(songId)+"');")

        for g in genres:
            cur.execute("INSERT INTO genre_song (`songId`, `genreId`) VALUES ('"+str(songId)+"', '"+str(g)+"');")

        conn.commit()
        cur.close()
        conn.close()

        return songId

    def addSongToPlaylist(self, songId, playlistId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("INSERT INTO playlist_song (`playlistId`, `songId`) VALUES ('"+playlistId+", '"+songId+"');")

        conn.commit()
        cur.close()
        conn.close()

    def removeSong(self, songId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `song` WHERE `song`.`id` = "+songId+";")

        conn.commit()
        cur.close()
        conn.close()

    def removeSongFromPlaylist(self, songId, playlistId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("DELETE FROM `playlist_song` WHERE `songId` = '"+songId+"' AND playlistId = '"+playlistId+"';")

        conn.commit()
        cur.close()
        conn.close()