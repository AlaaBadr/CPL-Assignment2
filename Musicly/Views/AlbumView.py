from Musicly.Album import AlbumController
from Musicly.Views.Player import PlayerController

class AlbumView:
    alc = AlbumController()
    player = PlayerController()

    def outputAlbums(self, albums):
        print("Albums:")
        for playlist in albums:
            print("\t*", playlist[0], "\t\t\ttracks: ", playlist[1])
        print()

    def index(self):
        albums = self.alc.getAll()
        self.outputAlbums(albums)

        while True:
            choice = int(input("Select an album to play, or 0 to exit: "))
            if choice != 0:
                songs = self.alc.getSongsOfAlbum(choice)
                self.player.playAll(songs)
            else:
                break
