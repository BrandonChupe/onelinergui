from sys import argv
from time import strftime
import pandas
import csv


def send_to_clipboard(data):
    """send data to clipboard. Requires csv.QUOTE_NONE to prevent duplication of
    quoting when it passes content into clipboard.
    """
    df = pandas.DataFrame([data])
    df.to_clipboard(index=False, header=False, quoting=csv.QUOTE_NONE)


def read_from_file(input):
    """Alternative function for when we read one liners from a file. Saving for
    future use.
    """
    input_open = open(input, 'r+')
    return str(input_open.read())


def serial():
    """Creates a state of authority timestamp based on current time."""
    serial = strftime('%Y%m%d%H')
    serial = int(serial) + 1
    send_to_clipboard(serial)


def du():
    """Terrible inode and space usage one liner. Useful for seeing which
        characters needed to be escaped."""
    du = "echo -e \"\\033[0;35mDetailed Inode and Space usage for: "\
        "$(pwd)\\033[0m\" ; echo -e \"\\033[0;34mInodes\\033[0m"\
        " - \\033[0;31mDiskUsage -Folder\\033[0m\";"\
        " for d in `find -maxdepth 1 -type d |cut -d\\/ -f2 |grep -xv . |"\
        "sort`; do s=$(du -h --max-depth=0 $d); c=$(find $d |wc -l);"\
        " printf \"\\033[0;34m$c\\t\\033[0m- \\033[0;31m$s\\t\\n\\033[0m\" ;"\
        " done ; printf \"\\033[0;34mTotal Inodes:\\033[0m \\033[1;34m\\t\\t"\
        "$(find $(pwd) | wc -l)\\n\\033[0m\"; printf \"\\033[0;31m"\
        "Total Disk Usage:\\033[0m \\033[1;31m\\t$(du -sh .)\\n\\033[0m\""
    send_to_clipboard(du)


def wp_login():
    """One liner to log into mysql with a wp-config.php's info."""
    wpLogin = "mysql -u$(awk -F\\' '/DB_U/ { print $4 }' ./wp-config.php) "\
              "-p$(awk -F\\' '/DB_P/ { print $4 }' ./wp-config.php) "\
              "$(awk -F\\' '/DB_N/ { print $4 }' ./wp-config.php)"
    send_to_clipboard(wpLogin)


def tail_all():
    """Tail all of the error logs. ALL OF THEM"""
    tailall = "tail -n0 -f $(find -type f -name \'error_log\')"
    send_to_clipboard(tailall)


# Need to add a version for easy apache 4.
def add_handler(phpVersion):
    """Sends a printf/sed friendly version of the normal addhandlers
    to the clipboard.
    """
    addHandler = "# Use PHP" + phpVersion + " as default\\nAddHandler "\
                 "application/x-httpd-php" + phpVersion + " .php\\n"\
                 "<IfModule mod_suphp.c>\\n    suPHP_ConfigPath /opt/php"\
                 + phpVersion + "/lib\\n</IfModule>"
    send_to_clipboard(addHandler)


def why_me():
    """WHYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"""
    whyMe = "WHYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"\
        "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"\
        " ;-;-;-;-;-;-;-;-;"
    send_to_clipboard(whyMe)


def wau():
    """WAUWAUWAUWAUWAUWAUWAU"""
    wau = "WAU"
    send_to_clipboard(wau)
