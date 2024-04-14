# TODO
import numpy as np
import cv2 as cv

from sistema.video import Video

class Segmentation(object):

    def __init__(self):
        pass


    def depth_color_map(self, frame):
        return frame


    def debug(self):
        v = Video()

        while True:
            frame = v.serialize()
            
            frame = self.depth_color_map(frame)

            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()
