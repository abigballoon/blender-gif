import bpy
import math
import os

from .ui import GifExporterUI
from ._operator import GifExporter
from .props import GifExporterPropertyGroup

bl_info = {
    "name": "Gif Exporter",
    "blender": (2, 83, 0),
    "location": "View3D",
    "category": "Tool",
    "version": (1, 0, 0),
}

classes = (GifExporterUI, GifExporter, GifExporterPropertyGroup)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.GifExporterPropertyGroup = bpy.props.PointerProperty(type=GifExporterPropertyGroup)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.GifExporterPropertyGroup

if __name__ == "__main__":
    register()