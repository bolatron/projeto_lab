from sistema.landmark import Landmark
from sistema.sound import Sound
from sistema.video import Video
from sistema.fsm import State 

import numpy as np 
import cv2 as cv
import threading
import time

class Debug(object):

    def debug_landmark():
        v = Video(is_client=True)
        l = Landmark()

        while True:
            frame = v.serialize()
            frame = v.deserialize(frame)

            frame, _, _, _ = l.recognize(frame)

            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()


    def debug_sound():
        v = Video(is_client=True)
        s = Sound()
        l = Landmark()
        
        _start = time.time()
        while True:
            frame = v.serialize()
            frame = v.deserialize(frame)
            
            frame, x, y, z = l.recognize(frame)
            
            _end = time.time()
            if _end - self._start > 0.4:
                x = threading.Thread(target=s.play, args=(x, y, z, ))
                x.start()
                self._start = _end
            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break
        
        s.close()
        v.close()


    def debug_video():
        v = Video(is_client=True)

        while True:
            frame = v.serialize() 
            frame = v.deserialize(frame)

            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()


    def debug_lab():
        v = Video(is_client=True)
        l = Landmark()
        s = State()

        while True:
            frame = v.serialize()
            frame = v.deserialize(frame)

            frame, gesture_name, position_x = l.read_gesture(frame)

            s.check((gesture_name, position_x))

            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()
