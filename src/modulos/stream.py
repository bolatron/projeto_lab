import struct
import socket
import cv2 as cv

from sistema.video import Video 
from sistema.settings import ( HOST, PORT )


class Stream(object):

    def __init__(self, is_server=False):
        self.socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if is_server:
            self.socket.bind((HOST, PORT))
            self.socket.listen()
        else:
            self.socket.connect((HOST, PORT))


    def server(self):

        v = Video()
        conn, addr = self.socket.accept()

        while True:
            serialized_frame = b''
            #payload = int.from_bytes(conn.recv(3), 'big')

            while len(serialized_frame) < 691200:
                serialized_frame += conn.recv(1024)

            serialized_frame = serialized_frame[:691200]

            frame = v.deserialize(serialized_frame)
            cv.imshow("Stream", frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()
        self.close()


    def client(self):

        v = Video()

        #while(True):
        #    serialized_frame = v.serialize()
        #    message = len(serialized_frame).to_bytes(3, 'big') + serialized_frame
        #    self.socket.sendall(message)
        
        while(True):
            self.socket.sendall(v.serialize())


        v.close()
        self.close()


    def close(self):
        self.socket.close()
