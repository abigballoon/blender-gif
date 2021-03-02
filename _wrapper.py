import os
import subprocess
from .settings import FFMPEG_PATH

def cmd(command):
    print("Executing:", command)
    proc = subprocess.check_call(command)

def images2video(dir_path, framerate):
    command = "%s -y -framerate %d -i %s -codec copy %s" % (FFMPEG_PATH, framerate,
            os.path.join(dir_path, "%04d.png"),
            os.path.join(dir_path, "output.mkv"))
    cmd(command)

def video2gif(input_path, output_path):
    command = "%s -y -i %s -loop 0 %s" % (FFMPEG_PATH, os.path.join(input_path, "output.mkv"), output_path)
    cmd(command)
