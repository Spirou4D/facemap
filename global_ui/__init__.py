# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2023 Steven Garcia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

import bpy

from bpy.types import (
        PropertyGroup,
        Panel
        )

from bpy.props import (
        IntProperty,
        BoolProperty,
        EnumProperty,
        PointerProperty,
        CollectionProperty
        )

from .region_ui import (
    Halo_RegionsPanel,
    Halo_OT_RegionMove,
    Halo_OT_RegionRemove,
    Halo_OT_RegionAdd,
    REGION_UL_List,
    RegionItem,
    Halo_OT_RegionAssign,
    Halo_OT_RegionRemoveFrom,
    Halo_OT_RegionSelect,
    Halo_OT_RegionDeselect,
    Halo_OT_RegionRemoveUnused,
    REGION_MT_context_menu,
    region_add,
    get_custom_attribute
)


classeshalo = (
    Halo_RegionsPanel,
    Halo_OT_RegionMove,
    Halo_OT_RegionRemove,
    Halo_OT_RegionAdd,
    REGION_UL_List,
    RegionItem,
    Halo_OT_RegionAssign,
    Halo_OT_RegionRemoveFrom,
    Halo_OT_RegionSelect,
    Halo_OT_RegionDeselect,
    Halo_OT_RegionRemoveUnused,
    REGION_MT_context_menu
    )
    
def register():
    for clshalo in classeshalo:
        bpy.utils.register_class(clshalo)
    bpy.types.Object.region_list = CollectionProperty(type = RegionItem)
    bpy.types.Object.active_region = IntProperty(name = "Active region index", description="Active index in the region array", default = -1)
    bpy.types.Scene.active_region_list = []
    bpy.types.Object.region_add = region_add
    bpy.types.Mesh.get_custom_attribute = get_custom_attribute
        
def unregister():
    del bpy.types.Object.region_list
    del bpy.types.Object.active_region
    del bpy.types.Scene.active_region_list
    del bpy.types.Object.region_add
    del bpy.types.Mesh.get_custom_attribute
    for clshalo in classeshalo:
        bpy.utils.unregister_class(clshalo)

if __name__ == '__main__':
    register()
