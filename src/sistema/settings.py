import os
from sys import path
from pathlib import Path
from platform import system

BASE_PATH   = Path(__file__).resolve().parent.parent.parent
SRC_PATH    = Path(__file__).resolve().parent.parent

path.append(str(SRC_PATH))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# GET SSH PUBKEY
SSH_PUBKEY = ''
if os.path.exists(f'{Path.home()}/.ssh/id_rsa.pub'):
    with open(f'{Path.home()}/.ssh/id_rsa.pub', 'r') as f:
        SSH_PUBKEY = f.read().replace('\n', '')
# /////////////////////////////////////////////////////////////////////////////

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ROOT FOLDERS PATH

DOCS_PATH   = os.path.join(BASE_PATH, 'docs')
MODELS_PATH = os.path.join(BASE_PATH, 'models')
SOUNDS_PATH = os.path.join(BASE_PATH, 'sounds')

# /////////////////////////////////////////////////////////////////////////////

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# SERVER SETTINGS

HOST    = '127.0.0.1'
PORT    = 65432
# /////////////////////////////////////////////////////////////////////////////
