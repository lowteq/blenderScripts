# Blender内部のデータ構造にアクセスするために必要
import bpy
import bmesh


bl_info = {
    "name" : "AsymmetrizeShapekeyPlugin",
    "author" : "lowteq",
    "version" : (0,1),
    "blender" : (2,78, 0),
    "location" : "View3D > Object",
    "description" : "Duplicate symmetric shapekey into asymmetric shapekeys",
    "warning" : "",
    "wiki_url" : "https://github.com/lowteq/blenderScripts",
    "tracker_url" : "",
    "category" : "Object"
}


class OBJECT_asymmetrize_shapekey(bpy.types.Operator):

    bl_idname = "object.asymmetrize_shapekey"
    bl_label = "Asymmetrize_Shapekey"
    bl_description = "Duplicate symmetric shapekey into asymmetric shapekeys"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.context.active_object

        src_shapekey_name = obj.active_shape_key.name
        src_shapekey_index = obj.active_shape_key_index

        obj.shape_key_add(name=src_shapekey_name + "_R", from_mix=True)
        shape_r_index = len(obj.data.shape_keys.key_blocks) - 1
        obj.shape_key_add(name=src_shapekey_name + "_L", from_mix=True)
        shape_l_index = len(obj.data.shape_keys.key_blocks) - 1

        bpy.ops.object.mode_set(mode='EDIT')
        index = obj.active_shape_key_index
        mesh = bmesh.from_edit_mesh(obj.data)
        bpy.ops.mesh.select_all(action="DESELECT")

        for v in mesh.verts:
            if v.co.x > 0:
                v.select = True
            else:
                v.select = False
        bpy.context.object.active_shape_key_index = shape_l_index
        bpy.ops.mesh.blend_from_shape(shape=src_shapekey_name, blend=1)

        bpy.ops.mesh.select_all(action="DESELECT")
        mesh = bmesh.from_edit_mesh(obj.data)

        for v in mesh.verts:
            if v.co.x < 0:
                v.select = True
            else:
                v.select = False

        bpy.context.object.active_shape_key_index = shape_r_index
        bpy.ops.mesh.blend_from_shape(shape=src_shapekey_name, blend=1)

        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_asymmetrize_shapekey.bl_idname,text="Asymmetrize Shapekey")


def register():
    bpy.utils.register_module(__name__)
    bpy.types.MESH_MT_shape_key_specials.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.MESH_MT_shape_key_specials.remove(menu_func)


if __name__ == "__main__":
    register()