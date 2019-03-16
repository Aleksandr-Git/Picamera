# делает серию снимков на длинной выдержке
# и сохраняет в папку по 1000 шт.

from picamera import PiCamera
from time import sleep
from fractions import Fraction
import datetime
from os import mkdir

n = 1

def INPUT_MIN(): #  ввод и проверка на корректность длительности съемки
    print('Длительность съемки в минутах')
    global MIN
    try:
        MIN = int(input())
     
    except ValueError:
        INPUT_MIN()

def INPUT_SLEEP(): #  ввод и проверка на корректность задержки
    print('Задержка между кадрами в секундах')
    global SLEEP
    try:
        SLEEP = int(input())
        
    except ValueError:
        INPUT_SLEEP()

INPUT_MIN()

INPUT_SLEEP()

RANGE = MIN * 60 / SLEEP

# Force sensor mode 3 (the long exposure mode), set
# the framerate to 1/6fps, the shutter speed to 6s,
# and ISO to 800 (for maximum gain)
camera = PiCamera(
    resolution=(1920, 1080),
    framerate=Fraction(1, 4),
    sensor_mode=3)
camera.shutter_speed = 4000000
camera.iso = 800
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)

for i in range(int(RANGE)):

    if (n-1) % 1000 == 0:
        today = datetime.datetime.today() #  создаем объект datatime
        DIR = today.strftime("%H_%M_%S %d-%m-%Y") #  записываем в переменную текущее время и дату
        mkdir(DIR)

    LEN_RANGE = len(str(int(RANGE)))
    h = '0' * LEN_RANGE
    #print(h)
    LEN_n = len(str(n))
    #print(t)
    y = h[0:(0-LEN_n)] + str(n)
        
    sleep(SLEEP)
    camera.exposure_mode = 'off'
# Finally, capture an image with a 6s exposure. Due
# to mode switching on the still port, this will take
# longer than 6 seconds
    camera.capture('./' + DIR + '/dark.' + y + '.jpg')
    n += 1
