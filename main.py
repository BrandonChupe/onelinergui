import clipboard #custom module containing our primary functions for things.
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from autogitupdate import update

#updateusinggit

update()


class MyWindow(Gtk.Window):

    def __init__(self):

        #window title
        Gtk.Window.__init__(self, title="PYTHON SAVES TEH WORLD")

        #setting up button arrangement and spacing.
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)


        #Creating the actual butttons.
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


    #Methods to be ran upon button click.
    def on_du_clicked(self, widget):
        clipboard.du()

    def on_wplogin_clicked(self, widget):
        clipboard.wplogin()

    def on_serial_clicked(self, widget):
        clipboard.serial()   

    def on_tailall_clicked(self, widget):
        clipboard.tailall()

    def on_handlers_combo_changed(self, combo):
        phpVersion = combo.get_active_text()
        clipboard.addhandler(phpVersion)

    def on_whyme_clicked(self, widget):
        clipboard.whyme()

    def on_wau_clicked(self, widget):
        clipboard.wau()


#Making sure the window actually works and closes.
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
