# !!!написать автоматическое создание папок


from time import sleep
from picamera import PiCamera

#print('Число кадров')
#RANGE = int(input())
print('Длительность съемки в минутах')
MIN = int(input())

print('Задержка между кадрами в секундах')
SLEEP = int(input())

print('Название файла')
FILE = input()

RANGE = MIN * 60 / SLEEP

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
    camera.capture(FILE + '.' + y + '.jpg')
    n += 1
