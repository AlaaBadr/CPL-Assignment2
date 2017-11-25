from Musicly.Band import BandController
from Musicly.Player import PlayerController


class ArtistView:
    bc = BandController()
    player = PlayerController()

    def index(self):
        artists = self.bc.getAll()
        for artist in artists:
            print(artist[1])
        print()

        while True:
            choice = int(input("Select a band to play their all songs, or 0 to exit: "))
            if choice != 0:
                songs = self.bc.getSongsOfBand(choice)
                self.player.playAll(songs)
            else:
                break