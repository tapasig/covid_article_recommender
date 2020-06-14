from flask import Flask, request, render_template, flash, redirect, url_for
from utils import load_model
from configuration import Configuration
import json
from recommender.forms import InputForm
import pandas as pd

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
    titles = {}
    catalog = None

    form = InputForm()
    '''
    if form.validate_on_submit():
    	#to render the message update the base template
        flash('Submit the paper_id{} of an article'.format(form.article_id.data))
        return redirect(url_for('input'))
    else:
        recommendations = model.get(article)
    '''
    if form.validate():
    	article = request.form.get("article_id")

    #model.get(article) returns the recommendations      
    if model.get(article):
        #query = article
    	recommendations = model.get(article) #json.dump(model.get(article))


    #read the title from csv file
    catalog = pd.read_csv('./data1/paper_catalog.csv')
    print("read catalog ", type(catalog))
#    print(type(article))

    for reco in recommendations:
        for index,row in catalog.itertuples(index=False):
           if (reco == index):
	        #print(article)
                titles[reco] = row


    print("article=", article, "title=", len(titles), "recommendations = ", len(recommendations))
    

    return render_template('input.html', titles=titles, form=form, article=article, recommendations=recommendations)

@app.route("/recommendations/<id>", methods=["GET"])
def recommendations(id):
    if model.get(id):
       return json.dumps(model.get(id))

if __name__ == "__main__":

    app.run(threaded=True, port=5000, debug=True)


