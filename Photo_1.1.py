# !!!! разобраться с неточностью обще длительности при съемке
# сделать сохранение по 1000 фоток в папке

# автоматически создает папку
# в качестве названия применяется текущая дата и время
# делает серию фото и сораняет в созданную папку

from time import sleep
from picamera import PiCamera
from os import mkdir
import datetime

def INPUT_MIN(): #  ввод и проверка на корректность длительности съемки
    print('Длительность съемки в минутах')
    try:
        MIN = int(input())
        global MIN

    except ValueError:
        INPUT_MIN()

def INPUT_SLEEP(): #  ввод и проверка на корректность задержки
    print('Задержка между кадрами в секундах')
    try:
        SLEEP = int(input())
        global SLEEP

    except ValueError:
        INPUT_SLEEP()


INPUT_MIN()

INPUT_SLEEP()

today = datetime.datetime.today() #  создаем объект datatime
DIR = today.strftime("%H_%M_%S %d-%m-%Y") #  записываем в переменную текущее время и дату

RANGE = MIN * 60 / SLEEP

mkdir(DIR)

camera = PiCamera()
#camera.resolution = (1024, 768)
#camera.start_preview()
# камера разминается
#sleep(1)
#camera.capture('foo_1.jpg')
n = 1
camera.resolution = (1920,1080)

for i in range(int(RANGE)):
    #camera.resolution = (640,480)
    #camera.iso = i  # максимум 800
    #camera.shutter_speed = 40000  # максимум 40000
    #camera.start_preview()

    LEN_RANGE = len(str(int(RANGE)))
    h = '0' * LEN_RANGE
    #print(h)
    LEN_n = len(str(n))
    #print(t)
    y = h[0:(0-LEN_n)] + str(n)
# камера разминается    
    sleep(SLEEP)
    #camera.capture(FILE + '.' + str(n) + '.jpg')
    camera.capture('./' + DIR + '/photo.' + y + '.jpg')
    n += 1
