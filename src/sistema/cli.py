import os
import time

from sistema.video import Video
from sistema.io import IO
from sistema.settings import ( DOCS_PATH )

from modulos.gesture_recognition import Recognizer
from modulos.image_to_sound import Image2Sound

class CLI(object):

    def __init__(self):
        pass


    def handler(self, flag):
        
        match flag:
            case '--debugging-video':
                self.debug_video()

            case '--debugging-recognizer':
                self.debug_recognizer()

            case '--debugging-sound':
                self.debug_sound()

            case '--help':
                self.help()

            case _:
                print('Flag não encontrada. Use --help para visualizar todas as opções')
        exit(0)        


    def debug_video(self):
        Video().debug()


    def debug_recognizer(self):
        Recognizer().debug()


    def debug_sound(self):
        Image2Sound().debug()
    

    def help(self):
        print(IO.read_as_utf8(DOCS_PATH, 'HELP.md'), end='')
