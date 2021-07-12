import os
import cv2
facefile ='/home/gubo/Downloads/test/'
piclist = os.listdir(facefile)
facefile1 ='/home/gubo/批量识别/gubo0_816_478/1/'
piclist1 = os.listdir(facefile1)


#i = 0
for okname in piclist:
    if okname.endswith('png'):
        img = cv2.imread(facefile + okname)
        # sp = img.shape
        # if sp[0]>=720:

        os.system('mv ' + facefile + okname + ' ' + facefile + okname + '.jpg')
    # for okname1 in piclist1:

            # if okname1 == okname:
            #     os.system('mv '+ facefile1 + okname1 + ' '+ '/home/gubo/1/' + okname1)
            #     os.system('mv ' + facefile + okname + ' ' + '/home/gubo/2/' + okname)
    # # if okname.endswith('jpg'):
    # print(okname)
    # newname = (("{:0>5d}".format(i)) + '.jpg')
    # i = i+1
    # os.rename(facefile + okname, facefile + newname)
    # print(newname)

# i = 0
# for i in range(1,6001):
#     print(("{:0>5d}".format(i))+'\n')