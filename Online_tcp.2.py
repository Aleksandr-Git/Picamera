# протестировать автоматическое подключение
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
                    camera.wait_recording(60)
                    print('rec')
                    camera.stop_recording()
                    print('stop')

            except Exception:
                print('break')
                break
    conn.close()
