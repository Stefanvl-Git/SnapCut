from tkinter import *
import os
import webbrowser

os.system("clear")

from infi.systray import SysTrayIcon
def info(systray):
    webbrowser.open('http://net-informations.com', new=2)
menu_options = (("Info", None, exit),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()
