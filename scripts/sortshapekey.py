import bpy
import bmesh


bl_info = {
    "name" : "SortShapekeyPlugin",
    "author" : "lowteq",
    "version" : (0,1),
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


    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.context.active_object
        src = obj
        #bpy.ops.object.shape_key_move(type='UP')

        #bpy.context.object.active_shape_key_index = 0
        
        shapekeynamelist = []
        
        if obj.data.shape_keys == None:
            bpy.ops.object.shape_key_add(from_mix=False)

        for i in range(1, len(src.data.shape_keys.key_blocks)): # skip basis
            src_key = src.data.shape_keys.key_blocks[i]
            print(src_key.name)
            shapekeynamelist.append(src_key.name)
        
        
        sortedlist = sorted(shapekeynamelist,key=str.lower)
        for sortedindex,name in enumerate(sortedlist):
            srcshapekeyindex = src.data.shape_keys.key_blocks.find(name)
            bpy.context.object.active_shape_key_index = srcshapekeyindex
            
            sortedindex += 1
            if sortedindex > srcshapekeyindex:
                opstype = "DOWN"
            else:
                opstype = "UP"
            
            prognum = abs(srcshapekeyindex - sortedindex)
            for i in range(prognum):
                bpy.ops.object.shape_key_move(type=opstype)
            

            
            
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_sort_shapekey.bl_idname,text="Sort Shapekey")

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