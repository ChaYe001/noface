
import codecs

f = codecs.open('data.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
lines = f.readlines()  # 以行的形式进行读取文件
list1 = []
for line in lines:

    str1 = 'Phase2 TimeMs:'
    if str1 in line:
        # print(line)
        a = line.split(str1)
        b = a[-1:]  # 这是选取需要读取的位数
        b = b[0].split(' ')[0]
        list1.append(float(b))  # 将其添加在列表之中

f.close()
print(list1)

