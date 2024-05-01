import bpy
import random
import bmesh
 
def subdivide():
    
    bm = bmesh.from_edit_mesh(bpy.context.object.data) 
    bm.faces.ensure_lookup_table()
    bm.faces[5].select = True   
    bpy.ops.mesh.subdivide(number_cuts = 1)   
  
def edit_mode():
    
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action = 'DESELECT')
    
def object_mode():
    
    bpy.ops.object.mode_set(mode = 'OBJECT')
    
class Edges():
    def rotate_edge(index, angle):

        bm = bmesh.from_edit_mesh(bpy.context.object.data)        
        bm.edges.ensure_lookup_table()
        bm.edges[index].select = True
        bpy.ops.transform.rotate(value= angle, orient_axis ='X', orient_type='LOCAL', constraint_axis=(True, False, False))

    def move_edge(index, height):

        bm = bmesh.from_edit_mesh(bpy.context.object.data)        
        bm.edges.ensure_lookup_table()
        bm.edges[index].select = True
        bpy.ops.transform.translate(value= (0, 0, height), orient_type= 'LOCAL')  
        
#creating and transforming plank
def create_house(height, thickness, angle):
    bpy.ops.mesh.primitive_cube_add(size= 1, location =(-150, 160,00))
    bpy.ops.transform.resize(value= (thickness, length, height), orient_type='LOCAL')
    bpy.ops.transform.translate(value= (1,1, 15), orient_matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    bpy.ops.transform.rotate(value=-0.1, orient_axis='Z')

           
gap = 5
    
for p in range(9):
    thickness= random.randrange(4, 5)
    height = random.uniform(5, 10.5)
    length = random.randrange(4, 5)
    angle = random.uniform(-0.1, 0.1)


    create_house(height, thickness, angle)
    bpy.ops.transform.translate(value= (0, (gap)*p, 0))
    
    edit_mode()
    subdivide()
    object_mode()
    edit_mode()
    Edges.move_edge(16, 1)
    object_mode()
    edit_mode()
    Edges.move_edge(17, 1)
    object_mode()
