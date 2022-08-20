from spacy import displacy
import spacy
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
app = Flask(__name__)
ors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
# @app.get("/", methods=["GET"])
def index():
    NER = spacy.load("en_core_web_sm")
    raw_text = "The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
    text1 = NER(raw_text)
    list_data = []
    for word in text1.ents:
        list_data.append([word.text, word.label_])
    return list_data


@app.route('/', methods=['POST'])
def update_record():
    NER = spacy.load("en_core_web_sm")
    record = json.loads(request.data)
    text1 = NER(record['det'])
    list_data = []
    for word in text1.ents:
        list_data.append([word.text, word.label_])
    return jsonify(list_data)
    # print(record)
    # return jsonify(record)

    if __name__ == '__main__':
        # Threaded option to enable multiple instances for multiple user access support
        app.run(threaded=True, port=5000)
