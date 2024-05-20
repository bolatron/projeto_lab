import pickle
import cv2 as cv 
import numpy as np

from types import NoneType

class Video(object):

    def __init__(self, is_client):
        self.camera = cv.VideoCapture(0)

        self.WIDTH  = 640
        self.HEIGHT = 360

        if is_client:
            #TODO: Resizible dimensions
            #self.WIDTH  = int(self.camera.get(cv.CAP_PROP_FRAME_WIDTH))
            #self.HEIGHT = int(self.camera.get(cv.CAP_PROP_FRAME_HEIGHT))

            #self.WIDTH      = 640
            #self.HEIGHT     = 360

            if not self.camera.isOpened():
                raise('Não foi possível abrir a câmera.')


    def serialize(self) -> bytes:
        ret, frame = self.camera.read()

        if not ret:
            raise('Não foi possível receber o frame.')

        return pickle.dumps(frame)


    def deserialize(self, serialized_ndarray) -> np.ndarray:
        return pickle.loads(serialized_ndarray)


    def close(self) -> NoneType:
        self.camera.release()
        cv.destroyAllWindows()
