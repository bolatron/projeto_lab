from modulos.gesture_recognition import Recognizer
from modulos.sound import Sound
from sistema.video import Video

import numpy as np 
import cv2 as cv

class Image2Sound(object):

    def __init__(self):
        pass


    def debug(self):
        v = Video()
        s = Sound()
        r = Recognizer()
        
        i=0
        while True:
            frame = v.serialize()
            
            frame, x, y = r.recognize(frame)
            
            s.play(x=int(x), y=y)
            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break
        
        s.close()
        v.close()
