from Musicly.Song import SongController

class SongView:
    sc = SongController()

    def output(self, description, songs):
        print(description)
        for song in songs:
            print(song[1], "\t" ,"Duration: " ,song[3])

    def showPlaylistSongs(self, playlistId):
        description, songs = self.sc.getSongsOfPlaylist(playlistId)

        self.output(description, songs)

        if input("Enter 0 if you want to order or any key otherwise: ") == "0":
            print("1. name\n2. artist\n3.album\n4. release date")
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

            self.output(description, sorted(songs, key=lambda x: x[index], reverse=order))

