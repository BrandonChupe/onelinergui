# Module containing the the function we use to send items to our cliboard.
import clipboard

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):

        # Window title.
        Gtk.Window.__init__(self, title="PYTHON SAVES TEH WORLD")

        # Sets up button arrangement and spacing.
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        # Creates the actual butttons.
        self.du = Gtk.Button(label="du")
        self.du.connect("clicked", self.on_du_clicked)
        self.box.pack_start(self.du, True, True, 0)

        self.wplogin = Gtk.Button(label="wplogin")
        self.wplogin.connect("clicked", self.on_wplogin_clicked)
        self.box.pack_start(self.wplogin, True, True, 0)

        self.serial = Gtk.Button(label="serial")
        self.serial.connect("clicked", self.on_serial_clicked)
        self.box.pack_start(self.serial, True, True, 0)

        self.tailall = Gtk.Button(label="tailall")
        self.tailall.connect("clicked", self.on_tailall_clicked)
        self.box.pack_start(self.tailall, True, True, 0)

        self.strace = Gtk.Button(label="strace")
        self.strace.connect("clicked", self.on_strace_clicked)
        self.box.pack_start(self.strace, True, True, 0)

        # Creates a dropdown filled with options from the list handlers.
        self.handlers = ["54", "55", "56", "70"]
        self.handlers_combo = Gtk.ComboBoxText()
        self.handlers_combo.set_entry_text_column(0)
        self.handlers_combo.connect("changed", self.on_handlers_combo_changed)
        for handler in self.handlers:
            self.handlers_combo.append_text(handler)
        self.box.pack_start(self.handlers_combo, True, True, 0)

        self.whyme = Gtk.Button(label="whyme")
        self.whyme.connect("clicked", self.on_whyme_clicked)
        self.box.pack_start(self.whyme, True, True, 0)

        self.wau = Gtk.Button(label="wau")
        self.wau.connect("clicked", self.on_wau_clicked)
        self.box.pack_start(self.wau, True, True, 0)

    # Functions to be ran upon button click.
    def on_du_clicked(self, widget):
        clipboard.du()

    def on_wplogin_clicked(self, widget):
        clipboard.wp_login()

    def on_serial_clicked(self, widget):
        clipboard.serial()

    def on_tailall_clicked(self, widget):
        clipboard.tail_all()

    def on_strace_clicked(self, widget):
        clipboard.strace()

    def on_handlers_combo_changed(self, combo):
        phpVersion = combo.get_active_text()
        clipboard.add_handler(phpVersion)

    def on_whyme_clicked(self, widget):
        clipboard.why_me()

    def on_wau_clicked(self, widget):
        clipboard.wau()


def gui_loop():
    """Opens the primary gui window."""
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
