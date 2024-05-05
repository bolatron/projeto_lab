import os
import time

from sistema.io import IO
from sistema.settings import ( DOCS_PATH )

from modulos.debug import Debug

class CLI(object):

    def __init__(self):
        pass


    def handler(self, flag):
        
        match flag:
            case '--debugging-video':
                Debug.debug_video()

            case '--debugging-landmark':
                Debug.debug_landmark()

            case '--debugging-sound':
                Debug.debug_sound()

            case '--help':
                self.help()

            case _:
                print('Flag não encontrada. Use --help para visualizar todas as opções')
        exit(0)

    def help(self):
        print(IO.read_as_utf8(DOCS_PATH, 'HELP.md'), end='')
