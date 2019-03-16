# отправляет письмо с вложением

#import os
import smtplib
#import sys
#from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#from email.utils import formatdate

msg = MIMEMultipart()  # создаем контейнер для мультиформатного сообщения
attachment = MIMEBase('image', "jpeg")  # создаес объект класса MIMEBase и передвем тип - картинка с расширением jpg

with open('./id93120.jpg', 'rb') as file:  # читаем файл в байтах
    data = file.read()

#print(data)

header = 'Content-Disposition', 'attachment; filename = "Test.jpg"'  # записываем в переменную заголовки

attachment.set_payload(data)  # добавляем файл в байтах в объект MIMEBase
#print(attachment)
encoders.encode_base64(attachment)  # кодируем в base64
#print(attachment)
attachment.add_header(*header)  # добавляем поле заголовка и содержимое заголовка
print(attachment)
msg.attach(attachment)  # добавляем объект MIMEBase в контейнер для мультиформатного сообщения MIMEMultipart
#print(attachment)

#print(msg)
'''
server = smtplib.SMTP('smtp.gmail.com', 587)
#Send the mail
#msg = MIMEText('\n Тук-тук, проснись Нео, ты увяз в Матрице!'.encode('utf-8'), _charset='utf-8')
server.starttls()
server.login('vasaisvanov@gmail.com','Asdf210781')
server.sendmail("vasaisvanov@gmail.com", "gavryukov@mail.ru", msg.as_string())

server.quit()
'''

