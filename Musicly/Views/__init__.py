from Musicly.Views.AlbumView import AlbumView
from Musicly.Views.ArtistView import ArtistView
from Musicly.Views.PlaylistView import PlaylistView
from Musicly.Views.SongView import SongView

class MainView:
    pv = PlaylistView()
    arv = ArtistView()
    alv = AlbumView()
    sv = SongView()

    def welcome(self):
        print("Welcome To Musicly")

        while True:
            choice = int(input("1. Playlists\t2. Artists\t3. Albums\t4. Library\t5. Exit\n"))
            if choice == 1:
                self.pv.index()
            elif choice == 2:
                self.arv.index()
            elif choice == 3:
                self.alv.index()
            elif choice == 4:
                self.sv.index()
            else:
                break

# mv = MainView()
# mv.welcome()
