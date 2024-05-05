import sistema.settings

from entrypoint.cli import CLI
from sys import argv

if __name__ == '__main__':

    if len(argv) != 2:
        print('Entrada ruim. Utilize python[3|3.10] src/main.py --help')
        exit(-1)

    CLI().handler(argv[1])
