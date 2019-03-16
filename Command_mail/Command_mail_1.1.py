# работает
# !!!!!!!!терминал не понимает относительные пути к файлу
# проверяет наличие новых писем
# проверяет новое письмо на соответствие
# если письмо прошло проверку, камера делает фото и отправляет фото
# если отправить письмо тема:Малина, тело:Фото, то в ответ прийдет письмо с фото

from imaplib import IMAP4_SSL
import email.message
import base64
import os
import time
import threading

from io import BytesIO
#from time import sleep
from picamera import PiCamera
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#stream = BytesIO()  # создаем объект для записи потока 
camera = PiCamera()
camera.resolution = (320, 240)

#msg = MIMEMultipart()  # создаем контейнер для мультиформатного сообщения
#attachment = MIMEBase('image', "jpeg")  # создаес объект класса MIMEBase и передве

SENDER = 'gavryukov@mail.ru'  # отправитель
#TEMA = '=?UTF-8?B?0KHQstGP0LfRjA==?='  # Связь
#TEMA = '=?UTF-8?B?emVybw==?='  # zero
TEMA = '=?UTF-8?B?0JzQsNC70LjQvdCw?='  # Малина
UID = ''
last_uid = ''

M = IMAP4_SSL('imap.mail.ru')
M.login('ffgg-1981@mail.ru', 'Asdf210781')
msgs = M.select('inbox')  # подключаемся к папке входящие. пример ('OK', [b'8'])

def photo():  # возвращает фото в формате jpg в бинарном виде
    stream = BytesIO()  # создаем 'буфер'
    camera.capture(stream, 'jpeg')  # сохраняем изображение в поток

#    view = stream.getbuffer()
#    print(len(view))

    buff_img = stream.getvalue()  # записываем содержимое буфера в переменную
#    print('фото сделано')
    return buff_img

#with open('./image_test_4.jpg', 'wb') as file:
#    file.write(photo())

def send_mail(data):
    msg = MIMEMultipart()
    attachment = MIMEBase('image', "jpeg")
    header = 'Content-Disposition', 'attachment; filename = "Test.jpg"'  # записываем в переменную заголовки

    attachment.set_payload(data)  # добавляем файл в байтах в объект MIMEBase
    #print(attachment)
    encoders.encode_base64(attachment)  # кодируем в base64
    #print(attachment)
    attachment.add_header(*header)  # добавляем поле заголовка и содержимое заголовка
#    print(attachment)
#    print(header)
    msg.attach(attachment)  # добавляем объект MIMEBase в контейнер для мультиформатного сообщения MIMEMultipart
#    print(attachment)
#    print('письмо собрано')
    #print(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    #Send the mail
    #msg = MIMEText('\n Тук-тук, проснись Нео, ты увяз в Матрице!'.encode('utf-8'), _charset='utf-8')
    server.starttls()
    server.login('vasaisvanov@gmail.com','Asdf210781')
    server.sendmail("vasaisvanov@gmail.com", "gavryukov@mail.ru", msg.as_string())
    
    server.quit()
#    print('письмо отпрвлено')

def UID_new_email():  # выполняет проверку наличия новых писем
    global UID, last_uid

    if len(UID) == 0:
#        with open('./UID_email.txt', 'r') as file:  # открываем файл для чтения
        with open('/home/flash/test/Picamera/Command_mail/UID_email.txt', 'r') as file:   
            for line in file:  # читаем строку
                UID = line

    typ_message_uid, list_message_uid = M.uid('search', None, 'ALL')  # получаем список UID писем
    # print(list_message_uid)

    last_uid = list_message_uid[0].split()[-1]  # определяем UID последнего письма
    # print(last_uid)

    if last_uid.decode() != UID and UID != 'error' and last_uid != b'error':  # если UID последнего письма не равен UID из файла
#        print(last_uid.decode(), UID)
        return last_uid  # возвращаем последний UID письма

    else:
#        print('Новых писем нет')
        return False


def new_email(last_uid):  # выполняет проверку письма на соответствие
    global UID

    UID = last_uid.decode()  # присваиваем новый UID
    typ_data_uid, message_data_uid = M.uid('fetch', last_uid,
                                           '(RFC822)')  # получаем все разделы письма в байтах в виде списка через UID
    msg_full_uid = email.message_from_bytes(message_data_uid[0][1])  # преобразуем байты в строки
    # print(typ_data_uid)
    # print(message_data_uid)
    FROM = msg_full_uid.get_all('FROM')  # записываем данные из раздела FROM в переменную FROM
    SUBJECT = msg_full_uid.get('SUBJECT')  # записываем данные из раздела SUBJECT в переменную SUBJECT
    # msg_full.add_header('Test', 'ON')
    # TEST = msg_full.get('Test')

    if SENDER in FROM[0] and SUBJECT == TEMA:  # если отправитель и тема совпадают

#        print('Есть новое письмо!', last_uid)
        # print(M.uid('fetch', last_uid, '(UID BODY[TEXT])'))
        raw_body = M.uid('fetch', last_uid, '(UID BODY[TEXT])')  # запрашиваем сырое тело письма
        body = raw_body[1][0][1].decode().split('\r\n')  # тело письма, разбитое на строки в список
        # print(body)

        for i in body:
            # print(i)

            try:
                # j = base64.b64decode(i).decode()
#                print(base64.b64decode(i).decode())
#                print('пробуем проверить команду')
                if 'Фото' in base64.b64decode(i).decode() or 'фото' in base64.b64decode(i).decode():  # если команда присутсвует в теле письма
                    # print('Команда распознана')
#                    with open('./UID_email.txt', 'w') as file:
#                    print('проверили команду')
                    with open('/home/flash/test/Picamera/Command_mail/UID_email.txt', 'w') as file: 
                        file.write(UID)  # записываем новый UID в файл, в котором хранится последний UID
#                    print('записали число в файл')
#                    return threading.Thread(target=os.system, args=('C:/Windows/system32/calc',)).start()  # открывает новый поток и выполняет команду
#                    return threading.Thread(target=os.system, args=('sudo python3 /home/flash/test/Picamera/Command_mail/Photo_send.py',)).start()  # открывает новый поток и выполняет команду
#                    return threading.Thread(target=send_mail, args=(photo(),)).start()
#                    print('попытка отправить письмо')
                    return send_mail(photo())
                    break

            except Exception:
#                print('ошибка в new_email или send_mail')
                continue


while True:
    try:
        time.sleep(5)  # задержка программы на 5 секунд

        if UID_new_email() != False:  # если есть новое письмо
            new_email(last_uid)

    except Exception:
        M = IMAP4_SSL('imap.mail.ru')
        M.login('ffgg-1981@mail.ru', 'Asdf210781')
        msgs = M.select('inbox')
        continue
