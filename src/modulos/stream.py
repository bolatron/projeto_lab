import struct
import socket
import cv2 as cv

from sistema.video import Video 
from sistema.settings import ( HOST, PORT )


class Stream(object):

    def __init__(self, is_server=False):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if is_server:
            self.socket.bind((HOST, PORT))
            self.socket.listen()
        else:
            self.socket.connect((HOST, PORT))


    def server(self):
        v = Video(is_client=False)
        conn, addr = self.socket.accept()

        PAYLOAD_SIZE = struct.calcsize("Q")

        streaming_data = b''

        while True:

            while len(streaming_data) < PAYLOAD_SIZE:
                packet = conn.recv(4 * 1024)
                if not packet: break
                streaming_data += packet

            packed_msg_size = streaming_data[:PAYLOAD_SIZE]
            streaming_data = streaming_data[PAYLOAD_SIZE:]
            video_msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(streaming_data) < video_msg_size:
                streaming_data += conn.recv(4 * 1024)
            
            serialized_frame = streaming_data[:video_msg_size]
            streaming_data = streaming_data[video_msg_size:]

            frame = v.deserialize(serialized_frame)
            cv.imshow("Stream", frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()
        self.close()


    def client(self):
        v = Video(is_client=True)

        while(True):
            serialized_frame = v.serialize()
            serialized_frame = struct.pack("Q", len(serialized_frame)) \
                + serialized_frame

            self.socket.sendall(serialized_frame)

        v.close()
        self.close()


    def close(self):
        self.socket.close()
