# проверяет наличие новых писем
# проверяяет новое письмо на соответствие
# открывает новый поток и выполняет необходимую команду из письма
# если оттправить письмо тема:zero, тель:Фото, то в ответ прийдет письмо с фото

from imaplib import IMAP4_SSL
import email.message
import base64
import os
import time
import threading

SENDER = 'gavryukov@mail.ru'  # отправитель
#TEMA = '=?UTF-8?B?0KHQstGP0LfRjA==?='  # Связь
TEMA = '=?UTF-8?B?emVybw==?='  # zero
UID = ''
last_uid = ''

M = IMAP4_SSL('imap.mail.ru')
M.login('ffgg-1981@mail.ru', 'Asdf210781')
msgs = M.select('inbox')  # подключаемся к папке входящие. пример ('OK', [b'8'])


def UID_new_email():  # выполняет проверку наличия новых писем
    global UID, last_uid

    if len(UID) == 0:
        with open('/home/flash/test/Picamera/Command_mail/UID_email.txt', 'r') as file:  # открываем файл для чтения
            for line in file:  # читаем строку
                UID = line

    typ_message_uid, list_message_uid = M.uid('search', None, 'ALL')  # получаем список UID писем
    # print(list_message_uid)

    last_uid = list_message_uid[0].split()[-1]  # определяем UID последнего письма
    # print(last_uid)

    if last_uid.decode() != UID:  # если UID последнего письма не равен UID из файла
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
                if 'Фото' in base64.b64decode(i).decode() or 'фото' in base64.b64decode(i).decode():  # если команда присутсвует в теле письма
                    # print('Команда распознана')
                    with open('/home/flash/test/Picamera/Command_mail/UID_email.txt', 'w') as file:
                        file.write(UID)  # записываем новый UID в файл, в котором хранится последний UID
#                    return threading.Thread(target=os.system, args=('C:/Windows/system32/calc',)).start()  # открывает новый поток и выполняет команду
                    return threading.Thread(target=os.system, args=('sudo python3 /home/flash/test/Picamera/Command_mail/Photo_send.py',)).start()  # открывает новый поток и выполняет команду
                    break

            except Exception:
                continue


while True:
    try:
        time.sleep(5)  # задержка программы на 5 секунд

        if UID_new_email() != False:  # если есть новое письмо
            new_email(last_uid)

    except Exception:
        continue
