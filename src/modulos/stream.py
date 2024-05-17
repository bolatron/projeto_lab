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

        while len(streaming_data) < PAYLOAD_SIZE:
            packet = conn.recv(1024)
            if not packet: break
            streaming_data += packet
        
        VIDEO_SHAPE_PAYLOAD = struct.unpack("Q", streaming_data[:PAYLOAD_SIZE])[0]
        streaming_data = streaming_data[PAYLOAD_SIZE:]

        while len(streaming_data) < VIDEO_SHAPE_PAYLOAD:
            streaming_data += conn.recv(1024)
        serialized_video_shape = streaming_data[:VIDEO_SHAPE_PAYLOAD]
        streaming_data = streaming_data[VIDEO_SHAPE_PAYLOAD:]

        video_shape = int.from_bytes(serialized_video_shape, byteorder='big')
        video_shape = tuple(video_shape.to_bytes(2, byteorder='big'))
        v.set_shape(video_shape)

        while True:

            # PAYLOAD
            while len(streaming_data) < PAYLOAD_SIZE:
                packet = conn.recv(1024)
                if not packet: break
                streaming_data += packet
            
            # VIDEO DATA
            VIDEO_PAYLOAD = struct.unpack("Q", streaming_data[:PAYLOAD_SIZE])[0]
            streaming_data = streaming_data[PAYLOAD_SIZE:]

            while len(streaming_data) < VIDEO_PAYLOAD:
                streaming_data += conn.recv(1024)
            serialized_frame = streaming_data[:VIDEO_PAYLOAD]
            streaming_data = streaming_data[VIDEO_PAYLOAD:]

            frame = v.deserialize(serialized_frame)
            cv.imshow("Stream", frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()
        self.close()


    def client(self):
        v = Video(is_client=True)

        video_shape = v.get_shape()

        serialized_video_shape = bytes(video_shape)
        serialized_video_shape = struct.pack("Q", len(serialized_video_shape)) \
            + serialized_video_shape

        self.socket.sendall(serialized_video_shape)

        while(True):
            serialized_frame = v.serialize()
            serialized_frame = struct.pack("Q", len(serialized_frame)) \
                + serialized_frame

            self.socket.sendall(serialized_frame)


        v.close()
        self.close()


    def close(self):
        self.socket.close()
