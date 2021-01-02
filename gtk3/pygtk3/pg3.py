#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk as gtk

def click (x):
    print("hello there")

def on_quit (x):
    print("goodbye")
    gtk.main_quit ()

def main ():
    builder = gtk.Builder()
    builder.add_from_file ("pg3.glade")

    win_wg = builder.get_object ("window1")
    win_wg.show ()

    but1_wg = builder.get_object ("button1")
    but1_wg.connect ("clicked", click)

    win_wg.connect ("destroy", on_quit)

    gtk.main ()

if __name__ == "__main__":
    main()

