import os
import pygame
from sistema.settings import ( SOUNDS_PATH )

import threading
import time

class State(object):

    def __init__(self):
        self.STATES = [
            'normal',
            'insert',
            'edit',
            'visual',
            'exit'
        ]
        self.init_state = 'normal'
        self.curr_state = self.init_state
        self.end_state = 'exit'

        self.gesture_name = None
        self.enter_state = True
        self.can_play_audio = True
        self._start = time.time()
        self.position_x = 0


    def check(self, package):

        self.gesture_name = package[0]
        self.position_x = package[1]

        print(self.position_x)

        match self.curr_state:
            case 'normal':
                self.normal_state()
            case 'insert':
                self.insert_state()
            case 'exit':
                self.exit_state()


    def set_state(self, new_state):
        if new_state != self.curr_state:
            self.enter_state = True

        self.curr_state = new_state


    def normal_state(self):
        if self.enter_state:
            self.can_play_audio = True
            self.enter_state = False

        self.set_state(self.check_normal())

    def insert_state(self):
        if self.enter_state:
            _end = time.time()
            if _end - self._start > 0.4:
                x = threading.Thread(target=self.play)
                x.start()
                self.can_play_audio = False
                self._start = _end
            self.enter_state = False

        self.set_state(self.check_insert())

    def exit_state(self):
        exit(0)


    def check_normal(self):
        new_state = self.curr_state
        if self.gesture_name == 'Closed_Fist':
            new_state = 'insert'
        if self.curr_state in ['normal', 'insert'] and self.gesture_name == 'Victory':
            new_state = 'exit'
        return new_state


    def check_insert(self):
        new_state = self.curr_state
        if self.gesture_name in ['Open_Palm', 'Thumb_Up']:
            new_state = 'normal'

        if self.curr_state in ['normal', 'insert'] and self.gesture_name == 'Victory':
            new_state = 'exit'
        return new_state


    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUNDS_PATH, 'kick.ogg'))
        if self.position_x > 0.5:
            pygame.mixer.music.load(os.path.join(SOUNDS_PATH, 'snare.ogg'))
        else:
            pygame.mixer.music.load(os.path.join(SOUNDS_PATH, 'kick.ogg'))
        pygame.mixer.music.play()
        pygame.time.delay(1000)
        pygame.mixer.music.stop()
