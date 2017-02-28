# -*- coding: utf-8 -*-
import json
import requests
import signal
import os
import gi
# import sys
# try:
#     import pygtk
#     pygtk.require("2.0")
# except:
#     pass
# try:
#     import gtk
#     import gtk.glade
# except:
#     print("GTK Not Availible")
#     sys.exit(1)

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GObject
from gi.repository import Notify
from gi.repository import AppIndicator3

APPID = "GTK Test"
CURRDIR = os.path.dirname(os.path.abspath(__file__))
# could be PNG or SVG as well
ICON = os.path.join(CURRDIR, 'web.png')


# Cross-platform tray icon implementation
# See:
# * http://ubuntuforums.org/showthread.php?t=1923373#post11902222
# * https://github.com/syncthing/syncthing-gtk/blob/master/syncthing_gtk/statusicon.py
class TrayIcon:
    def __init__(self, appid, icon, menu):
        self.menu = menu

        APPIND_SUPPORT = 1
        # TODO SAFETY
        if APPIND_SUPPORT == 1:
            self.ind = AppIndicator3.Indicator.new(
                appid, icon,
                AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
            self.ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
            self.ind.set_menu(self.menu)
        else:
            self.ind = Gtk.StatusIcon()
            self.ind.set_from_file(icon)


class Handler:
    filename = "config.xml"

    def __init__(self):
        self.window_is_hidden = True

    def onShowOrHide(self, *args):
        if self.window_is_hidden:
            window.show()
        else:
            window.hide()

        self.window_is_hidden = not self.window_is_hidden

    def onQuit(self, *args):
        Notify.uninit()
        Gtk.main_quit()

    def onButtonPressed(self, box, *args, **kwargs):
        children = box.get_children()
        entries = []

        for child in children:
            if isinstance(child, Gtk.Entry):
                entries.append(child)

        values = {}
        for entry in entries:
            values.update({entry.get_name(): entry.get_text()})

        login_dict = {"notify_method": "login", "email": values.get('Login'), "password": values.get('Password')}

        login_response = requests.post("http://rmnova.30meridian.com/API", json=login_dict)
        token = login_response.json()
        window.hide()
        LastNotify(email=values['Login'], token=json.loads(token)['token'])
        #gobject.timeout_add(300000, self.periodic) #gobject - объект PyGObject

    # def startCycleTimer(self, counter):
    #     GObject.timeout_add_seconds(15000, self.displaytimer(counter))

    def writing(self):
        with open(self.filename, "r+") as writed_file:
            writed_file.write()

    def parsing(self):
        with open(self.filename, "r+") as read_file:
           for line in read_file:
               token = line[11:43]


class LastNotify(object):
    def __init__(self, email, token):
        self.email = email
        self.token = token
        self.last_notify_params = {"notify_method": "get_last", "email": email, "token": token}


    def last_notify_cicle(self):
        get_last_notify_response = requests.post("http://rmnova.30meridian.com/API", json=self.last_notify_params)


if __name__ == '__main__':
    # Handle pressing Ctr+C properly, ignored by default
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    builder = Gtk.Builder()
    builder.add_from_file('gtk-example.glade')
    builder.connect_signals(Handler())

    window = builder.get_object('window1')
    window.set_icon_from_file(ICON)
    window.show_all()

    entry = builder.get_object('entry1')
    menu = builder.get_object('menu1')
    icon = TrayIcon(APPID, ICON, menu)
    Notify.init(APPID)
    #print builder.get_objects()

    Gtk.main()
