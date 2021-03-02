import bpy

class GifExporterPropertyGroup(bpy.types.PropertyGroup):
    output: bpy.props.StringProperty(name="Output", subtype="FILE_PATH")
    file_name: bpy.props.StringProperty(name="File Name")
