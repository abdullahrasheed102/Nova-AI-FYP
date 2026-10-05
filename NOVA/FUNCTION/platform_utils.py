"""Runtime adapters for the Windows and Ubuntu desktop environments."""

import os
import shlex
import subprocess
import sys
import webbrowser
from pathlib import Path

IS_WINDOWS = sys.platform.startswith("win")
IS_LINUX = sys.platform.startswith("linux")

WINDOWS_LAUNCHERS = {
    "my computer": "explorer",
    "notepad": "notepad",
    "chrome": "chrome",
    "paint": "mspaint",
    "calculator": "calc",
    "email": "start outlook:",
    "command prompt": "cmd",
    "terminal": "start cmd",
    "task manager": "taskmgr",
    "control panel": "control",
    "file explorer": "explorer",
    "settings": "ms-settings:",
    "system info": "systeminfo",
    "device manager": "devmgmt.msc",
    "word": "winword",
    "excel": "excel",
    "vs code": "code",
    "powerpoint": "powerpnt",
    "recycle bin": "explorer.exe shell:RecycleBinFolder",
    "download": os.path.expanduser("~/Downloads"),
    "updates": "chrome://settings/help",
    "gmail": "https://mail.google.com",
    "map": "https://www.google.com/maps",
    "drive": "https://drive.google.com",
    "calender": "https://calendar.google.com",
}

LINUX_LAUNCHERS = {
    "my computer": "nautilus",
    "files": "nautilus",
    "file explorer": "nautilus",
    "file manager": "nautilus",
    "notepad": "gedit",
    "chrome": "google-chrome",
    "paint": "pinta",
    "calculator": "gnome-calculator",
    "email": "thunderbird",
    "command prompt": "gnome-terminal",
    "terminal": "gnome-terminal",
    "task manager": "gnome-system-monitor",
    "control panel": "gnome-control-center",
    "settings": "gnome-control-center",
    "system info": "gnome-system-monitor",
    "device manager": "gnome-control-center",
    "word": "libreoffice --writer",
    "excel": "libreoffice --calc",
    "vs code": "code",
    "powerpoint": "libreoffice --impress",
    "recycle bin": "xdg-open trash:///",
    "download": os.path.expanduser("~/Downloads"),
    "updates": "https://www.google.com/chrome/",
    "gmail": "https://mail.google.com",
    "map": "https://www.google.com/maps",
    "drive": "https://drive.google.com",
    "calender": "https://calendar.google.com",
}

APP_NAMES = tuple(dict.fromkeys((*WINDOWS_LAUNCHERS, *LINUX_LAUNCHERS)))


def _warn_optional(label, exc):
    if IS_LINUX:
        print(f"{label} unavailable on Linux; continuing: {exc}")


try:
    import pygetwindow as _pygetwindow  # noqa: F401
except Exception as exc:
    _pygetwindow = None
    _warn_optional("pygetwindow", exc)

try:
    import pywifi as _pywifi  # noqa: F401
except Exception as exc:
    _pywifi = None
    _warn_optional("pywifi", exc)

try:
    import screen_brightness_control as _brightness_control
except Exception as exc:
    _brightness_control = None
    _warn_optional("Screen brightness control", exc)


def get_brightness():
    if _brightness_control is None:
        return []
    try:
        return _brightness_control.get_brightness()
    except Exception as exc:
        _warn_optional("Screen brightness control", exc)
        return []


def set_brightness(value, display=None):
    if _brightness_control is None:
        return False
    try:
        _brightness_control.set_brightness(value, display=display)
        return True
    except Exception as exc:
        _warn_optional("Screen brightness control", exc)
        return False


def create_tts_engine():
    import pyttsx3

    if IS_WINDOWS:
        return pyttsx3.init("sapi5")
    return pyttsx3.init()


def start_rainmeter(path):
    if IS_WINDOWS and os.path.isfile(path):
        open_path(path)
        return True
    print("Rainmeter unavailable; skipping Rainmeter startup")
    return False


def get_active_window_title():
    if _pygetwindow is None:
        raise RuntimeError("pygetwindow is unavailable")
    return _pygetwindow.getActiveWindowTitle()


def open_path(path):
    path = os.fspath(path)
    if IS_WINDOWS:
        os.startfile(path)
    elif IS_LINUX:
        subprocess.Popen(["xdg-open", path])
    else:
        webbrowser.open(path)


def open_app(name):
    launchers = WINDOWS_LAUNCHERS if IS_WINDOWS else LINUX_LAUNCHERS
    command = launchers.get(name, name)
    if name == "download":
        return open_path(command)
    if isinstance(command, str) and (
        command.startswith("https://")
        or command.startswith("http://")
        or command.startswith("chrome://")
    ):
        return webbrowser.open(command)
    if IS_WINDOWS:
        subprocess.Popen(["cmd", "/c", command], shell=False)
    elif IS_LINUX:
        subprocess.Popen(shlex.split(command))
    else:
        webbrowser.open(command)


def kill_app(name):
    if IS_WINDOWS:
        command = ["taskkill", "/f", "/im", os.fspath(name)]
    elif IS_LINUX:
        linux_name = {"msedge.exe": "microsoft-edge", "chrome.exe": "chrome"}.get(
            os.fspath(name), os.fspath(name)
        )
        command = ["pkill", "-f", linux_name]
    else:
        return
    subprocess.run(command, check=False)


def power_action(action):
    if IS_WINDOWS:
        commands = {
            "shutdown": ["shutdown", "/s", "/t", "5"],
            "restart": ["shutdown", "/r", "/t", "5"],
            "logout": ["shutdown", "/l"],
            "sleep": ["rundll32", "powrprof.dll,SetSuspendState", "0,1,0"],
        }
    else:
        commands = {
            "shutdown": ["systemctl", "poweroff"],
            "restart": ["systemctl", "reboot"],
            "logout": ["gnome-session-quit", "--logout", "--no-prompt"],
            "sleep": ["systemctl", "suspend"],
        }
    if action not in commands:
        raise ValueError(f"Unsupported power action: {action}")
    try:
        subprocess.run(commands[action], check=False)
    except OSError as exc:
        print(f"Power action '{action}' is unavailable: {exc}")


def set_wallpaper(path):
    if IS_WINDOWS:
        import ctypes

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.fspath(path), 3)
    elif IS_LINUX:
        uri = Path(path).resolve().as_uri()
        for setting in ("picture-uri", "picture-uri-dark"):
            try:
                subprocess.run(
                    ["gsettings", "set", "org.gnome.desktop.background", setting, uri],
                    check=False,
                )
            except OSError as exc:
                print(f"Unable to set wallpaper: {exc}")


def scroll(amount):
    if IS_WINDOWS:
        import ctypes

        ctypes.windll.user32.mouse_event(0x0800, 0, 0, int(amount) * 40, 0)
    elif IS_LINUX:
        import pyautogui

        pyautogui.scroll(amount)


def press_enter():
    if IS_WINDOWS:
        import ctypes

        ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0x0D, 0, 0x0002, 0)
    elif IS_LINUX:
        import pyautogui

        pyautogui.press("enter")


def hotkey(*keys):
    if IS_WINDOWS:
        import keyboard

        key_names = ["windows" if key == "win" else key for key in keys]
        keyboard.press_and_release(" + ".join(key_names))
    elif IS_LINUX:
        import pyautogui

        pyautogui.hotkey(*keys)


def press_key(key, presses=1, interval=0):
    if IS_WINDOWS:
        import keyboard

        for index in range(presses):
            keyboard.press(key)
            keyboard.release(key)
            if interval and index + 1 < presses:
                import time

                time.sleep(interval)
    elif IS_LINUX:
        import pyautogui

        pyautogui.press(key, presses=presses, interval=interval)


def play_sound(path):
    if not os.path.isfile(path):
        print(f"Sound file unavailable; skipping playback: {os.path.basename(path)}")
        return
    if IS_WINDOWS:
        try:
            from playsound import playsound
        except Exception as exc:
            print(f"playsound unavailable: {exc}")
            return
        playsound(os.fspath(path))
    elif IS_LINUX:
        import pygame

        pygame.mixer.init()
        pygame.mixer.music.load(os.fspath(path))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
