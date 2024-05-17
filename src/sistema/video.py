import cv2 as cv 
import numpy as np

from types import NoneType

class Video(object):

    def __init__(self, is_client):
        self.camera = cv.VideoCapture(0)

        self.WIDTH  = -1
        self.HEIGHT = -1

        if is_client:
            #TODO: Resizible dimensions
            self.WIDTH  = int(self.camera.get(cv.CAP_PROP_FRAME_WIDTH))
            self.HEIGHT = int(self.camera.get(cv.CAP_PROP_FRAME_HEIGHT))

            #self.WIDTH      = 640
            #self.HEIGHT     = 360

            if not self.camera.isOpened():
                raise('Não foi possível abrir a câmera.')


    def serialize(self) -> bytes:
        ret, frame = self.camera.read()

        if not ret:
            raise('Não foi possível receber o frame.')

        return frame.tobytes()


    def deserialize(self, serialized_ndarray) -> np.ndarray:
        deserialized_ndarray = np.frombuffer(serialized_ndarray, dtype=np.uint8)
        frame = np.reshape(deserialized_ndarray, newshape=(self.HEIGHT, self.WIDTH))

        return frame


    def get_shape(self) -> tuple:
        return (int(self.HEIGHT / 10), int(self.WIDTH / 10))


    def set_shape(self, video_shape):
        self.HEIGHT, self.WIDTH = video_shape
        self.HEIGHT *= 10
        self.WIDTH  *= 10


    def close(self) -> NoneType:
        self.camera.release()
        cv.destroyAllWindows()
