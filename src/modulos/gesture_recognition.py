import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

from sistema.settings import ( MODELS_PATH )
from sistema.video import Video

import numpy as np 
import cv2 as cv

class Recognizer(object):


    def __init__(self):
        VisionRunningMode = mp.tasks.vision.RunningMode
        
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles


        self.base_options   = python.BaseOptions(
            model_asset_path    = os.path.join(MODELS_PATH, 'gesture_recognizer.task')
        )

        self.options        = vision.GestureRecognizerOptions(
                base_options    = self.base_options
            #running_mode=VisionRunningMode.VIDEO
        )

        self.recognizer     = vision.GestureRecognizer.create_from_options(
                self.options
        )


    def recognize(self, frame):
        mp_frame = mp.Image(
            image_format=mp.ImageFormat.SRGB, 
            data=frame
        )
        
        recognition_result = self.recognizer.recognize(
            mp_frame
        )

        if len(recognition_result.gestures) == 0:
            return frame

        gesture = recognition_result.gestures[0][0]
        gesture_name = gesture.category_name
        hand_landmarks = recognition_result.hand_landmarks

        for hand_landmark in hand_landmarks:
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmark
        ])

        self.mp_drawing.draw_landmarks(
            frame,
            hand_landmarks_proto,
            self.mp_hands.HAND_CONNECTIONS,
            self.mp_drawing_styles.get_default_hand_landmarks_style(),
            self.mp_drawing_styles.get_default_hand_connections_style()
        )

        return frame


    def serialize(self):
        pass


    def debug(self):
        v = Video()

        while True:
            frame = v.serialize()
            
            frame = self.recognize(frame)

            cv.imshow('Debug', frame)

            if cv.waitKey(1) == ord('q'):
                break

        v.close()
