from flask import Flask, request, jsonify
import json
from flask_socketio import SocketIO

from lib.text_test import TextTest

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
        return json.dumps({"should_censor": should_censor}), 200




if __name__ == '__main__':
    TextTest.load_keywords()
    app.run()