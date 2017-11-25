import random

from pygame import *
from tkinter.filedialog import askopenfilename
from tkinter import Tk

class PlayerController:
    def playSong(self, path):
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        # while mixer.music.get_busy():
        #     time.Clock().tick(10)

        choice = int(input("1. Stop"))
        if choice == 1:
            mixer.music.stop()

    def shuffle(self, songs):
        songsPaths = []
        for song in songs:
            songsPaths.append(song[4])
        shuffled = random.choice(songsPaths)
        mixer.init()
        mixer.music.load(shuffled)
        mixer.music.play()

    def playAllPlaylist(self, songs):
        if len(songs) == 0:
            print("No songs")
            return
        for i in range(len(songs)):
            if i == 0:
                mixer.init()
                mixer.music.load(songs[i][4])
                mixer.music.play()
            else:
                mixer.music.queue(songs[i][4])

    def playAll(self, songs):
        if len(songs) ==0:
            print("No songs")
            return
        for i in range(len(songs)):
            if i == 0:
                mixer.init()
                mixer.music.load(songs[i][0])
                mixer.music.play()
            else:
                mixer.music.queue(songs[i][0])
