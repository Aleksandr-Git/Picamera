# не работает после принудительного отключения
# работет автоматическая трансляция при подключении и корректном завершении трансляции
# tcp/h264://192.168.1.70:8000/ ссылка для трансляции в VLC

import socket
import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 25

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

def fun():

# Примите одно соединение и создайте из него файловый объект
    with server_socket.accept()[0].makefile('wb') as connection:
#    connection = server_socket.accept()[0].makefile('wb')
#        try:
        camera.start_recording(connection, format='h264')
        print('satrt')
        camera.wait_recording(30)
        print('rec')
        camera.stop_recording()
        print('stop')

#    except Exception:h
#        connection.close()
#        server_socket.close()
#        print('close')
#        fun()
        
#    finally:
#        connection.close()
#        server_socket.close()
#        print('CLOSE')
#        fun()

while True:
    fun()
