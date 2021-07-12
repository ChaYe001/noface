#!/usr/bin/env python3
import time
import os
from multiprocessing import Process
def task(n):
    print('子进程的PID：%s' %os.getpid())


def mytest(n):
    os.system('../G26X/LLvisionCompile/bin/myriad_compile -m /home/gubo/WorkSpace/G26X/LLvisionCompile/MOBILENET_CCPD_LPD_iter_105000.xml -VPU_PLATFORM VPU_2480')
    print('5')
if __name__ == '__main__':

    p = Process(target=mytest,args=('子进程',))
    p.start()