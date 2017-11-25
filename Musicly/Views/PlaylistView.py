from Musicly.Playlist import PlaylistController
from Musicly.Song import SongController
from Musicly.Views.SongView import SongView

class PlaylistView:
    pl = PlaylistController()
    sv = SongView()
    sc = SongController()
    def outputPlaylists(self):
        playlists = self.pl.getAll()

        print("Playlists:")
        for playlist in playlists:
            print("\t", playlist[0], "- ", playlist[1], "\t\t\ttracks: ", playlist[2])

    def index(self):
        while True:
            self.outputPlaylists()

            choice = int(input("\n1. View Playlist\t\t2. Back To Home\n3. Add Playlist\t\t4. Delete Playlist\t\t5.Add Song to Playlist\n"))
            if choice == 1:
                playlistId = input("Enter playlist number: ")
                self.sv.showPlaylistSongs(playlistId)
            elif choice == 2:
                break
            elif choice == 3:
                self.playlistInput()
            elif choice ==4:
                playlistId = input("Enter playlist number: ")
                self.pl.removePlaylist(playlistId)
            elif choice == 5:
                self.sv.index()
                songId = int(input("Enter song number: "))
                playlistId = int(input("Enter playlist number: "))
                self.sc.addSongToPlaylist(songId,playlistId)
            else:
                break

    def playlistInput(self):
        name = input("Enter Playlist name: ")
        description = input("Enter Description: ")
        self.pl.addPlaylist(name,description)
