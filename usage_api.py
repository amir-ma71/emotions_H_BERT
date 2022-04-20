from flask import Flask, request
from langdetect import detect, DetectorFactory

from src.HebEMO import HebEMO


HebEMO_model = HebEMO()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



@app.route('/predict', methods=['POST'])
def prepare_text():

    request_data = request.get_json()

    sent = request_data['text']

    # Detect language of text
    try:
        DetectorFactory.seed = 0
        lang = detect(sent)
    except:
        return "No text enter",400

    if lang != "he":
        return "the language is not Hebrew, please type Hebrew language to detect topic.",400


    if len(sent)< 40:
        return "your text is too small, please type more words to detect",400
    # Prepare the text

    final_dict = HebEMO_model.hebemo(text=sent)

    # Return on a JSON format
    return final_dict


@app.route('/check', methods=['GET'])
def check():
    return "every things right! "

if __name__ == '__main__':

    app.run(host='0.0.0.0')
