import os
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

from sistema.settings import ( MODELS_PATH )

class Landmark(object):

    def __init__(self):
        VisionRunningMode = mp.tasks.vision.RunningMode
        
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles


        self.base_options   = python.BaseOptions(
            model_asset_path    = os.path.join(MODELS_PATH, 'gesture_recognizer.task')
        )

        self.options        = vision.GestureRecognizerOptions(
                base_options    = self.base_options,
                num_hands       = 2
        #        running_mode    = VisionRunningMode.VIDEO
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
            return frame, 0, 0, 0

        gesture = recognition_result.gestures[0][0]
        gesture_name = gesture.category_name
        hand_landmarks = recognition_result.hand_landmarks

        test_x = 0
        test_y = 0.0

        for hand_landmark in hand_landmarks:
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmark])

            self.mp_drawing.draw_landmarks(
                frame,
                hand_landmarks_proto,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style()
            )

        return frame, hand_landmarks[0][8].x * 100, hand_landmarks[0][8].y * 100, hand_landmarks[0][8].z * 10


    def read_gesture(self, frame):
        mp_frame = mp.Image(
            image_format=mp.ImageFormat.SRGB, 
            data=frame
        )
        
        recognition_result = self.recognizer.recognize(
            mp_frame
        )

        if len(recognition_result.gestures) == 0:
            return frame, None, 0

        gesture = recognition_result.gestures[0][0]
        gesture_name = gesture.category_name
        hand_landmarks = recognition_result.hand_landmarks

        print(gesture_name)

        for hand_landmark in hand_landmarks:
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend(
                [
                    landmark_pb2.NormalizedLandmark(
                        x=landmark.x, 
                        y=landmark.y, 
                        z=landmark.z
                    ) 
                    for landmark in hand_landmark
                ]
            )

            self.mp_drawing.draw_landmarks(
                frame,
                hand_landmarks_proto,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style()
            )

        return frame, gesture_name, hand_landmarks[0][8].x


    def serialize(self):
        pass
