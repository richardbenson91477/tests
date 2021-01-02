import bpy
import math

bpy.ops.mesh.primitive_emptyvert_add()
bpy.ops.mesh.delete(type='VERT')
#bpy.ops.object.editmode_toggle()

s = []
for x in range(10):
    s += [bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False,
        location=(x, 0, math.sin(x/10 * 6.28)))]

print(s)
