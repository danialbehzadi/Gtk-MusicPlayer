import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import os
import pygame as pg
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

musics=[]
i = 0
c = 0
pg.mixer.init()

win = gtk.Window()
win.set_title("Music")
scrolledwin = gtk.ScrolledWindow()


playbutton = gtk.Button(label="PLay")



def play():
    global musics, i, c, playbutton

    if c == 0:
        pg.mixer.quit()
        samplerate = MP3(musics[i]).info.sample_rate
        pg.mixer.init(samplerate)
        pg.mixer_music.load(musics[i])
        pg.mixer_music.play()
        playbutton.set_label("Pause")
        c += 1
    elif c%2 == 1:
        print("pause")
        pg.mixer_music.pause()
        playbutton.set_label("Play")
        c += 1
    elif c%2 == 0:
        pg.mixer_music.unpause()
        playbutton.set_label("Pause")
        c += 1




listbox = gtk.ListBox()

def b1(button):
    global c
    play()

playbutton.connect("clicked", b1)

for file in os.walk("/home/parsa/Music"):
    for f in file:
        for f2 in f:
            if f2.endswith(".mp3"):
                l1 = gtk.Label(f2)
                musics.append("/home/parsa/Music/"+f2)
                listbox.add(l1)


grid = gtk.Grid()
grid.set_row_spacing(5)
grid.set_column_spacing(5)
win.add(grid)
grid.attach(scrolledwin,0,0,100,100)
scrolledwin.add(listbox)
grid.attach(playbutton,50,101,1,1)


def li(listbox, listboxrow):
    global musics, i, c
    c = 0
    i = listboxrow.get_index()
    play()

listbox.connect("row-activated", li)

win.connect("destroy", gtk.main_quit)
win.show_all()
gtk.main()
