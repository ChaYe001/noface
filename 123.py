
import os

facefile = "/home/gubo/WorkSpace/littleface/"
successfile = "/home/gubo/WorkSpace/face_yao/Posface/success/"

piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
# i = 0
for imagename in piclist:
    if imagename.endswith('jpg'):
        print(imagename)
    # for imagename in piclist:
    #     if imagename.endswith('jpg'):
    #         print(imagename)

        # if imagename == okname:
        #     os.system('rm ' + facefile + okname)
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