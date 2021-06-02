# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>



bl_info = {
    "name": "Mesh Wheel",
    "author": "Manoj_Narasimha",
    "version": (1, 0),
    "blender": (2, 90, 2),
    "Shortcuts": "V",
    "location": "View3D",
    "category": "3D view",
    "doc_url" : "https://gumroad.com/manojnarasimha"
}


import bpy
from bpy.types import Menu,Operator,Panel





class MESH_MT_wheel(Menu):
    # label is displayed at the center of the pie menu.
     bl_label = "Mesh Wheel"
     bl_idname= "PIE_MT_wheel"
     

     def draw(self, context):
         layout = self.layout
         #bpy.ops.preferences.keyitem_remove(item_id=119)
         

         pie = layout.menu_pie()
         
         pie.operator("cube.add")
         pie.operator("uvsphere.add")
         pie.operator("cylinder.add")
         pie.operator("plane.add")
         pie.operator("monkey.add")
         pie.operator("torus.add")
         pie.operator("cone.add")
         pie.operator("icosphere.add") 

class MESH_PT_wheel(Panel):
    
    bl_idname = "MESH_PT_panel"
    bl_label = "Mesh Wheel Documentation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Mesh Wheel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
       

        row = layout.row()
        layout.label(text="SHORTCUT KEY: 'V'")
        layout.operator("mesh.ops")
        layout.label(text="Instructions:")
        layout.label(text="1)Go to edit > Preferences > addons > Install")
        layout.label(text="2)Press V ")
        layout.label(text="Support me on my gumroad page by clicking on the follow button")
        layout.label(text="https://gumroad.com/manojnarasimha")

class MESH_OT_Operator(Operator):
    bl_label = "Run Mesh Wheel"
    bl_idname = "mesh.ops"
    
    def execute(self,context):
        bpy.ops.wm.call_menu_pie(name='PIE_MT_wheel')

        return{'FINISHED'}
    
class CUBE_OT_ADD(Operator):
    
    bl_label = "Cube"
    bl_idname= "cube.add"
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    
    def execute(self, context):
        
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True

        return{'FINISHED'}
    
    
class UV_SPHERE_OT_ADD(Operator):
    
    bl_label = "UV Sphere"
    bl_idname= "uvsphere.add"
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}
    
    
class CYLINDER_OT_ADD(Operator):
    
    bl_label = "Cylinder"
    bl_idname= "cylinder.add"
    
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        
        bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}    


class TORUS_OT_ADD(Operator):
    
    bl_label = "Torus"
    bl_idname= "torus.add"
    
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_torus_add(location=(0, 0, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}

class PLANE_OT_ADD(Operator):
    
    bl_label = "Plane"
    bl_idname= "plane.add"
    
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}

class MONKEY_OT_ADD(Operator):
    
    bl_label = "Monkey"
    bl_idname= "monkey.add"
    
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}
    
class CONE_OT_ADD(Operator):
    
    bl_label = "Cone"
    bl_idname= "cone.add"
    
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_cone_add(location=(0, 0, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}

class ICO_SPHERE_OT_ADD(Operator):
    
    bl_label = "Ico Sphere"
    bl_idname= "icosphere.add"
    
    
    #mode: bpy.props.StringProperty(name="Interactive mode", default="OBJECT")
    def execute(self, context):
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 1))
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True   
        return{'FINISHED'}             

        
addon_keymaps = []

def register():
    bpy.utils.register_class(MESH_MT_wheel)
    bpy.utils.register_class(MESH_PT_wheel)
    bpy.utils.register_class(CUBE_OT_ADD)
    bpy.utils.register_class(MESH_OT_Operator)  
    bpy.utils.register_class(ICO_SPHERE_OT_ADD)
    bpy.utils.register_class(CONE_OT_ADD)
    bpy.utils.register_class(MONKEY_OT_ADD)
    bpy.utils.register_class(PLANE_OT_ADD)
    bpy.utils.register_class(TORUS_OT_ADD)
    bpy.utils.register_class(CYLINDER_OT_ADD)
    bpy.utils.register_class(UV_SPHERE_OT_ADD)
    
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        
        km = kc.keymaps.new(name='OBJECT', space_type='VIEW_3D')
        kmi = km.keymap_items.new("mesh.ops", type="V", value='PRESS')
        addon_keymaps.append((km, kmi))   
  

def unregister():
        
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:    
       for km,kmi in addon_keymaps:
           km.keymap_items.remove(kmi)
           
       addon_keymaps.clear()
    
    
    bpy.utils.unregister_class(MESH_MT_wheel)
    bpy.utils.unregister_class(MESH_PT_wheel)
    bpy.utils.unregister_class(CUBE_OT_ADD)
    bpy.utils.unregister_class(MESH_OT_Operator)  
    bpy.utils.unregister_class(ICO_SPHERE_OT_ADD)
    bpy.utils.unregister_class(CONE_OT_ADD)
    bpy.utils.unregister_class(MONKEY_OT_ADD)
    bpy.utils.unregister_class(PLANE_OT_ADD)
    bpy.utils.unregister_class(TORUS_OT_ADD)
    bpy.utils.unregister_class(CYLINDER_OT_ADD)
    bpy.utils.unregister_class(UV_SPHERE_OT_ADD)
    

if __name__ == "__main__":
   register()
