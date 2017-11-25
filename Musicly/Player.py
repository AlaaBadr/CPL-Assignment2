from pygame import *
from tkinter.filedialog import askopenfilename
from tkinter import Tk

class PlayerController:
    def playSong(self):
        Tk().withdraw()
        path = askopenfilename(initialdir="/home/alaa/Documents/MP3")
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(10)

pc = PlayerController()
pc.playSong()