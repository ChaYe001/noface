import os
import codecs
facefile = "/home/gubo/1/1/caiji/8888/yuv/"
successfile = "/home/gubo/1/1/caiji/0000/jpg/清楚/"
successfile1 = "/home/gubo/8/buqingchu/"
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)

f = codecs.open('data.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readlines()  # 以行的形式进行读取文件
for i in range(len(line)):

    d = line[i].split('-1.jpg')
    c = d[0].split('_')
    #print(d[0])
    for okname in piclist:
        if okname.endswith('yuv'):
            a = okname.split('.')
            if c[-1] == a[0]:
                os.rename(facefile + okname ,facefile + d[0] + '.yuv')




