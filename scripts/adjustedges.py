bl_info = {
    "name": "Adjust edge length",
    "author": "lowteq",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "3DView > ContextMenu ",
    "description": "Adjust selected edge length to average length",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

import bpy
from bpy_extras import object_utils
from bmesh import from_edit_mesh
import bmesh

def get_selected_edges(obj,bm):

  selected_edges = [e for e in bm.edges if e.select]
  print(len(selected_edges))
  return selected_edges

def get_edge_lengths(edges):
  edge_lengths = []
  for edge in edges:
    v1 = edge.verts[0].co
    v2 = edge.verts[1].co
    length = (v1 - v2).length
    edge_lengths.append(length)
  return edge_lengths

def adjust_edge_length(edges, target_length):
  for edge in edges:
    v1 = edge.verts[0].co
    v2 = edge.verts[1].co
    length = (v1 - v2).length

    a = v1 - v2
    a.normalize()

    new_v1 = v1 + a* ((target_length-length)/2)
    new_v2 = v2 - a* ((target_length-length)/2)

    edge.verts[0].co = new_v1
    edge.verts[1].co = new_v2

class AdjustEdgeLength(bpy.types.Operator):
    bl_idname = "mesh.adjust_edge_length"
    bl_label = "Adjust edge length"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        bm = bmesh.from_edit_mesh(obj.data)
        # 選択された辺を取得
        selected_edges = get_selected_edges(obj,bm)

        # 選択された辺が1本以上ある場合は実行可能
        return len(selected_edges) > 0

    def execute(self,context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)
        # 選択された辺を取得
        selected_edges = get_selected_edges(obj,bm)

        # 選択された辺の長さのリストを作成
        edge_lengths = get_edge_lengths(selected_edges)

        # 選択された辺の長さの平均を求める
        avg_length = sum(edge_lengths) / len(edge_lengths)

        # 選択された辺の長さを揃える
        adjust_edge_length(selected_edges, avg_length)

        # bmeshを更新
        bmesh.update_edit_mesh(obj.data)
        
        return {'FINISHED'}
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(AdjustEdgeLength.bl_idname)

def register():
    bpy.utils.register_class(AdjustEdgeLength)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_fn)
def unregister():
    bpy.utils.unregister_class(AdjustEdgeLength)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_fn)

if __name__ == "__main__":
    register()