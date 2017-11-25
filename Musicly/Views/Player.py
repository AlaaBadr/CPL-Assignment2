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

        while True:
            choice = int(input("1. Stop"))
            if choice == 1:
                mixer.music.stop()
            else:
                break

    def shuffle(self, songs):
        songsPaths = []
        for song in songs:
            songsPaths.append(song[4])
        shuffled = random.choice(songsPaths)
        mixer.init()
        mixer.music.load(shuffled)
        mixer.music.play()

    def playAllPlaylist(self, songs):
        mixer.init()
        for song in songs:
            mixer.music.queue(song[4])

    def playAll(self, songs):
        mixer.init()
        for song in songs:
            mixer.music.queue(song[0])
