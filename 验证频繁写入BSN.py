import os
import time
import random
def generate_random_str(randomlength=16):
  """
  生成一个指定长度的随机字符串
  """
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str
for i in range(100):
    random_str = generate_random_str(randomlength=11)
    os.system('adb shell input text G40'+ str(random_str) + '&& adb shell input keyevent 66')
    time.sleep(1)