from flask import Flask
from utils import load_model
from configuration import Configuration
import json


app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret!"
config = Configuration()
model = load_model(config)


@app.route("/", methods=["GET"])
def index():
    return "Hello"


@app.route("/recommendations/<id>", methods=["GET"])
def recommendations(id):
    if model.get(id):
       return json.dumps(model.get(id))

if __name__ == "__main__":

    app.run(threaded=True, port=5000, debug=True)

