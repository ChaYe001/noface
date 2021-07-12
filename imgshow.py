import os
from PIL import Image
import matplotlib.pyplot as plt
import time
facefile ='/home/gubo/234/'
piclist = os.listdir(facefile)
# facefile1 ='/home/gubo/WorkSpace/2.blu/Posface/littleface/'
# piclist1 = os.listdir(facefile1)


# plt.imshow(img)
for okname in piclist:
    img = Image.open(facefile + okname)
    name = okname.split('.')[0]
    print(name)
    plt.figure(figsize=(10, 10))
    plt.ion()  # 打开交互模式
    plt.axis('off')  # 不需要坐标轴
    plt.imshow(img)
    plt.pause(3)
    plt.clf()
    plt.close()
    time.sleep(0.5)
