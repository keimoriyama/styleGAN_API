from flask import Flask, send_from_directory, request
from styleGAN import generate_cat_fugure
import os
from flask_cors import CORS
from PIL import Image
import base64
import json

app = Flask(__name__)
CORS(app, resources={r"/request/*": {"origins": "*"}})


@app.route('/')
def test():
    return 'hello world'


@app.route("/request/<color>/<variety>/<int:hair_length>/", methods=["GET"])
def index(color, variety, hair_length):
    if request.method == "GET":
        cat_hair_length = hair_length
        cat_color = color
        cat_variety = variety
        generate_cat_fugure(color=cat_color,
                            variety=cat_variety,
                            hair_length=cat_hair_length)
        #img_file = './results/figure03-style-mixing15.png'
        #b64 = base64.encodestring(open(img_file, 'rb').read())
        # dictdata = {
        #    "str": "image",
        #    "image": base64.b64encode(b64).decode('utf-8')
        # }
        #strdata = json.dumps(dictdata)
        # return strdata.encode()
        image = Image.open('./results/figure03-style-mixing15.png')
        image.save('./results/figure.jpg')
        return send_from_directory(directory="./results/", filename="figure.jpg")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, threaded=False)
