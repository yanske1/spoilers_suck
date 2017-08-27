from flask import Flask, request, jsonify
import json


from lib.text_test import TextTest
from lib.img_test import recognize_face

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world, spoilers suck."

@app.route('/text', methods=["POST"])
def text():
    print "text test route"
    if request.is_json:
        data = request.get_json()
        print json.dumps(data, indent=4, separators=(',', ': '))
        text = data["content"]
        should_censor = TextTest.compare_text(text)
        return json.dumps({"should_censor": should_censor}), 200, {'Content-Type': 'application/json'}

@app.route('/img', methods=["POST"])
def img():
    print "test img route"
    if request.is_json:
        data = request.get_json()
        print json.dumps(data, indent=4, separators=(',',': '))
        img_url = data["url"]

        print recognize_face(url='img_url', gallery_name='1')


if __name__ == '__main__':
    print "app started"
    print "generating keywords"
    TextTest.generate_keywords()
    TextTest.load_keywords()
    app.run()