from flask import Flask, request, jsonify
import json


from lib.text_test import TextTest
from lib.img_test import recognize_face
from lib.shows import Show

show_map = {}

class CheckInit(object):
    """Simple WSGI middleware to check if shows and entities have been initialized yet"""
    
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        global show_map
        print "check init middleware"
        if len(show_map) == 0:
            print "no shows initialized; initializing:"
            show_map = Show.initializeShows()
        else:
            print "shows already initialized, continuing to correct route"
        return self.app(environ, start_response)

app = Flask(__name__)

app.wsgi_app = CheckInit(app.wsgi_app)

@app.route('/')
def index():
    return "Hello world, spoilers suck."

@app.route('/text', methods=["POST"])
@app.route('/text/<show_name>', methods=["POST"])
def text(show_name='game_of_thrones'):
    print "text test route: %s" % show_name
    if request.is_json:
        data = request.get_json()
        print json.dumps(data, indent=4, separators=(',', ': '))
        text = data["content"]
        should_censor = show_map[show_name].text_tester.test_content(text)
        return json.dumps({"should_censor": should_censor}), 200, {'Content-Type': 'application/json'}
    else:
        return jsonify(error="no json provided"), 400

@app.route('/img', methods=["POST"])
def img():
    print "test img route"
    if request.is_json:
        data = request.get_json()
        print json.dumps(data, indent=4, separators=(',',': '))
        img_url = data["url"]
        result = recognize_face(url=img_url, gallery_name='1')

        try:
            if result["images"][0]["transaction"]["status"] == "success":
                return jsonify({"should_censor": True}), 200, {'Content-Type': 'application/json'}
        except:
            pass
        
    return jsonify({"should_censor": False}), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    print "app started"
    app.run()