import os
import re

print('Начальный номер')
START = int(input())
#PATH = r'\\raspberrypi\test\picamera\06_04_28_24-04-2018'
PATH = r'C:\Users\Алиса\Desktop\Склейка видео\19_14_02 21-04-2018'
PATH_RMN = r'C:\Users\Алиса\Desktop\Склейка видео\RNM_photo'
#SHABLON = r'(photo\.)(\d\d\d)(\.jpg)'
SHABLON = r'(dark\.)(\d\d\d)(\.jpg)'
# список файлов в исходной папке
LIST_FILE = os.listdir(PATH)

for i in LIST_FILE:
    result = re.findall(SHABLON, i)
    n = int(result[0][1]) + START
    NEW_NAME = 'photo.' + str(n) + result[0][2]
    #NEW_NAME = result[0][0] + str(n) + result[0][2]
    #print(NEW_NAME)
    #print(i)
    with open(PATH + '\\' + i, 'rb') as f_1:
        h_1 = f_1.read()

    with open(PATH_RMN + '\\' + NEW_NAME, 'wb') as f_2:
        f_2.write(h_1)
