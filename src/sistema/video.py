from types import NoneType

import numpy as np 
import cv2 as cv 


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


    def debug(self) -> NoneType:
        while True:
            frame = self.serialize()
            
            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break

        self.close()
