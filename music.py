#! /usr/bin/python3
# Parsa Amini, 2020
# Released by GPL3+

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import os
import pygame as pg
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

musics=[]
i = 0
c = 0

listbox = Gtk.ListBox()

pg.mixer.init()

win = Gtk.Window()
win.set_title("Music")
scrolledwin = Gtk.ScrolledWindow()


playbutton = Gtk.Button(label="PLay")
nextbutton = Gtk.Button(label=">>")
pervbutton = Gtk.Button(label="<<")

a=''
g = 0
def play():
    global musics, i, c, playbutton, listbox, g, a
    if g != 0:
        print(type(a),a)
       # listbox.select_row()
    g += 1
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



def nex(button):
    global i, c
    i += 1
    c = 0
    play()
nextbutton.connect("clicked", nex)

def perv(button):
    global i, c
    i -= 1
    c = 0
    play()
pervbutton.connect("clicked", perv)

def b1(button):
    global c
    play()
playbutton.connect("clicked", b1)

music_dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_MUSIC)
for file in os.walk(music_dir):
    for f in file:
        for f2 in f:
            if f2.endswith(".mp3"):
                l1 = Gtk.Label(label=f2)
                musics.append('{}/{}'.format(music_dir,f2))
                listbox.add(l1)


grid = Gtk.Grid()
grid.set_row_spacing(5)
grid.set_column_spacing(5)
win.add(grid)
grid.attach(scrolledwin,0,0,100,100)
scrolledwin.add(listbox)
grid.attach(playbutton,50,101,1,1)
grid.attach(nextbutton,51,101,1,1)
grid.attach(pervbutton,49,101,1,1)


def li(listbox, listboxrow):
    global musics, i, c, a
    c = 0
    i = listboxrow.get_index()
    a = listboxrow
    play()

listbox.connect("row-activated", li)



win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
