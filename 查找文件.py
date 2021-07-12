import os
import codecs


def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')

        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        #os.system('rm -r ' + str(path))
        return False


facefile = "/home/gubo/WorkSpace/prnet/误检测/1/"
# successfile = "/home/gubo/2/caiji2/bujujiao/mohu/"
# successfile1 = "/home/gubo/8/buqingchu/"
piclist = os.listdir(facefile)
# successlist = os.listdir(successfile)

f = codecs.open('data.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readlines()  # 以行的形式进行读取文件
for i in range(len(line)):

    d = line[i].split()
    # print(d[0])
    # mkdir(facefile + d[0])
    for okname in piclist:
        if okname.endswith('.jpg'):
            # print(okname[5:18])
            # a = okname.split('.jpg')
            # #c = a[0].split('_')
            # print(d[5:19])
            if d[0] == okname[0:18]:
                print(d[0])
                #os.system('rm '+ facefile + okname)
                # abc = mkdir(facefile + d[0])
                #print(abc)
                os.system('mv ' + facefile + okname + ' ' + facefile + '2/' + okname)