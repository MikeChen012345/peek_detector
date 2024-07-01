#!/usr/bin/env python

"""
Acknowledgement:
This script is based on https://github.com/arjun024/turn-off-screen
"""

import sys
import pyautogui

def screen_off(): 
    """
    Will keep the screen off.
    """
    if sys.platform.startswith('linux'):
        import os
        os.system("xset dpms force off")

    elif sys.platform.startswith('win'):
        import win32gui
        import win32con
        SC_MONITORPOWER = 0xF170
        win32gui.SendMessageTimeout(win32con.HWND_BROADCAST,
            win32con.WM_SYSCOMMAND, 
            SC_MONITORPOWER, 2, 
            win32con.SMTO_NOTIMEOUTIFNOTHUNG, 
            10)

    elif sys.platform.startswith('darwin'):
        import subprocess
        subprocess.call('echo \'tell application "Finder" to sleep\' | osascript', shell=True)

    else:
        print("Unsupported OS")


def screen_on():
    """
    Will turn the screen on.
    """
    pyautogui.click()
    