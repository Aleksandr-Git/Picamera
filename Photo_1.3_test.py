# !!!! разобраться с неточностью обще длительности при съемке

# автоматически создает папку
# в качестве названия применяется текущая дата и время
# делает серию фото и сораняет в созданную папку по 10

from time import sleep
from picamera import PiCamera
from os import mkdir
from os import chmod
import datetime

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

camera = PiCamera()
#camera.resolution = (1024, 768)
#camera.start_preview()
# камера разминается
#sleep(1)
#camera.capture('foo_1.jpg')
camera.resolution = (1920,1080)

for i in range(int(RANGE)):
    #camera.resolution = (640,480)
    #camera.iso = i  # максимум 800
    #camera.shutter_speed = 40000  # максимум 40000
    #camera.start_preview()

    if (n-1) % 10 == 0:
        today = datetime.datetime.today()  # создаем объект datatime
        DIR = today.strftime("%H_%M_%S_%d-%m-%Y")  # записываем в переменную текущее время и дату
        mkdir('./pap_2/'+DIR)
        chmod('./pap_2/'+DIR, 0o777)

    LEN_RANGE = len(str(int(RANGE)))
    h = '0' * LEN_RANGE
    #print(h)
    LEN_n = len(str(n))
    #print(t)
    y = h[0:(0-LEN_n)] + str(n)
    
    sleep(SLEEP) #  задержка
    camera.capture('./pap_2/' + DIR + '/photo.' + y + '.jpg')
    n += 1
