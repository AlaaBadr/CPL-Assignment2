import sqlite3


class Playlist:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getAll(self):
        conn = sqlite3.connect('musicly.db')
        playlists = conn.execute('''select playlist.name as name, count(*)
from playlist inner join playlist_song
on playlist.id = playlist_song.playlistId
group by (name)''')
        conn.close()

    def get