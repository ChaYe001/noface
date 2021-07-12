import os
import codecs
f = codecs.open('/home/gubo/newqr.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
str1 = '结果'
str2 = '0.8'
str3 = '结果：Rect'
str4 = 'QR score = 0.6'
str5 = 'QR score = 0.7'
str6 = 'QR score = 0.5'
str7 = 'QR score = 0.4'

str7 = 'QR score = 0.2'
jc = 0
jcc8 = 0
jcc7 = 0
jcc6 = 0
jcc5 = 0
jcc4 = 0
jcc3 = 0
jcc2 = 0
jx = 0
jxx = 0
jjj = 0
line = f.readlines()  # 以行的形式进行读取文件
for i in range(len(line)):

    d = line[i].split('检测')
    d1 = line[i].split('QR score = ')
    if d1[-1].find(',(') != -1:
        b = d1[-1]
        if int(b[2:3]) <= 6 and int(b[2:3]) > 0:
            # print(b[0:4])
            jjj += 1
    # print(d[-1].find((str1)))
    if d[-1].find(str1) != -1:
        jc += 1
    if d1[-1].find(',(') != -1:
        a = d1[-1]
    if d[-1].find(str3) != -1:
        jx += 1
        if int(a[2:3]) <=8 and int(a[0:1]) < 1 and int(a[3:4]) <= 9:
            print(a[0:4])
            jxx =+ 1

    if d1[-1].find('1.0',0,5) != -1:
        jcc8 += 1
    if d1[-1].find('0.9',0,5) != -1:
        jcc8 += 1

    if d1[-1].find('0.8',0,5) != -1:
        jcc8 += 1
    if d1[-1].find('0.7',0,5) != -1:
        jcc7 += 1
    if d1[-1].find('0.6',0,5) != -1:
        jcc6 += 1
    if d1[-1].find('0.5',0,5) != -1:
        jcc5 += 1
    if d1[-1].find('0.4',0,5) != -1:
        jcc4 += 1
    if d1[-1].find('0.3',0,5) != -1:
        jcc3 += 1
print(jjj/jx)
print('检出率8:' + str(jcc8/jc) + ' 检出率7:' + str((jcc8+jcc7)/jc) + ' 检出率6:' + str((jcc8+jcc7+jcc6)/jc) + ' 检出率5:' + str((jcc8+jcc7+jcc6+jcc5)/jc) + ' 检出率4:' + str((jcc8+jcc7+jcc6+jcc5+jcc4)/jc) + ' 识别率：' + str(jx/jc))
    # jcc8 = d.find(str2)
    # jcc8 = d.find(str2)
    # jcc8 = d.find(str2)
    # jcc8 = d.find(str2)