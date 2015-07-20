import bpy

def save(operator, context, filepath=""):
    bpy.ops.object.mode_set(mode='OBJECT')
    for object in bpy.data.objects:
        if(object.type != 'MESH'):
            continue
        mesh = object.data
        mesh.calc_tessface()
        
        vertices = []
        UVs = []
        normals = []
        
        indices = []
        
        indexOffset = 0
        for face in mesh.tessfaces:
            tempIndices = []
            for i in range(0, len(face.vertices)):
                index = face.vertices[i]
                blenderVertex = mesh.vertices[index].co[:]
                outVertex = (blenderVertex[0], blenderVertex[2], -blenderVertex[1])
                UV = mesh.tessface_uv_textures.active.data[face.index].uv[i][:]
                if face.use_smooth:
                    normal = mesh.vertices[index].normal[:]
                else:
                    normal = face.normal[:]
                
                dupIndex = -1
                for j in range(0, len(vertices)):
                    tempVert = vertices[j]
                    tempUV = UVs[j]
                    tempNormal = normals[j]
                    
                    if outVertex == tempVert and UV == tempUV and normal == tempNormal:
                        #Duplicate Found
                        dupIndex = j
                        break
                if dupIndex != -1:
                    #Duplicate Found
                    print("dup")
                    tempIndices.append(dupIndex)
                else:
                    vertices.append(outVertex)
                    UVs.append(UV)
                    normals.append(normal)
                    tempIndices.append(indexOffset)
                    indexOffset += 1
                
            if len(tempIndices) == 4:
                indices.append((tempIndices[0], tempIndices[3], tempIndices[2]))
                indices.append((tempIndices[0], tempIndices[2], tempIndices[1]))
            else:
                indices.append((tempIndices[0], tempIndices[2], tempIndices[1]))
            
        file = open(filepath, 'w')
        fw = file.write
        fw("gmdl\n")
        fw("%i %i\n" % (len(vertices), len(indices) * 3))
        fw("1\n")#This is whether or not the mesh is textured
        
        for v in vertices:
            fw("v %f %f %f\n" % v[:])
        
        for uv in UVs:
            fw("t %f %f\n" % uv[:])
            
        for n in normals:
            fw("n %f %f %f\n" % n[:])
        
        for i in indices:
            fw("i %i %i %i\n" % i[:])
        
        file.close
    
    return {'FINISHED'}