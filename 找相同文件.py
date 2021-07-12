import os
import codecs
facefile = "/home/gubo/樣本/车牌/误检测/0.92/"
successfile = "/home/gubo/樣本/车牌/误检测/jpg/"
successfile1 = "/home/gubo/樣本/车牌/误检测/"
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)


for okname in piclist:
    if okname.endswith('-1.jpg'):
        a = okname.split('-1.jpg')
        #c = a[0] + '.yuv'
        #print(c)
        #os.system('mv ' + facefile + okname + ' ' + successfile + a[0] + '.yuv')
        for name in successlist:
            if name.endswith('.jpg'):
                #d = name.split('_')
                e = name.split('.jpg')
                #print(e[0])

                if a[0] == e[0]:
                    #print(1)
                    #os.system('rm '+ facefile + okname)
                    os.system('mv ' + successfile + name + ' ' + successfile1 + name)