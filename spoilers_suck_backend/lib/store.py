import fileinput
import json
import time

def save_to_file(show, entities):
    f = open('storage/%s.json' % show, 'w')
    jsonObject = {"show": show, "updated_at": int(time.time()), "entities": entities}
    json.dump(jsonObject, f)

def load_from_file(show):
    with open('storage/%s.json' % show, 'r') as file:
        data = json.load(file)
        print json.dumps(data, indent=4, separators=(',', ': '))
        return data
    