# делает фото в бефер
# записывает потоа его в файл
from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()
camera = PiCamera()
camera.resolution = (320, 240)
#camera.start_preview()
#sleep(1)
#camera.capture(stream, format='jpeg')
camera.capture(stream, 'jpeg')
# "Rewind" the stream to the beginning so we can read its content
#stream.seek(0)
#image = Image.open(stream)

#view = stream.getbuffer()
#print(len(view))

buff = stream.getvalue()  # записываем содержимое буфера в переменную

with open('./image_test_2.jpg', 'wb') as file:
    file.write(buff)
