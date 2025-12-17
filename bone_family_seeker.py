## 1024pm 12/16/25 - made to help me understand rigacar add-on
bl_info = {
    "name": "Bone Parenting Status Displayer",
    "description": "Shows expanded parenting info of selected bone",
    "author": "Lancine Doumbia",
    "version": (1, 0, 0),
    "blender": (2, 9, 0),
    "location": "View3D",
    "warning": "",
    "wiki_url": "",
    "category": "Armature" }
    
import bpy

class ShowBoneInfo(bpy.types.Panel):
    bl_idname = "panel.show_bone_info"
    bl_label = "Show Parenting Info"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def poll(self, context):
        return context.object and context.object.mode == 'EDIT'
    
    def draw(self, context):
        layout = self.layout

         ### design your panel here ###
        bone = context.object.data.edit_bones.active

        if bone.parent:
            layout.label(text=f"Parent: {bone.parent.name}")
            
        if bone.children:
            layout.label(text=f"Children of {bone.name}:")
            #show children already added
            box = layout.box()
            for child in bone.children:
                box.label(text=f"{child.name}")

def register():
    bpy.utils.register_class(ShowBoneInfo)

def unregister():
    bpy.utils.unregister_class(ShowBoneInfo)

if __name__ == "__main__":
    register()
