from flask import Flask, request, render_template, flash, redirect, url_for
from utils import load_model, load_catalog
from configuration import Configuration
import json
from recommender.forms import InputForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret!"

config = Configuration()
model = load_model(config)
catalog = load_catalog(config)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Home")


@app.route("/input", methods=["GET", "POST"])
def input():
    article = None
    recommendations = None
    titles = {}

    form = InputForm()


    if form.validate():
        article = request.form.get("article_id")
        titles[article] = catalog.get(article, "")

    if model.get(article):
        recommendations = model.get(article)
        if recommendations != None:
            print("recos are not empty")
            for reco in recommendations:
                title = catalog.get(reco, "")
                titles[reco] = title
        else:
            print("recos is empty")

    return render_template(
        "input.html",
        titles=titles,
        form=form,
        article=article,
        recommendations=recommendations,
    )


@app.route("/recommendations/<id>", methods=["GET"])
def recommendations(id):
    if model.get(id):
        return json.dumps(model.get(id))


if __name__ == "__main__":

    app.run(threaded=True, port=5000, debug=True)
