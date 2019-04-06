# копирует файлы из одной папки в другую
# проверяет обе папки на наичие всех скопированных файлов
# если проверка прошлая, удаляет первую папку
# если нет, копирует недостающие файла и т.д.

import os
import shutil
import time

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

while True:
    total_size = 0
    if fun(path_origin) > 30:
        copy(last_pap())
       
#copy(last_pap())



