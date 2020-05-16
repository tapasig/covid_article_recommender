from flask import Flask, request, render_template
from utils import load_model
from configuration import Configuration
import json
from recommender.forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret!"

config = Configuration()
model = load_model(config)


@app.route("/", methods=["GET"])

def index():
    return render_template('index.html', title='Home')
#    article = None
#    form = InputForm(request.args)
#    if form.validate():
#    	article = request.args.get("article_id")
#    return "Hello"
#    return render_template('index.html', title='Home', form=form, article=article) 

@app.route('/input')
def input():
    article = None
    form = InputForm()
    if form.validate():
           article = request.args.get("article_id")
    return render_template('input.html', title='Input', form=form, article=article)

@app.route("/recommendations/<id>", methods=["GET"])
def recommendations(id):
    if model.get(id):
       return json.dumps(model.get(id))

if __name__ == "__main__":

    app.run(threaded=True, port=5000, debug=True)

