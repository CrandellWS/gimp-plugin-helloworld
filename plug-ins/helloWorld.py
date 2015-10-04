#!/usr/bin/env python

import gtk
from gimpfu import *

def helloWorldFn() :

    # Using gtk to display an info type message see -> http://www.gtk.org/api/2.6/gtk/GtkMessageDialog.html#GtkMessageType
    message = gtk.MessageDialog(type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
    message.set_markup("Hello World \nThis Dialog Will Cause Unexpected Issues During Batch Procedures")
    message.run()
    message.destroy()

    # Using GIMP's interal procedure database see -> http://docs.gimp.org/en/glossary.html#glossary-pdb
    pdb.gimp_message("Hello World, This Message Looks Like An Error And/Or Warning")

    # Using stdout see -> https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
    print "Hello World \nThis message does not show in the GUI."
    # (Unix Terminal Output) Will not work on Windows Based Systems.
    return

# see -> http://www.gimp.org/docs/python/
register(
    #name
    "helloWorldPlugin",

    #blurb
    "Saying Hello World",

    #help
    "Saying Hello to the World",

    #author
    "William Crandell <william@crandell.ws>",

    #copyright
    "William Crandell <william@crandell.ws>",

    #date
    "2015",

    #menupath
    "Hello World",

    #imagetypes (use * for all, leave blank for none)
    "",

    #params
    [],

    #results
    [],

    #function (to call)
    helloWorldFn,

    #this can be included this way or the menu value can be directly prepended to the menupath
    menu = "<Toolbox>/Hello/")

main()
