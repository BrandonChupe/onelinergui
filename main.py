# This module primarily acts as a launcher to check for updates before running
# the rest of the script.
import pickle
import requests
import importlib
from bs4 import BeautifulSoup
from datetime import date

# imports the module containing the majority of the script.
import gui


class UpdateAvailable(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "My Dialog", parent, 0,
                            (Gtk.STOCK_CANCEL,
                                Gtk.ResponseType.CANCEL,
                                Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)

        label = Gtk.Label("There is an update available.",
                          "Would you like to download it now?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class DialogWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="UpdateAvailable")

        self.set_border_width(6)

        button = Gtk.Button("Open dialog")
        button.connect("clicked", self.on_button_clicked)

        self.add(button)

    def on_button_clicked(self, widget):
        dialog = UpdateAvailable(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            perform_update()
        elif response == Gtk.ResponseType.CANCEL:
            pass

        dialog.destroy()


def check_update(day):
    """If it has not checked for an update today it will check for one using the
    remote version file and local version file. It will also update the
    lastupdate file with the most recent date that it checked for an update.
    """
    if (date.today() == day):
        return False
    elif (date.today() > day):
        if (float(import_version_remote()) > float(import_version_local())):
            export_date(day)
            return True
        else:
            export_date(day)
            return False


def import_version_remote():
    """Imports the version number from the version file in the github
    repository.
    """
    response = requests.get('https://raw.githubusercontent.com/BrandonChupe/',
                            'onelinergui/master/version.txt')
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()


def import_version_local():
    """Imports the version number from the local version file."""
    with open('version.txt', 'r') as myfile:
        data = myfile.read()
    return data


def import_date():
    """Imports the last day an update was checked from a local pickle file, if
    none exists it uses a default day.
    """
    try:
        day = pickle.load(open("lastupdate.p", "rb"))
    except:
        day2 = date(2017, 9, 25)
        return day2

    return day


def export_date(day):
    """exports the day to a pickle file."""
    pickle.dump(day, open("lastupdate.p", "wb"))


def get_repository_files(url):
    """Obtains a list of files within the github repository using GitHub's
    restful API. Returns it as a list of download urls.
    """
    fileList = []

    resp = requests.get(url)
    for each in resp.json():
        fileList.append(each['download_url'])

    return fileList


# Need to watch for optimization.
def download_file(url):
    """Uses requests to obtain a file's contents then write it to disk."""
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

    return local_filename


def guiwindow():
    """Opens a dialogue window to confirm that the user wishes to update to the
    latest version.
    """
    win = DialogWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def perform_update():
    """Downloads the updated repository files and reloads the custom module."""
    fileList = get_repository_files(REPOSITORY_URL)

    for each in fileList:
        download_file(each)

    importlib.reload(gui)

# Change this if you create your own branch. Replace "BrandonChupe" with
# your github user.
REPOSITORY_URL = ('https://api.github.com/repos/BrandonChupe',
                  '/onelinergui/contents')

if check_update(import_date()):
    guiwindow()


interface.gui_loop()
