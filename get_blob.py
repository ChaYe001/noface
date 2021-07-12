#!/usr/bin/env python3
import os
import sys
modelfile = "/media/gubo/DATADRIVE0/work/testLLvisionCompilemodel/model/"
# successfile = "/home/gubo/2/caiji2/bujujiao/mohu/"
# successfile1 = "/home/gubo/8/buqingchu/"
# modellist = os.listdir(modelfile)



for root, dirs, files in os.walk(modelfile):
    # print(root)
    #
    # print(dirs)
    #
    # print(files)
#         return files
#
# root, dirs,files = file_name(modelfile)
    for file in files:
        # print(file)
        if file.endswith('blob'):
            # print(root[0:53], root[58:-4], file)
            if os.path.isdir(root[0:53] + 'opensource' + root[58:-4]):
                pass
            else:
                os.makedirs(root[0:53] + 'opensource' + root[58:-4])
            os.system('cp ' + root + '/' + file + ' ' + root[0:53] + 'opensource' + root[58:-4] + file)
# modellist.sort(key=lambda x:x)
# print(modellist)
# for filename in filelist:
#     print(filename)
#     piclist = os.listdir(facefile + filename + '/')
#     if len(piclist) >=2:
#         print(len(piclist))
#         i = 0
#         for okname in piclist:
#
#             a = facefile + filename + '/' + okname
#             #print(a)
#             img = cv2.imread(facefile + filename + '/' + okname)
#             cv2.namedWindow(okname,80)
#
#             #print(int(i/5))
#             cv2.moveWindow(okname, 400*(i%5), int(i/5)*400)
#             cv2.imshow(okname,img)
#             i += 1
#
#
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#         a = os.system('rm -r ' + facefile + filename)
        #print(len(filelist))