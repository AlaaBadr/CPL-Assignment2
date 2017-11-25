import pymysql
import pygame

from Musicly.Album import AlbumController
from tkinter.filedialog import askopenfilename
from tkinter import Tk

class SongController:
    def getSongsOfPlaylist(self, playlistId):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute("SELECT playlist.description FROM playlist WHERE playlist.id = "+playlistId+";")

        description = cur.fetchall()

        cur.execute('''SELECT result.*, band.name as ft
                       FROM (
                       SELECT song.id, song.name, song.lyrics, song.length,
                       album.release_date, album.title as album_name,
                       band.name as band_artist
                       FROM song JOIN album JOIN band JOIN playlist_song
                       ON song.album = album.id AND album.band = band.id AND song.id=playlist_song.songId
                       WHERE playlist_song.playlistId = '''+playlistId+''') AS result LEFT JOIN
                       (band INNER JOIN featuring)
                       ON result.id = featuring.songId AND band.id = featuring.bandId 
                    ''')

        songs = cur.fetchall()

        print(songs)

        cur.close()
        conn.close()

        return description, songs

    def getAll(self):
        conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        cur = conn.cursor()

        cur.execute('''SELECT result.*, band.name as ft
                       FROM (
                       SELECT song.id, song.name, song.lyrics, song.length,
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
        filename = askopenfilename()
        print(filename)

        # albumController = AlbumController()
        # print(albumController.getAll())
        #
        # albumId = input("Enter the number of the album, or 0 if single song or n to create new album: ")
        # name = input("Enter song name: ")
        # lyrics = input("Enter lyrics of the song: ")
        # length = input("Enter length in seconds: ")
        #
        # conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='musicly')
        # cur = conn.cursor()
        #
        # cur.execute("INSERT INTO `song` (`id`, `name`, `lyrics`, `length`, `album`) VALUES (NULL, '"+name+"', '"+lyrics+"', '"+length+"', '"+albumId+"');")
        #
        # conn.commit()
        # cur.close()
        # conn.close()

    def playSong(self):
        # Tk().withdraw()
        # filename = askopenfilename(initialdir='/media/alaa/New Volume/Mp3/')

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('/home/alaa/Cadbury.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()

s = SongController()
s.playSong()