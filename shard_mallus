import bpy
import random

def clean():
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)
        
def create_cube(width, height, length):
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.resize(value=(width, height, length))
    bpy.ops.transform.translate(value = (0, 0, height*0.2))
    return bpy.context.object

def create_plane():
    bpy.ops.mesh.primitive_plane_add(size= 50)
    bpy.context.object.name= "Ground"
    
def subdivide(obj, name, levels):   
    subdiv= obj.modifiers.new(type = "SUBSURF", name = name) 
    subdiv.levels = levels
        
def displace(obj, name):
    dsplace = obj.modifiers.new(type="DISPLACE", name=name)
    texture = voronoi(intensity, scale)

def voronoi(intensity, scale):
    texture = bpy.data.textures.new("voronoi", type="VORONOI")
    texture.distance_metric="DISTANCE_SQUARED"
    texture.noise_intensity = intensity
    texture.noise_scale = scale

def decimate(obj, name, ratio):
    modifier= obj.modifiers.new(type="DECIMATE", name=name)
    modifier.ratio=ratio


def get_vert_offset(vertex, scale):
    direction = vertex.normal
    
    direction[0] += random.uniform(-0.5, 0.5)
    direction[1] += random.uniform(-0.5, 0.5)
    direction[2] += random.uniform(-0.5, 0.5)
    
    return direction * scale
     
def offset_verts(obj):
     for vertex in obj.data.vertices:
         vertex.co += get_vert_offset(vertex, 2)


def collapse_modifiers(cube):
    for modifier in cube.modifiers:
        bpy.ops.object.modifier_apply(modifier=modifier.name)  

clean()
create_plane()
gap = 5

width= random.uniform(0.5, 5)
height= random.uniform(0.5, 5)
length= random.uniform(0.5, 1)

intensity = random.uniform(0.4, 1)
scale = random.uniform(0.4, 1)

level = 3.5

cube= create_cube(width, height, length)
subdivide(cube, 'subdivide', levels = level)
displace(cube, 'displace')
decimate(cube, 'decimate', 0.03)
 
offset_verts(cube)    
collapse_modifiers(cube) 
        
for r in range(4):
    width= random.uniform(0.1, 1)
    height= random.uniform(0.1, 1)
    length= random.uniform(0.1, 1)
    
    x_between = width * r * gap
    y_between = height * r * gap
    
    cube= create_cube(width, height, length)
    bpy.ops.transform.translate(value = (x_between, y_between, 0))
    
    subdivide(cube, 'subdivide', levels = level)
    displace(cube, 'displace')
    decimate(cube, 'decimate', 0.03)

    offset_verts(cube)    
    collapse_modifiers(cube) 
    
    x_pos = random.uniform(-15, 15)
    y_pos = random.uniform(-15, 15)
    
    bpy.ops.transform.translate(value=(x_pos, y_pos, 0))   
