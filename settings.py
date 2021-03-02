import os
import json
import tempfile
import random
from sys import platform

TEMP_DIR_NAME = 'blender-gif-exporter'

def r():
    pop = "abcdefghijklmnopqrstuvwxyz1234567890"
    s = ""
    for _ in range(6):
        s += random.choice(pop)
    return s

def get_temp_dir():
    path = os.path.join(tempfile.gettempdir(), TEMP_DIR_NAME, r(), "")
    if not os.path.exists(path):
        os.makedirs(path)
    return path

BASE = os.path.dirname(__file__)

if platform == "linux" or platform == "linux2":
    FFMPEG_PATH = os.path.join(BASE, "ffmpeg", "linux", "ffmpeg")
elif platform == "darwin":
    FFMPEG_PATH = os.path.join(BASE, "ffmpeg", "mac", "ffmpeg")
elif platform == "win32":
    FFMPEG_PATH = os.path.join(BASE, "ffmpeg", "windows", "ffmpeg.exe")

print("FFMPEG_PATH:", FFMPEG_PATH)