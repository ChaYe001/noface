import os
import cv2
facefile = "/home/gubo/Downloads/jpg/"
# successfile = "/home/gubo/2/caiji2/bujujiao/mohu/"
# successfile1 = "/home/gubo/8/buqingchu/"
filelist = os.listdir(facefile)
filelist.sort(key=lambda x:x)
print(filelist)
for filename in filelist:
    print(filename)
    piclist = os.listdir(facefile + filename + '/')
    if len(piclist) >=2:
        print(len(piclist))
        i = 0
        for okname in piclist:

            a = facefile + filename + '/' + okname
            #print(a)
            img = cv2.imread(facefile + filename + '/' + okname)
            cv2.namedWindow(okname,80)

            #print(int(i/5))
            cv2.moveWindow(okname, 400*(i%5), int(i/5)*400)
            cv2.imshow(okname,img)
            i += 1


        cv2.waitKey(0)
        cv2.destroyAllWindows()
        a = os.system('rm -r ' + facefile + filename)
        #print(len(filelist))