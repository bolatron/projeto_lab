import os
import json


class IO(object):

    def read_as_json(filepath, filename) -> dict:
        with open(os.path.join(filepath, filename), 'r', encoding='utf8') as f:
            data = json.load(f)
        return data


    def read_as_utf8(filepath, filename) -> str:
        with open(os.path.join(filepath, filename), 'r', encoding='utf8') as f:
            data = f.read()
        return data


    def update(filepath, filename, data):
        with open(os.path.join(filepath, filename), 'w', encoding='utf8') as f:
            json.dump(
                obj=data,
                fp=f, 
                ensure_ascii=False,
                indent='\t', 
                separators=(',', ': ')
            )
