from io import BytesIO
from time import sleep
from picamera import PiCamera
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

stream = BytesIO()  # создаем объект для записи потока
camera = PiCamera()
camera.resolution = (320, 240)

msg = MIMEMultipart()  # создаем контейнер для мультиформатного сообщения
attachment = MIMEBase('image', "jpeg")  # создаес объект класса MIMEBase и передвем тип - картинка с расширением jpg

def photo():
    camera.capture(stream, 'jpeg')  # сохраняем изображение в поток

#    view = stream.getbuffer()
#    print(len(view))

    buff_img = stream.getvalue()  # записываем содержимое буфера в переменную
    return buff_img

#with open('./image_test_4.jpg', 'wb') as file:
#    file.write(photo())

def send_mail(data):
    header = 'Content-Disposition', 'attachment; filename = "Test.jpg"'  # записываем в переменную заголовки

    attachment.set_payload(data)  # добавляем файл в байтах в объект MIMEBase
    #print(attachment)
    encoders.encode_base64(attachment)  # кодируем в base64
    #print(attachment)
    attachment.add_header(*header)  # добавляем поле заголовка и содержимое заголовка
#    print(attachment)
    msg.attach(attachment)  # добавляем объект MIMEBase в контейнер для мультиформатного сообщения MIMEMultipart
#    print(attachment)

    #print(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    #Send the mail
    #msg = MIMEText('\n Тук-тук, проснись Нео, ты увяз в Матрице!'.encode('utf-8'), _charset='utf-8')
    server.starttls()
    server.login('vasaisvanov@gmail.com','Asdf210781')
    server.sendmail("vasaisvanov@gmail.com", "gavryukov@mail.ru", msg.as_string())
    
    server.quit()

send_mail(photo())

