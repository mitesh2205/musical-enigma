import spacy
from spacy import displacy
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
app = Flask(__name__)
ors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def index():
    return "HI this is flask app."


@app.route('/', methods=['POST'])
def update_record():
    NER = spacy.load("en_core_web_sm")
    record = json.loads(request.data)
    text1 = NER(record['det'])
    list_data = []
    for word in text1.ents:
        list_data.append([word.text, word.label_])
    return jsonify(list_data)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
