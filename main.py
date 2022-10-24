import gi
from screeninfo import get_monitors
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk
from gi.repository import GdkPixbuf

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.menus.headbar as hdb
import scripts.main_fixed as mf
import scripts.button_connect as btnc
import scripts.styles.styles as styles

class Main(gtk.Window):
    def __init__(self):

        style_provider = gtk.CssProvider()
        css_data = styles.style
        style_provider.load_from_data(css_data)
        gtk.StyleContext.add_provider_for_screen(
            gdk.Screen.get_default(),
            style_provider,
            gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        super().__init__()


        self.add(mf.main_fixed)
        self.set_titlebar(hdb.headb)
        btnc.btn_connect()
        self.show_all()

win = Main()
win.set_default_size(inc.win_w, inc.win_h)
win.set_resizable(0)
win.connect("destroy", gtk.main_quit)
g2.set_win_init(win)
#win.show_all()
gtk.main()
