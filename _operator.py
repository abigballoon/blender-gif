import bpy
import math
import os
import shutil

from mathutils import Vector
from ._wrapper import images2video, video2gif
from .settings import get_temp_dir, FFMPEG_PATH

class GifExporter(bpy.types.Operator):
    """Export animation to gif"""
    bl_idname = "tool.export_gif"
    bl_label = "Export gif"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        props = scene.GifExporterPropertyGroup
        dir_path = props.output
        prefix = props.file_name
        fp = bpy.data.filepath
        file_dir, filename = os.path.split(fp)

        if not prefix:
            prefix = ".".join(filename.split(".")[: -1])

        framerate = scene.render.fps

        temp_dir = get_temp_dir()
        original_path = scene.render.filepath
        scene.render.filepath = temp_dir
        bpy.ops.render.render(animation=True)

        images2video(temp_dir, framerate)
        video2gif(temp_dir, os.path.join(fp, dir_path, "%s.gif" % prefix))

        # clean up
        scene.render.filepath = original_path

        # remove temp files
        shutil.rmtree(temp_dir)

        self.report({"INFO"}, "Export completed")
        return {"FINISHED"}
