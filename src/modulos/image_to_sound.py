from modulos.gesture_recognition import Recognizer
from modulos.sound import Sound
from sistema.video import Video

import numpy as np 
import cv2 as cv
import threading
import time

class Image2Sound(object):

    def __init__(self):
        pass


    def debug(self):
        v = Video()
        s = Sound()
        r = Recognizer()
        
        _start = time.time()
        while True:
            frame = v.serialize()
            
            frame, x, y, z = r.recognize(frame)
            
            _end = time.time()
            if _end - _start > 0.4:
                x = threading.Thread(target=s.play, args=(x, y, z, ))
                x.start()
                _start = _end
            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break
        
        s.close()
        v.close()
