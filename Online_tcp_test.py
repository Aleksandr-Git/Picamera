# написать автоматическую трансляцию при подключении
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

# Примите одно соединение и создайте из него файловый объекn
while True:
    conn = server_socket.accept()[0]
    print('conn')

    while True:
        try:
            camera.stop_recording()
            print('STOP')
            connection.close()
            print('CLOSE')
        except Exception:
            try:
                with conn.makefile('wb') as connection:
                    camera.start_recording(connection, format='h264')
                    print('start')
                    camera.wait_recording(30)
                    print('rec')
                    camera.stop_recording()
                    print('stop')

            except Exception:
                print('break')
#                camera.stop_recording()
#                print('stop')
#                connection.close()
#                print('close')
                break
    conn.close()

#conn = server_socket.accept()[0]
#print('conn_2')
#with conn.makefile('wb') as connection:
#    camera.start_recording(connection, format='h264')
#    camera.wait_recording(30)
#    camera.stop_recording()
#conn.close()
#try:
#camera.start_recording(connection, format='h264')
#camera.wait_recording(30)
#camera.stop_recording()
#finally:
#connection.close()
#server_socket.accept()[0].close()

#connection.close()
#server_socket.close()

#connection = server_socket.accept()[0].makefile('wb')
#try:
#camera.start_recording(connection, format='h264')
#camera.wait_recording(30)
#camera.stop_recording()
#finally:
#connection.close()
#server_socket.accept()[0].close()
