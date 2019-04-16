# !!!! разобраться с неточностью обще длительности при съемке

# автоматически создает папку
# в качестве названия применяется текущая дата и время
# делает серию фото и сораняет в созданную папку по 10

from time import sleep
from picamera import PiCamera
import os
import datetime
import shutil
import time

n = 1

path_origin = './pap_2'
path_copy = '/mnt/yandex_disk/pap_3'

total_size = 0
os.system('sudo mount -a')
time.sleep(10)

print(os.listdir(path_origin))

def test_copy(path_1, path_2):
    for i in os.listdir(path_1):
        if i in os.listdir(path_2):
            print(i)
            continue
        else:
            return False
    return True

def copy(folder):
    try:
        os.makedirs(path_copy+'/'+folder)
    except FileExistsError:
        pass

    for i in os.listdir(folder):
            shutil.copyfile(folder+'/'+i, path_copy+'/'+folder+'/'+i)
    
    if test_copy(folder, path_copy+'/'+folder):
            try:
                shutil.rmtree(folder)
            except PermissionError:
                pass

    else:
        copy(folder)

def last_pap():
    dir_list = [os.path.join(path_origin, x) for x in os.listdir(path_origin)]
    print(dir_list)
    if dir_list:
    # Создадим список из путей к файлам и дат их создания.
        date_list = [[x, os.path.getctime(x)] for x in dir_list]
  
    # Отсортируем список по дате создания в прямом порядке
        sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=False)

        return sort_date_list[0][0]

def fun(path):   # определяет размер папки
    global total_size
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):

            fun(path + '/' + i)

        else:
            s = os.path.getsize(path + '/' + i)
            total_size += s
    return total_size / 1024 / 1024

print(last_pap())

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
        os.mkdir('./pap_2/'+DIR)
        os.chmod('./pap_2/'+DIR, 0o777)
        print('test_1')

    LEN_RANGE = len(str(int(RANGE)))
    h = '0' * LEN_RANGE
    #print(h)
    LEN_n = len(str(n))
    #print(t)
    y = h[0:(0-LEN_n)] + str(n)

    print('test_2')
    sleep(SLEEP) #  задержка
    print('test_3')
    camera.capture('./pap_2/' + DIR + '/photo.' + y + '.jpg')
    n += 1

    print('test_4')
    total_size = 0
    if fun(path_origin) > 30:
        print('copy')
        copy(last_pap())
        print('end_copy')
