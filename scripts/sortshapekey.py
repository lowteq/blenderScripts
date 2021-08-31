import bpy
import bmesh
from bpy.props import BoolProperty
bl_info = {
    "name" : "SortShapekeyPlugin",
    "author" : "lowteq",
    "version" : (0,2),
    "blender" : (2,80, 0),
    "location" : "View3D > Object",
    "description" : "Sort shapekeys",
    "warning" : "",
    "wiki_url" : "https://github.com/lowteq/blenderScripts",
    "tracker_url" : "",
    "category" : "Object"
}


class OBJECT_OT_sort_shapekey(bpy.types.Operator):

    bl_idname = "object.sort_shapekey"
    bl_label = "Sort_Shapekey"
    bl_description = "Sort shapekeys"
    bl_options = {'REGISTER', 'UNDO'}


    reverse : BoolProperty(
        default=False,
        options = {'HIDDEN'}
    )
    
    

    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.context.active_object
        src = obj

        if obj.data.shape_keys == None:
            bpy.ops.object.shape_key_add(from_mix=False)

        shapekeynamelist = [src_key.name for src_key in src.data.shape_keys.key_blocks[1:]] # skip basis
        
        sortedlist = sorted(shapekeynamelist,key=str.lower,reverse=self.reverse)

        for index,name in enumerate(sortedlist):
            src_key_ix = src.data.shape_keys.key_blocks.find(name)
            dst_key_ix = index + 1

            #move shapekey at src_key_ix to dst_key_ix
            bpy.context.object.active_shape_key_index = src_key_ix
            if dst_key_ix > src_key_ix:
                opstype = "DOWN"
            else:
                opstype = "UP"

            for i in range(abs(src_key_ix - dst_key_ix)):
                bpy.ops.object.shape_key_move(type=opstype)


        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.separator()
    asc = self.layout.operator(OBJECT_OT_sort_shapekey.bl_idname,text="Sort Shapekey")
    asc.reverse = False
    desc = self.layout.operator(OBJECT_OT_sort_shapekey.bl_idname,text="Sort Shapekey reverse")
    desc.reverse = True
    

classes = [
    OBJECT_OT_sort_shapekey,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.MESH_MT_shape_key_context_menu.append(menu_func)


def unregister():
    bpy.types.MESH_MT_shape_key_context_menu.remove(menu_func)
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()