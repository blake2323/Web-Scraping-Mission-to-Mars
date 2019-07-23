
from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
from pymongo import MongoClient
import scrape_mars

#syntax to create a MongoClient in Python
client = MongoClient("mongodb://127.0.0.1:27017");

app = Flask(__name__)

@app.route('/')
def index():
       mars = client.db.mars.find_one()
       return render_template("index.html", mars=mars)
       
@app.route('/scrape')
def scrape():
       mars = client.db.mars
       mars_data = scrape_mars.scrape_all()
       mars.update({}, mars_data, upsert=True)
       return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)