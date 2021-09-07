import bpy
from bpy.props import IntProperty, FloatProperty
from bpy.props import EnumProperty, FloatVectorProperty
from bpy.props import BoolProperty


def pivotpointchange(pivotpoint):
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].pivot_point = pivotpoint


def currentpivotpoint():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            return area.spaces[0].pivot_point


def get_override(area_type, region_type):
    for area in bpy.context.screen.areas: 
        if area.type == area_type:             
            for region in area.regions:                 
                if region.type == region_type:                    
                    override = {'area': area, 'region': region} 
                    return override
    #error message if the area or region wasn't found
    raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                        "\n Make sure it's open while executing script.")



bl_info = {
    "name": "FaceEXShapekey",
    "author": "lowteq",
    "version": (1, 1),
    "blender": (2, 78, 0),
    "location": "3D View > Mesh",
    "description": "Create extra shapekeys for faces",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "https://github.com/lowteq",
    "category": "Mesh"
}


class FaceEXShapekey(bpy.types.Operator):

    bl_idname = "object.faceexshapekey"
    bl_label = "Face EX Shapekey"
    bl_description = "Create extra shapekeys for faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        scene = context.scene
        
        duplicateFlag = scene.faceexshapekey_prop_duplicateFlag
        innerOffset = scene.faceexshapekey_prop_innerOffset
        innerScale = scene.faceexshapekey_prop_innerScale

        surfOffset = scene.faceexshapekey_prop_surfOffset
        surfScale = scene.faceexshapekey_prop_surfScale

       
        transformOffset = (-innerOffset[0] + surfOffset[0], -innerOffset[1] + surfOffset[1], -innerOffset[2] + surfOffset[2])

            
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.context.active_object
        obj.active_shape_key_index = 0

        bpy.ops.object.mode_set(mode='EDIT')

        if duplicateFlag:
            bpy.ops.mesh.duplicate()
            

        override = get_override("VIEW_3D","WINDOW")
        pivotPointTemp = currentpivotpoint()
        pivotpointchange('INDIVIDUAL_ORIGINS')

        bpy.ops.transform.translate(value=innerOffset, constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED')
        bpy.ops.transform.resize(override,value=(innerScale, innerScale, innerScale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED')

        bpy.ops.object.mode_set(mode='OBJECT')
        exshapekey = obj.shape_key_add(name="Ex",from_mix=False)
        index = len(obj.data.shape_keys.key_blocks) - 1
        bpy.context.object.active_shape_key_index = index

        bpy.ops.object.mode_set(mode='EDIT')
        
        obj.data.shape_keys.key_blocks[exshapekey.name].value = 1

        bpy.ops.transform.resize(override,value=(1/innerScale, 1/innerScale, 1/innerScale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED')
        bpy.ops.transform.translate(value=transformOffset, constraint_orientation='GLOBAL', mirror=True, proportional='DISABLED')
        bpy.ops.transform.resize(override,value=(surfScale, surfScale, surfScale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=True, proportional='DISABLED')

        obj.data.shape_keys.key_blocks[exshapekey.name].value = 0

        pivotpointchange(pivotPointTemp)

        
        return {'FINISHED'}


class VIEW3D_PT_CustomMenu(bpy.types.Panel):

    bl_label = "FaceEXShapekey"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "FaceEXShapekey"
    bl_context = "mesh_edit"

    @classmethod
    def poll(cls, context):
        return True


    def draw_header(self, context):
        layout = self.layout
        layout.label(text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "faceexshapekey_prop_duplicateFlag")
        layout.prop(scene, "faceexshapekey_prop_innerOffset")
        layout.prop(scene, "faceexshapekey_prop_innerScale")
        layout.separator()
        layout.prop(scene, "faceexshapekey_prop_surfOffset")
        layout.prop(scene, "faceexshapekey_prop_surfScale")
        layout.separator()
        layout.operator(FaceEXShapekey.bl_idname, text="create")
        


def menu_fn_1(self, context):
    self.layout.separator()
    self.layout.operator(FaceEXShapekey.bl_idname, text="FaceEXShapekey")

def init_props():
    scene = bpy.types.Scene
    scene.faceexshapekey_prop_innerOffset = FloatVectorProperty(
        name="innerOffset",
        description="Float Vector Property",
        subtype='TRANSLATION',
        default=(0.0, 0.05, 0.0)
    )
    scene.faceexshapekey_prop_innerScale = FloatProperty(
        name="innerScale",
        description="Float Property",
        default=0.5,
        min=0.001,
        max=1.0
    )
    scene.faceexshapekey_prop_surfOffset = FloatVectorProperty(
        name="surfOffset",
        description="Float Vector Property",
        subtype='TRANSLATION',
        default=(0.0, -0.001, 0.0)
    )
    scene.faceexshapekey_prop_surfScale = FloatProperty(
        name="surfScale",
        description="Float Property",
        default=1.0,
        min=0.0
    )
    scene.faceexshapekey_prop_duplicateFlag = BoolProperty(
        name="duplicate", default=True)
    

def clear_props():
    scene = bpy.types.Scene
    del scene.faceexshapekey_prop_innerOffset
    del scene.faceexshapekey_prop_innerScale
    del scene.faceexshapekey_prop_surfOffset
    del scene.faceexshapekey_prop_surfScale
    del scene.faceexshapekey_prop_duplicateFlag
    

def register():
    bpy.utils.register_module(__name__)
    init_props()
    bpy.types.VIEW3D_MT_object.append(menu_fn_1)



def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn_1)
    clear_props()
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

































