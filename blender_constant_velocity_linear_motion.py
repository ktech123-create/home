import bpy

# physical calculation for Constant velocity linear motion
velocity = 20 

position1 = []
position2 = []
position3 = []
 
for t in range(0, 100):
    # velocity 20
    x1 = velocity * t 
    position1.append((x1,0,0))
    # velocity 10
    x2 = velocity / 2 * t
    position2.append((x2,0,0))
    # velocity 5
    x3 = velocity / 4 * t
    position3.append((x3,0,0))

# delete all registered objects
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)
   
for material in bpy.data.materials:
   bpy.data.materials.remove(material)

# define material color for each object
material_red = bpy.data.materials.new('red')
material_red.diffuse_color = (1.0, 0.0, 0.0, 1.0)

material_green = bpy.data.materials.new('green')
material_green.diffuse_color = (0.0, 1.0, 0.0, 1.0)

material_blue = bpy.data.materials.new('blue')
material_blue.diffuse_color = (0.0, 0.0, 1.0, 1.0)

# define sphere and object name
bpy.ops.mesh.primitive_uv_sphere_add(radius=5)
bpy.context.object.name = 'sphere_red'

bpy.ops.mesh.primitive_uv_sphere_add(radius=5)
bpy.context.object.name = 'sphere_green'

bpy.ops.mesh.primitive_uv_sphere_add(radius=5)
bpy.context.object.name = 'sphere_blue'

# apply color for each objects
ob_red = bpy.data.objects['sphere_red']
ob_red.data.materials.append(material_red)

ob_green = bpy.data.objects['sphere_green']
ob_green.data.materials.append(material_green)

ob_blue = bpy.data.objects['sphere_blue']
ob_blue.data.materials.append(material_blue)

# start frame
frame_num = 0

for p in position1:
    # set start frame
    bpy.context.scene.frame_set(frame_num)
    # move location
    ob_red.location = p
    # insert frame
    ob_red.keyframe_insert(data_path = "location",index = -1)
    # add frame
    frame_num += 10
    
# start frame
frame_num = 0

for p in position2:
    # set start frame
    bpy.context.scene.frame_set(frame_num)
    # move location
    ob_green.location = p
    # insert frame
    ob_green.keyframe_insert(data_path = "location",index = -1)
    # add frame
    frame_num += 10

# start frame
frame_num = 0

for p in position3:
    # set start frame
    bpy.context.scene.frame_set(frame_num)
    # move location
    ob_blue.location = p
    # insert frame
    ob_blue.keyframe_insert(data_path = "location",index = -1)
    # add frame
    frame_num += 10
