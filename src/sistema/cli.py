import os
import time

from sistema.video import Video

class CLI(object):

    def __init__(self):
        pass


    def handler(self, flag):
        
        match flag:
            case '--debugging-video':
                self.debug_video()
        
            case '--help':
                self.help()

            case _:
                print('Flag não encontrada. Use --help para visualizar todas as opções')
        exit(0)        


    def debug_video(self):
        Video().debug()


    def help(self):
        with open('docs/HELP.md', 'r') as f:
            print(f.read(), end='')
