from flask import Flask, request, render_template, flash, redirect
from utils import load_model
from configuration import Configuration
import json
from recommender.forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "top secret!"

config = Configuration()
model = load_model(config)


@app.route("/", methods=["GET"])
#@app.route("/index", methods=["GET","POST"])
def index():
    return render_template('index.html', title='Home')
#    article = None
#    form = InputForm(request.args)

#    if form.validate():
#    	article = request.args.get("article_id")
#    print("article = ", article)

#    return "Hello"
#    return render_template('index.html', title='Home', form=form, article=article) 

@app.route('/input', methods=["GET","POST"])
def input():
    global model
    article = None
    recommendations = None

    form = InputForm()

    '''
    if form.validate_on_submit():
        flash('Missing field for article_id={}'.format(form.article_id.data))
        return redirect('/input')
    else:
        recommendations = model.get(article)
    '''
    if form.validate():
    	article = request.form.get("article_id")
    

    #model.get(article) returns the recommendations      
    if model.get(article):
    	recommendations = model.get(article) #json.dump(model.get(article))

    print("article=", article, "recommendations = ", type(recommendations))
    
    return render_template('input.html', title='Input', form=form, article=article, recommendations=recommendations)

@app.route("/recommendations/<id>", methods=["GET"])
def recommendations(id):
    if model.get(id):
       return json.dumps(model.get(id))

if __name__ == "__main__":

    app.run(threaded=True, port=5000, debug=True)

