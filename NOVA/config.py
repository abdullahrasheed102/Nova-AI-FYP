"""Shared, platform-independent project paths for Nova AI."""

import os

NOVA_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(NOVA_DIR)

MEMORY_DIR = os.path.join(PROJECT_ROOT, "Memory")
MUSIC_DIR = os.path.join(PROJECT_ROOT, "Music")
PLAYLIST_DIR = os.path.join(PROJECT_ROOT, "Playlist")
WALLPAPER_DIR = os.path.join(PROJECT_ROOT, "Wallpapers")
QURAN_DIR = os.path.join(PROJECT_ROOT, "Quran_Majeed")
GUI_DIR = os.path.join(NOVA_DIR, "GUI")
DATA_DIR = os.path.join(NOVA_DIR, "Data")
SOUND_DIR = os.path.join(DATA_DIR, "SoundEffects")
