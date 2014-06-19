import bpy

def save(operator, context, filepath=""):
    bpy.ops.object.mode_set(mode='OBJECT')
    for object in bpy.data.objects:
        if(object.type != 'MESH'):
            continue
        mesh = object.data
        mesh.calc_tessface()
        
        vertexList = mesh.vertices
        uvList = mesh.uv_layers.active.data
        indexList = mesh.tessfaces
        
        writeVertexList = vertexList
        writeUVList = uvList
        writeNormalList = []
        writeIndexList = []
        
        for i in indexList:
            if(len(i.vertices) == 3):
                writeIndexList.append(i.vertices[:])
            else:
                writeIndexList.append((i.vertices[0], i.vertices[1], i.vertices[2]))
                writeIndexList.append((i.vertices[2], i.vertices[3], i.vertices[0]))
        
        file = open(filepath, 'w')
        fw = file.write
        fw("gmdl\n")
        fw("%i %i\n" % (len(vertexList), len(writeIndexList) * 3))
        
        for v in vertexList:
            fw("v %.4f %.4f %.4f\n" % v.co[:])
        
        for d in uvList:
            fw("t %.4f %.4f\n" % d.uv[:])
            
        for v in vertexList:
            fw("n %.4f %.4f %.4f\n" % v.normal[:])
            
        for i in writeIndexList:
            fw("i %i %i %i\n" % i)
        
        file.close
    
    return {'FINISHED'}