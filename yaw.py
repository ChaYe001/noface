
import os

facefile = "/home/gubo/WorkSpace/face_yao/Posface/littleface/"


piclist = os.listdir(facefile)
# i = 0
for imagename in piclist:
    if imagename.endswith('jpg'):
        print(imagename)


        idname = imagename.split('.')[0]
        idname = imagename.split('_')[2]
        id = os.path.splitext(os.path.basename(idname))[0]
        print(id)
        blu = imagename.split('_')[0]
        blu = id + 'blu' + blu
        yaw = imagename.split('_')[1]
        yaw = id + 'yaw' + yaw

        newname = blu + '_' + yaw + '_' + idname
        os.renames(facefile + imagename, facefile + newname)
        # i = i + 1
        print(imagename)