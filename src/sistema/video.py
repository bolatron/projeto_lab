import cv2 as cv 

from types import NoneType

class Video(object):

    def __init__(self):
        self.camera = cv.VideoCapture(0)

        if not self.camera.isOpened():
            raise('Não foi possível abrir a câmera.')


    def serialize(self) -> np.ndarray:
        ret, frame = self.camera.read()

        if not ret:
            raise('Não foi possível receber o frame.')

        return frame


    def close(self) -> NoneType:
        self.camera.release()
        cv.destroyAllWindows()
