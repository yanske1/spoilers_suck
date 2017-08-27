import fileinput
import json
import time
import os

def save_to_file(show, entities):
    f = open('storage/%s.json' % show, 'w')
    jsonObject = {"show": show, "updated_at": int(time.time()), "entities": entities}
    json.dump(jsonObject, f)

def load_from_file(show):
    path = 'storage/%s.json' % show
    if not (os.path.isfile(path) and os.path.getsize(path) > 0):
        return None
    with open(path, 'w+') as file:
        data = json.load(file)
        return data
    