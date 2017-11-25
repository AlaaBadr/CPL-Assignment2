from Musicly.Genre import GenreController
from Musicly.Player import PlayerController
from Musicly.Song import SongController

class SongView:
    sc = SongController()
    gc = GenreController()
    player = PlayerController()

    def output(self, description, songs):
        print(description)
        for song in songs:
            print("\t", song[0], "- ", song[1], "\t\t" ,"Duration: " ,song[3])

    def showPlaylistSongs(self, playlistId):
        description, songs = self.sc.getSongsOfPlaylist(playlistId)

        while True:
            self.output(description, songs)
            choice = int(input("0. Order\t1. View Song\t2. Play Song\t3.Shuffle Song\t4. Play All Playlist\t5. Remove Song from Playlist\n"))
            if choice == 0:
                songs = self.order(songs)
            elif choice == 1:
                songId = int(input("Enter song number: "))
                song = [x for x in songs if x[0] == songId][0]
                self.outputSong(song)
            elif choice == 2:
                songId = int(input("Enter song number: "))
                path = [x for x in songs if x[0] == songId][0][4]
                self.player.playSong(path)
            elif choice == 3:
                self.player.shuffle(songs)
            elif choice == 4:
                self.player.playAllPlaylist(songs)
            elif choice == 5:
                songId = int(input("Enter song number: "))
                self.sc.removeSongFromPlaylist(songId, playlistId)
            else:
                break

    def order(self, songs):
        print("1. Name\n2. Artist\n3. Album\n4. Release date")
        criteria = int(input("Choose a criteria to order:"))
        way = int(input("1. Ascending\n2. Descending"))

        if criteria == 1:
            index = 1
        elif criteria == 2:
            index = 6
        elif criteria == 3:
            index = 5
        elif criteria == 4:
            index = 4

        if way == 1:
            order = False
        elif way == 2:
            order = True

        return sorted(songs, key=lambda x: x[index], reverse=order)

    def outputSong(self, song):
        print("Song: ", song[1])
        print("Band/Artist: ", song[7])
        print("Featured artist/band: ", song[8])
        print("Album: ", song[6])
        print("Release date: ", song[5])
        print("Genres:")
        genres = self.gc.getGenresOfSong(song[0])
        for g in genres:
            print("\t",g[0])
        print("Lyrics: ", song[2])
        print()

    def index(self):
        while True:
            songs = self.sc.getAll()
            for song in songs:
                print(song[0], "- ", song[1], "\t\t", song[7])

            choice = int(input("1. Play song\t2. Add Song\t3. Remove Song"))
            if choice == 1:
                songId = int(input("Enter song number: "))
                path = [x for x in songs if x[0] == songId][0][4]
                self.player.playSong(path)
            elif choice == 2:
                self.sc.addSong()
            elif choice == 3:
                songId = int(input("Enter song number: "))
                self.sc.removeSong(songId)
            else:
                break