import signal
import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk
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

    Gtk.main()
