# ============================================
# JARVIS — SYSTEM SKILLS
# ============================================

import os
import subprocess

def set_volume(level):
    # level 0-100
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)

def get_battery():
    import psutil
    battery = psutil.sensors_battery()
    return f"Battery is at {battery.percent} percent"

def take_screenshot():
    import pyautogui
    import datetime
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(filename)
    return f"Screenshot saved as {filename}"