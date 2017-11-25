from Musicly.Genre import GenreController
from Musicly.Player import PlayerController


class GenreView:
    gc = GenreController()
    player = PlayerController()

    def index(self):
        genres = self.gc.getAll()
        for genre in genres:
            print(genre[0],"- ",genre[1])
        print()

        while True:
            choice = int(input("Select a genre to play all songs in it, or 0 to exit: "))
            if choice != 0:
                songs = self.gc.getSongsOfGenre(choice)
                self.player.playAll(songs)
            else:
                break