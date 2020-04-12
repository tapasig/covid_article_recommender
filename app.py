from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret!"


@app.route("/", methods=["GET"])
def index():
    return "Hello"


if __name__ == "__main__":

    app.run(threaded=True, port=5000, debug=True)

