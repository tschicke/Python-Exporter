import os
clear = lambda: os.system('cls')


import bpy

mesh = bpy.data.objects['Cube'].data

def printFunc():
    clear()
    mesh.calc_tessface()
    
    tris = 0
    
    indexList = []
    
    for face in mesh.tessfaces:
        if(len(face.vertices) == 3):
            indexList.append(face.vertices[:])
        else:
            indexList.append((face.vertices[0], face.vertices[1], face.vertices[2]))
            indexList.append((face.vertices[2], face.vertices[3], face.vertices[0]))
    
    for tri in indexList:
        tris += 1
        print(tri)
            
    print("Number of tris: %i" % tris)
    
    
printFunc()