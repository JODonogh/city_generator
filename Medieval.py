import bpy
import random
import bmesh

bpy.ops.object.mode_set(mode= 'OBJECT')
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()

# primitive addtions and object variation transforms    
def city_gen():
    
    bpy.ops.mesh.primitive_cube_add(size = 0.5, location = (local_x, local_y, 0), scale= (width, length, height))
    bpy.ops.transform.translate(value= (0, 0, height * 0.25), orient_matrix= ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    
def edit_mode():
    
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action = 'DESELECT')
    
def object_mode():
    
    bpy.ops.object.mode_set(mode = 'OBJECT')
    
def subdivide():
    
    bm = bmesh.from_edit_mesh(bpy.context.object.data) 
    bm.faces.ensure_lookup_table()
    bm.faces[5].select = True   
    bpy.ops.mesh.subdivide(number_cuts = 1)

def move_vertix():

    bm = bmesh.from_edit_mesh(bpy.context.object.data)        
    bm.verts.ensure_lookup_table()
    bm.verts[1].select = True
    bpy.ops.transform.translate(value= (0, 0, 1), constraint_axis=(False, False, True))

def random_vertex():
    
    bpy.ops.transform.vertex_random(offset =0.1)    
    
def rotate_face():   
    
    bm = bmesh.from_edit_mesh(bpy.context.object.data) 
    bm.faces.ensure_lookup_table()
    bm.faces[3].select = True
    bpy.ops.transform.rotate(value= 0.1, orient_axis = 'X') 
    bm.faces[1].select = True
    bpy.ops.transform.rotate(value= -0.1, orient_type= 'GLOBAL') 
    
def extrude_face(face, axis, constraint):   
    
    bm = bmesh.from_edit_mesh(bpy.context.object.data) 
    bm.faces.ensure_lookup_table()
    bm.faces[face].select = True   
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate = {"value": axis, "constraint_axis": constraint})
    
def move_faces():

    bpy.ops.mesh.select_all(action = 'DESELECT')
    bm = bmesh.from_edit_mesh(bpy.context.object.data)        
    bm.faces.ensure_lookup_table()
    bm.faces[6].select = True
    bpy.ops.transform.translate(value= (0, 0, 0.5))
    
def move_edge():

    bm = bmesh.from_edit_mesh(bpy.context.object.data)        
    bm.edges.ensure_lookup_table()
    bm.edges[0].select = True
    bpy.ops.transform.translate(value= (0, 1, 0))

def rotate_edge():

    bm = bmesh.from_edit_mesh(bpy.context.object.data)        
    bm.edges.ensure_lookup_table()
    bm.edges[1].select = True
    bpy.ops.transform.rotate(value= 0.11, orient_axis ='X')
    
def ground():
    
    bpy.ops.mesh.primitive_plane_add(size = 50, location = (0,0,0))
    bpy.context.object.name = "Ground"
    
if __name__=="__main__":
    
    for i in range(200):
        local_x = random.randrange(-20, 20)
        local_y = random.randrange(-20, 20)
        height = random.randrange(5, 10)
        width = random.randrange(1, 5)
        length = random.randrange(1, 5)
        
        city_gen()
        edit_mode()
        bpy.ops.mesh.select_mode(type ='FACE')
        extrude_face(5, (0, 0, 1), (False, False, True))
        object_mode()
        edit_mode()
        bpy.ops.mesh.select_mode(type ='FACE')
        extrude_face(8, (0, 1, 0), (False, True, False))
        extrude_face(9, (1, 0, 0), (True, False, False))
        #move_vertix()
        #subdivide()
        #rotate_face()
        #move_faces()
        #rotate_edge()
        object_mode()
        
    ground()