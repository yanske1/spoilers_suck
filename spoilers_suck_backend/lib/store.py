import fileinput
import json

def save_to_file(show, entities):
    f = open('storage/%s.json' % show, 'w')
    jsonObject = {"show": show, "updated_at": date.now(), "entities": entities}
    json.dump(jsonObject, f)

def load_from_file(show):
    with open('storage/%s.json' % show, 'r') as file:
        data = json.load(file)
        return data
    