import bpy

class GifExporterUI(bpy.types.Panel):
    bl_label = "Gif Exporter"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export gif:")

        props = context.scene.GifExporterPropertyGroup
        row = layout.row()
        row.prop(props, "output")
        row = layout.row()
        row.prop(props, "file_name")

        row = layout.row()
        row.operator("tool.export_gif", text="Export", icon="WORLD_DATA")
