from flask import Flask, request, render_template, flash, redirect, url_for
from typing import Dict, Any
from utils import load_model, load_catalog
from configuration import Configuration
import json
from recommender.forms import InputForm
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret!"

config = Configuration()
model = load_model(config)
catalog = load_catalog(config)


@app.route("/", methods=["GET"])
# @app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html", title="Home")


#    article = None
#    form = InputForm(request.args)

#    if form.validate():
#    	article = request.args.get("article_id")
#    print("article = ", article)

#    return "Hello"
#    return render_template('index.html', title='Home', form=form, article=article)


@app.route("/input", methods=["GET", "POST"])
def input():
    article = None
    recommendations = None
    titles = {}  # type: Dict[id, title]

    form = InputForm()
    """
    if form.validate_on_submit():
        #to render the message update the base template
        flash('Submit the paper_id{} of an article'.format(form.article_id.data))
        return redirect(url_for('input'))
    else:
        recommendations = model.get(article)
    """
    if form.validate():
        article = request.form.get("article_id")

    # model.get(article) returns the recommendations
    if model.get(article):
        recommendations = model.get(article)  # json.dump(model.get(article))
        print("article=", article, "recommendations = ", recommendations)
        if recommendations != None:
            print("recos are not empty")
            for reco in recommendations:
                title = catalog.get(reco, "")
                titles[reco] = title
        else:
            print("recos is empty")

    print(
        "article=",
        article,
        "title=",
        len(titles),
        "recommendations = ",
        len(recommendations),
    )

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
