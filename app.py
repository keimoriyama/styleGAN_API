from flask import Flask, send_from_directory, request
from styleGAN import generate_cat_fugure
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})

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
        return send_from_directory(directory="./results/", filename="figure03-style-mixing15.png")


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False, threaded=False)