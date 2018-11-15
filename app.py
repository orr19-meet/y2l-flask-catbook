from flask import Flask
from flask import *
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:n>',methods=['GET', 'POST'])
def catbook_cat(n):
	cat=get_cat_by_id(n)
	return render_template("cat.html", cat=cat)

@app.route("/create", methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('add_cat.html')
    else:
        name = request.form['catname']
       

        create_cat(name)        
        return redirect(url_for('catbook_home'))

@app.route('/vote/<int:id>',methods=['GET', 'POST'])
def vote(id):
	cat=get_cat_by_id(id)
	add_vote(id)
	return render_template("cat.html", cat=cat)


if __name__ == '__main__':
   app.run(debug = True)
