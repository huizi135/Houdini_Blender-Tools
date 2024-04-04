bl_info = {
     "name" : "Send to Houdini",
     "version" : (1,0),
     "blender" : (4,0,0),
     "loation" : "View3D > Toolbar > Houdini",
     "description" : "sending the model to Houdini",
     "catergory" : "Houdini"
}

import bpy
import subprocess

class SimplePanel(bpy.types.Panel):
    bl_idname = "Houdini_panel"
    bl_category = "Houdini"
    bl_label = "Houdini Menu"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.send_houdini")
    
class SendToHoudini(bpy.types.Operator):
        bl_idname = "object.send_houdini"
        bl_label = "Send To Houdini"

        def execute(self, context):
            fbxPath = 'D:/Tools/temp_geo.fbx'
            bpy.ops.export_scene.fbx(filepath=fbxPath, global_scale=0.01)

            Houdinipath = 'C:/Program Files/Side Effects Software/Houdini 20.0.653/bin/houdini.exe'
            HoudiniScript = 'D:/Tools/import_hou_fbx.py'

            cmd = [Houdinipath, HoudiniScript]
            subprocess.Popen(cmd)

            return {'FINISHED'}



def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(SendToHoudini)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.register_class(SendToHoudini)

if __name__ == "__main__":
    register()