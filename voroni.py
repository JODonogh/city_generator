import bpy
import math

def clean_scene():
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)
        
def create_cube():
    bpy.ops.mesh.primitive_cube_add(size=1)
    return bpy.context.object

def apply_modifier(name):
    bpy.ops.object.modifier_apply(modifier=name)
    
def check_apply(apply, name):
    if apply:
        apply_modifier(name)

def subdivide(obj, name, levels=5, apply=True):
    # subdivide modifier elements
    subdiv_modifier= obj.modifiers.new(type='SUBSURF', name=name)
    subdiv_modifier.levels = levels
    check_apply(apply, subdiv_modifier.name)
            
def spherify(obj, name, apply= True):
    # spherify cube
    cast_modifier= obj.modifiers.new(type='CAST', name=name)
    check_apply(apply, cast_modifier.name)
        
def decimate(obj, degrees, name, apply=True):
    # Decimate cube
    decimate_modifier= obj.modifiers.new(type='DECIMATE', name=name)
    decimate_modifier.decimate_type ='DISSOLVE'
    decimate_modifier.use_dissolve_boundaries = True
    decimate_modifier.angle_limit= math.radians(degrees)
    check_apply(apply, decimate_modifier.name)
        
def create_cool_sphere():
    # cube creation
    cube = create_cube()
    
    subdivide(cube, 'subdiv_cube')
    spherify(cube, 'cast_cube')
    decimate(cube, 20, 'decimate_cube')
        
clean_scene()
create_cool_sphere()
