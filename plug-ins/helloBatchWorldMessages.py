#!/usr/bin/env python
#
# Use with scripts/helloBatchWorldMessages.scm to enable batch mode

import gtk
from gimpfu import *

def helloBatchWorldMessagesFn(messageType) :

    #dictionary mapping case values to functions see -> https://docs.python.org/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
    messageOptions = {0:noMessage,1:terminalMessage,2:gtkMessage,3:gimpMessage}
    messageFunction = messageOptions[messageType]
    # usage example:
    messageFunction('Message To Deliver')
    # gimpMessage(messageType)

#function to Deliver nothing
def noMessage(msgText) :
    return

def terminalMessage(msgText) :
    # Using stdout see -> https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
    print msgText
    # (Unix Terminal Output) Will not work on Windows Based Systems.

def gtkMessage(msgText) :
    # Using gtk to display an info type message see -> http://www.gtk.org/api/2.6/gtk/GtkMessageDialog.html#GtkMessageType
    message = gtk.MessageDialog(type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
    message.set_markup(msgText)
    message.run()
    message.destroy()

def gimpMessage(msgText) :
    # Using GIMP's interal procedure database see -> http://docs.gimp.org/en/glossary.html#glossary-pdb
    pdb.gimp_message(msgText)

# see -> http://www.gimp.org/docs/python/
register(
    #name
    "helloBatchWorldMessagesPlugin",

    #blurb
    "Saying Hello Batch World",

    #help
    "Saying Hello  to the Batch World",

    #author
    "William Crandell <william@crandell.ws>",

    #copyright
    "William Crandell <william@crandell.ws>",

    #date
    "2015",

    #menupath
    "Hello Batch World Messages",

    #imagetypes (use * for all, leave blank for none)
    "",

    #params
    [
        (PF_OPTION,"message-options", "Message Options:", 0, [("No Messages"),("Terminal Messages"),("Standard Gimp Messages"),("Pretty GTK Messages")]),
    ],

    #results
    [],

    #function (to call)
    helloBatchWorldMessagesFn,

    #this can be included this way or the menu value can be directly prepended to the menupath
    menu = "<Toolbox>/Hello/")

main()
