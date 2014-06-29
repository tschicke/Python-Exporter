import os
clear = lambda: os.system('cls')


import bpy

mesh = bpy.data.objects['Cube'].data

def printFunc():
    bpy.ops.object.mode_set(mode='OBJECT')
    clear()
    mesh.calc_tessface()
    
    vertices = []
    UVs = []
    normals = []
    
    outVertices = []
    outUVs = []
    outNormals = []
    outIndices = []
    
    tris = 0
    
    triangulatedIndices = []
    
    #Triangulate faces
    for face in mesh.tessfaces:
        if(len(face.vertices) == 3):
            triangulatedIndices.append(face.vertices[:])
            uvArray = mesh.tessface_uv_textures.active.data[face.index]
            UVs.append(uvArray.uv[0][:])
            UVs.append(uvArray.uv[1][:])
            UVs.append(uvArray.uv[2][:])
        else:
            triangulatedIndices.append((face.vertices[0], face.vertices[1], face.vertices[2]))
            triangulatedIndices.append((face.vertices[2], face.vertices[3], face.vertices[0]))
            uvArray = mesh.tessface_uv_textures.active.data[face.index]
            UVs.append(uvArray.uv[0][:])
            UVs.append(uvArray.uv[1][:])
            UVs.append(uvArray.uv[2][:])
            UVs.append(uvArray.uv[3][:])
    
    #Print face vertices (temp)
    for tri in triangulatedIndices:
        tris += 1
        print(tri)
            
    print("Number of tris: %i" % tris)
    
    #Populate vertices and normals arrays
    for v in mesh.vertices:
        vertices.append(v.co)
        normals.append(v.normal)
    
    print("%i %i %i" % (len(vertices), len(UVs), len(normals)))
    
    for v in vertices:
        print("v %.6f %.6f %.6f" % (v[0], v[1], v[2]))
    
    for uv in UVs:
        print("t %.6f %.6f" % (uv[0], uv[1]))
    
    for n in normals:
        print("n %.6f %.6f %.6f" % (n[0], n[1], n[2]))
    
printFunc()
'''
clear()
mesh.calc_tessface()
#print(dir(mesh.tessface_uv_textures.active.data[0].uv[0][0]))
print(len(mesh.tessface_uv_textures.active.data))
print(len(mesh.uv_layers.active.data))
#print(mesh.tessface_uv_textures.active.data[0].uv[7][0])

for face in mesh.tessface_uv_textures.active.data:
    for vertex in face.uv:
        print(vertex[:])
    print()
'''
